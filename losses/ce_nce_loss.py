# encoding: utf-8
"""
@author:  hungvm2
@contact: hung.ttkt1@gmail.com
"""
import torch
import torch.nn.functional as F
from .cross_entroy_loss import CrossEntropy
from .NCECriterion import NCECriterion
from .NCEAverage import NCEAverage


def extract_probs(probs):
    return probs[:, 0].mean()


class CENCE(torch.nn.Module):
    def __init__(self, args, len_neg, len_pos, beta=0.5, eps=0.1, alpha=0.2):
        super(CENCE, self).__init__()
        self.eps = eps
        self.alpha = alpha
        self.beta = beta
        self.ce = CrossEntropy(eps)
        self.nce_a = NCEAverage(args.feature_dim, len_neg, len_pos, args.tau, args.Z_momentum)
        self.nce = NCECriterion(len_neg)

    def forward(self, pred_class_outputs, n_train_batch_size, gt_classes):

        ### CE loss
        num_classes = pred_class_outputs.size(1)
        # print("gt_classes: ", gt_classes)
        if self.eps >= 0:
            smooth_param = self.eps
        else:
            # Adaptive label smooth regularization
            soft_label = F.softmax(pred_class_outputs, dim=1)
            smooth_param = self.alpha * soft_label[
                torch.arange(soft_label.size(0)), gt_classes].unsqueeze(1)

        ce_outs = F.softmax(pred_class_outputs, dim=1)
        # print("outs: ", outs)
        ce_probs, _ = torch.max(ce_outs, dim=1)
        log_probs = torch.log(ce_outs)
        # log_probs = F.log_softmax(pred_class_outputs, dim=1)
        with torch.no_grad():
            targets = torch.ones_like(log_probs)
            targets *= smooth_param / (num_classes - 1)
            targets.scatter_(1, gt_classes.to("cuda:0").data.unsqueeze(1), (1 - smooth_param))
        # print("targets: ", targets)
        ce_loss = (-targets * log_probs).sum(dim=1)

        with torch.no_grad():
            non_zero_cnt = max(ce_loss.nonzero(as_tuple=False).size(0), 1)

        # print("loss before averaging: ", loss)
        ce_loss = ce_loss.sum() / non_zero_cnt
        # probs_mean = 1
        ce_probs = ce_probs.mean()
        # print("probs size: ", probs.size(), "mean: ", probs_mean, "num_classes: ", num_classes,
        #       "loss: ", loss, "non_zero_cnt: ", non_zero_cnt)

        ### NCE loss
        n_vec = pred_class_outputs[0:n_train_batch_size]
        a_vec = pred_class_outputs[n_train_batch_size:]
        nce_outs, nce_probs = self.nce_a(n_vec, a_vec)
        nce_loss = self.nce(nce_outs)

        ### Combine
        loss = (1 - self.beta) * ce_loss + self.beta * nce_loss
        probs = (1 - self.beta) * ce_probs + self.beta * nce_probs
        return loss, pred_class_outputs, probs

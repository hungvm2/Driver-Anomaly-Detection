# encoding: utf-8
"""
@author:  l1aoxingyu
@contact: sherlockliao01@gmail.com
"""
import torch
import torch.nn.functional as F


# from fastreid.utils.events import get_event_storage
#
#
# def log_accuracy(pred_class_logits, gt_classes, topk=(1,)):
#     """
#     Log the accuracy metrics to EventStorage.
#     """
#     bsz = pred_class_logits.size(0)
#     maxk = max(topk)
#     _, pred_class = pred_class_logits.topk(maxk, 1, True, True)
#     pred_class = pred_class.t()
#     correct = pred_class.eq(gt_classes.view(1, -1).expand_as(pred_class))
#
#     ret = []
#     for k in topk:
#         correct_k = correct[:k].view(-1).float().sum(dim=0, keepdim=True)
#         ret.append(correct_k.mul_(1. / bsz))
#
#     storage = get_event_storage()
#     storage.put_scalar("cls_accuracy", ret[0])

def extract_probs(probs):
    return probs[:, 0].mean()


class CrossEntropy(torch.nn.Module):
    def __init__(self, eps, alpha=0.2):
        super(CrossEntropy, self).__init__()
        self.eps = eps
        self.alpha = alpha

    def forward(self, pred_class_outputs, gt_classes):
        num_classes = pred_class_outputs.size(1)
        # print("gt_classes: ", gt_classes)
        if self.eps >= 0:
            smooth_param = self.eps
        else:
            # Adaptive label smooth regularization
            soft_label = F.softmax(pred_class_outputs, dim=1)
            smooth_param = self.alpha * soft_label[
                torch.arange(soft_label.size(0)), gt_classes].unsqueeze(1)

        outs = F.softmax(pred_class_outputs, dim=1)
        # print("outs: ", outs)
        probs, _ = torch.max(outs, dim=1)
        log_probs = torch.log(outs)
        # log_probs = F.log_softmax(pred_class_outputs, dim=1)
        with torch.no_grad():
            targets = torch.ones_like(log_probs)
            targets *= smooth_param / (num_classes - 1)
            targets.scatter_(1, gt_classes.to("cuda:0").data.unsqueeze(1), (1 - smooth_param))
        print("targets: ", targets)
        print("gt_classes: ", gt_classes)
        loss = (-targets * log_probs).sum(dim=1)

        with torch.no_grad():
            non_zero_cnt = max(loss.nonzero(as_tuple=False).size(0), 1)

        # print("loss before averaging: ", loss)
        loss = loss.sum() / non_zero_cnt
        # probs_mean = 1
        probs_mean = probs.mean()
        # print("probs size: ", probs.size(), "mean: ", probs_mean, "num_classes: ", num_classes,
        #       "loss: ", loss, "non_zero_cnt: ", non_zero_cnt)
        return loss, pred_class_outputs, probs_mean

#
# def cross_entropy_loss(pred_class_outputs, gt_classes, eps, alpha=0.2):
#     num_classes = pred_class_outputs.size(1)
#
#     if eps >= 0:
#         smooth_param = eps
#     else:
#         # Adaptive label smooth regularization
#         soft_label = F.softmax(pred_class_outputs, dim=1)
#         smooth_param = alpha * soft_label[torch.arange(soft_label.size(0)), gt_classes].unsqueeze(1)
#
#     outs = F.softmax(pred_class_outputs, dim=1)
#     print("outs size: ", outs.size())
#     probs, _ = torch.max(outs, dim=1)
#     log_probs = torch.log(outs)
#     # log_probs = F.log_softmax(pred_class_outputs, dim=1)
#     with torch.no_grad():
#         targets = torch.ones_like(log_probs)
#         targets *= smooth_param / (num_classes - 1)
#         targets.scatter_(1, gt_classes.to("cuda:0").data.unsqueeze(1), (1 - smooth_param))
#     print("targets size: ", targets.size())
#     loss = (-targets * log_probs).sum(dim=1)
#
#     with torch.no_grad():
#         non_zero_cnt = max(loss.nonzero(as_tuple=False).size(0), 1)
#
#     print("loss before averaging: ", loss)
#     loss = loss.sum() / non_zero_cnt
#     # probs_mean = 1
#     probs_mean = probs.mean()
#     print("probs size: ", probs.size(), "mean: ", probs_mean, "num_classes: ", num_classes,
#           "loss: ", loss, "non_zero_cnt: ", non_zero_cnt)
#     return loss, pred_class_outputs, probs_mean
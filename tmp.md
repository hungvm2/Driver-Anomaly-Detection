NCE:
outs:  torch.Size([90, 151]) val:  tensor([[1.7202e-04, 1.7105e-04, 5.1162e-05,  ..., 1.8118e-04, 7.7928e-05,                                                                                                         
         6.3176e-05],                                                                                                                                                                                                 
        [1.5989e-04, 1.7105e-04, 5.1162e-05,  ..., 1.8118e-04, 7.7928e-05,                                                                                                                                            
         6.3176e-05],                                                                                                                                                                                                 
        [1.7571e-04, 1.7105e-04, 5.1162e-05,  ..., 1.8118e-04, 7.7928e-05,                                                                                                                                            
         6.3176e-05],                                                                                                                                                                                                 
        ...,                                                                                                                                                                                                          
        [8.3121e-05, 2.2754e-05, 1.2862e-04,  ..., 8.8591e-06, 9.5840e-05,                                                                                                                                            
         1.1201e-04],                                                                                                                                                                                                 
        [5.2121e-05, 2.2754e-05, 1.2862e-04,  ..., 8.8591e-06, 9.5840e-05,                                                                                                                                            
         1.1201e-04],                                                                                                                                                                                                 
        [9.1847e-05, 2.2754e-05, 1.2862e-04,  ..., 8.8591e-06, 9.5840e-05,                                                                                                                                            
         1.1201e-04]], device='cuda:0', grad_fn=<DivBackward0>)                                                                                                                                                       
probs:  torch.Size([]) val:  tensor(0.0067, device='cuda:0', grad_fn=<MeanBackward0>)                                                                                                                                 
loss:  torch.Size([1]) val:  tensor([6.1716], device='cuda:0', grad_fn=<DivBackward0>)


CE:
probs size:  torch.Size([160]) mean:  tensor(0.0181, device='cuda:0', grad_fn=<MeanBackward0>) num_classes:  128                                                                                                      
outs:  torch.Size([160, 128]) val:  tensor([[ 0.8227,  0.1060, -0.0215,  ..., -0.0439, -0.0178, -0.0537],                                                                                                             
        [ 0.8238,  0.1022, -0.0247,  ..., -0.0429, -0.0226, -0.0514],                                                                                                                                                 
        [ 0.8246,  0.1037, -0.0256,  ..., -0.0429, -0.0226, -0.0519],                                                                                                                                                 
        ...,                                                                                                                                                                                                          
        [ 0.8222,  0.1030, -0.0197,  ..., -0.0428, -0.0175, -0.0531],                                                                                                                                                 
        [ 0.8227,  0.1022, -0.0234,  ..., -0.0418, -0.0212, -0.0513],                                                                                                                                                 
        [ 0.8238,  0.1034, -0.0243,  ..., -0.0427, -0.0210, -0.0519]],                                                                                                                                                
       device='cuda:0', grad_fn=<DivBackward0>)                                                                                                                                                                       
probs:  torch.Size([]) val:  tensor(0.0181, device='cuda:0', grad_fn=<MeanBackward0>)                                                                                                                                 
loss:  torch.Size([]) val:  tensor(4.2194, device='cuda:0', grad_fn=<DivBackward0>)  
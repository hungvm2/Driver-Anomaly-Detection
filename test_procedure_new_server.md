Train 1->8
Val 1->2
epoches 100
val_step 1
nthreads 4

# Experiment 2:

Default (SGD optimizer, NCE loss, n/a batch 10/150, lr 0.01)
Epoches 100
Best Acc: 84.66 | Threshold: 0.87 | AUC: 0.9213

# Experiment 22:

SGD optimizer, CENCE loss (beta0.5, eps 0.0), no ce label smoothing, n/a batch 10/150
Best Acc: 88.34 | Threshold: 0.9 | AUC: 0.9407

# Experiment 26:

SGD optimizer, CENCE loss (beta0.4, eps 0.0), no ce label smoothing, n/a batch 10/150
Best Acc: 85.6 | Threshold: 0.82 | AUC: 0.922

# Experiment 27:

SGD optimizer, CENCE loss (beta0.6, eps 0.0), no ce label smoothing, n/a batch 10/150
Best Acc: 85.75 | Threshold: 0.84 | AUC: 0.9282

# Experiment 30:

SGD optimizer, CENCE loss (beta0.9, eps 0.0), no ce label smoothing, n/a batch 10/150
Best Acc: 83.48 | Threshold: 0.83 | AUC: 0.8896

# Experiment 23:

SGD optimizer, CENCE loss (beta0.5, eps 0.1), ce label smoothing, n/a batch 10/150
Best Acc: 88.19 | Threshold: 0.87 | AUC: 0.9388

# Experiment 28:

SGD optimizer, CENCE loss (beta0.5, eps 0.2), ce label smoothing, n/a batch 10/150
Best Acc: 84.71 | Threshold: 0.8 | AUC: 0.9137

# Experiment 29:

SGD optimizer, CENCE loss (beta0.5, eps 0.05), ce label smoothing, n/a batch 10/150
Best Acc: 84.52 | Threshold: 0.84 | AUC: 0.9002

# Experiment 24:

SGD optimizer, NCE loss, n/a batch 10/150, BasicCSP block in backbone (b type: 2 transition blocks)
Best Acc: 87.02 | Threshold: 0.86 | AUC: 0.9337
Total testing time: 2109.534331560135

# Experiment 31:

SGD optimizer, NCE loss, n/a batch 10/150, BasicCSP block in backbone (d type: fusion first, c type in paper)
Best Acc: 85.82 | Threshold: 0.78 | AUC: 0.9091
Total testing time: 2044.8548233509064

# Experiment 32:

SGD optimizer, NCE loss, n/a batch 10/150, BasicCSP block in backbone (c type: fusion last, d type in paper)
Best Acc: 83.26 | Threshold: 0.67 | AUC: 0.8873

Total testing time: 2147.911495447159

# Experiment 25:

SGD optimizer, n/a batch 10/150, BasicCSP block in backbone (b type: 2 transition blocks), CENCE loss (beta0.5, eps 0.0), no ce label smoothing,
Best Acc: 86.24 | Threshold: 0.87 | AUC: 0.9383
Total testing time: 2111.0074281692505

# Experiment 33:

SGD optimizer, NCE loss, n/a batch 10/150, lr 0.01, normal_downsample=3, downsample=2
Epoches 100


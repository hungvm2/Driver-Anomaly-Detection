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

# Experiment 23:
SGD optimizer, CENCE loss (beta0.5, eps 0.1), ce label smoothing, n/a batch 10/150

# Experiment 24:
SGD optimizer, NCE loss, n/a batch 10/150, BasicCSP block in backbone

# Experiment 25:
SGD optimizer, n/a batch 10/150, BasicCSP block in backbone, CENCE loss (beta0.5, eps 0.0), no ce label smoothing,

# Experiment 20: (not yet)

n_threads 4, Adam optimizer

# Experiment 21: (not yet)

n_threads 4, n/a_train_batch_size 32

# Eperiment : (not yet)

n_threads 4, n/a_train_batch_size 32, 1 projection heads, CENCE loss (beta0.8, eps 0.0 - no CE label smoothing).

# Eperiment 15:

n_threads 4, n/a_train_batch_size 32, 2 projection heads, ce head only has 1 hidden layer 64 nodes, CENCE loss (beta0.8, eps 0.0 - no CE label smoothing).

# Experiment 14: on going

n_threads 4, n/a_train_batch_size 32, 2 projection heads, ce head has 2 hidden layer 256 & 64 nodes, CENCE loss (beta0.8, eps 0.0 - no CE label smoothing).

# Eperiment 13:

n_threads 4, n/a_train_batch_size 32, 2 projection heads, ce head has 2 hidden layer 256 & 64 nodes, CENCE loss (beta0.8, eps 0.1 - CE label smoothing).
Best Acc: 90.7 | AUC: 0.9541

# Eperiment 17:

n_threads 4, n/a_train_batch_size 32, 2 projection heads, ce head has 2 hidden layer 256 & 64 nodes, CENCE loss (beta0.8, eps 0.2 - CE label smoothing).
Best Acc: 88.88 | Threshold: 0.78 | AUC: 0.9469

# Eperiment 18:

n_threads 4, n/a_train_batch_size 32, 2 projection heads, ce head has 2 hidden layer 256 & 64 nodes, CENCE loss (beta0.5, eps 0.1 - CE label smoothing).
Best Acc: 89.86 | Threshold: 0.71 | AUC: 0.9503

# Eperiment 19:

n_threads 4, n/a_train_batch_size 32, 2 projection heads, ce head has 2 hidden layer 256 & 64 nodes, CENCE loss (beta0.8, eps 0.1 - CE label smoothing), leaky ReLU activation.
Best Acc: 89.8 | Threshold: 0.69 | AUC: 0.941

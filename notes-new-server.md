```bash
cd /mnt/dad/hungvm/Driver-Anomaly-Detection
conda activate dad
python3 run.py -m train -n experiment
```

# Experiment 2 - new server Tesla T4:

Default, n_threads 4

## Train:
### Command:

```
python main.py --root_path /mnt/data/hungvm/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment2
python main.py --root_path /mnt/data/hungvm/DAD/ --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment2
python main.py --root_path /mnt/data/hungvm/DAD/ --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment2
python main.py --root_path /mnt/data/hungvm/DAD/ --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment2
python3 run.py -m train -n experiment2
```

## Test:
### Command: 
```bash
python3 run.py -m test -n experiment2
```

### Results:
Mode: Top(D):      Best Acc: 86.15 | Threshold: 0.79 | AUC: 0.8959
View: Top(D)(post-processed):       Best Acc: 86.21 | Threshold: 0.79 | AUC: 0.897 

Mode: Top(IR):      Best Acc: 80.97 | Threshold: 0.67 | AUC: 0.8586
View: Top(IR)(post-processed):       Best Acc: 81.05 | Threshold: 0.67 | AUC: 0.8609 

Mode: Top(DIR):      Best Acc: 85.64 | Threshold: 0.78 | AUC: 0.8981
View: Top(DIR)(post-processed):       Best Acc: 85.74 | Threshold: 0.78 | AUC: 0.8993 

Mode: Front(D):      Best Acc: 86.86 | Threshold: 0.85 | AUC: 0.8905
View: Front(D)(post-processed):       Best Acc: 87.0 | Threshold: 0.85 | AUC: 0.8929 

Mode: Front(IR):      Best Acc: 82.94 | Threshold: 0.83 | AUC: 0.863
View: Front(IR)(post-processed):       Best Acc: 83.11 | Threshold: 0.83 | AUC: 0.8665 

Mode: Front(DIR):      Best Acc: 87.83 | Threshold: 0.84 | AUC: 0.9126
View: Front(DIR)(post-processed):       Best Acc: 87.99 | Threshold: 0.84 | AUC: 0.915 

Mode: Fusion(D):      Best Acc: 89.63 | Threshold: 0.83 | AUC: 0.9492
View: Fusion(D)(post-processed):       Best Acc: 89.73 | Threshold: 0.82 | AUC: 0.9507 

Mode: Fusion(IR):      Best Acc: 85.44 | Threshold: 0.78 | AUC: 0.9131
View: Fusion(IR)(post-processed):       Best Acc: 85.55 | Threshold: 0.79 | AUC: 0.9155 

Mode: Fusion(DIR):      Best Acc: 89.78 | Threshold: 0.83 | AUC: 0.9516
View: Fusion(DIR)(post-processed):       Best Acc: 89.89 | Threshold: 0.83 | AUC: 0.9533 

Total testing time: 8901.237252235413

# Experiment 4:
Cross entropy eps 0.1
### command:
```
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.001 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name adam_nthreads4_ce --opt adam --loss ce --feature_dim 2
```

### Results:
Training Process is running: 250/250  | Batch: 51 | Loss: 0.35905003547668457 (0.362499570617309) | Probs: 0.8044182062149048 (0.8039084592690835)
Training Process is running: 250/250  | Batch: 52 | Loss: 0.35904690623283386 (0.3624344260062812) | Probs: 0.8044233322143555 (0.8039181738529565)
Training Process is running: 250/250  | Batch: 53 | Loss: 0.3661196231842041 (0.3625026703984649) | Probs: 0.8044205904006958 (0.8039274778630998)
Training Process is running: 250/250  | Batch: 54 | Loss: 0.3590617775917053 (0.3624401087110693) | Probs: 0.8043991327285767 (0.8039360534061085)
Training Process is running: 250/250  | Batch: 55 | Loss: 0.35906317830085754 (0.3623798063823155) | Probs: 0.8043968081474304 (0.8039442811693464)
Training Process is running: 250/250  | Batch: 56 | Loss: 0.3590504825115204 (0.3623213971915998) | Probs: 0.8044174313545227 (0.8039525820497881)
Training Process is running: 250/250  | Batch: 57 | Loss: 0.4050751030445099 (0.36260083317756653) | Probs: 0.8014804720878601 (0.8039364244683376)
==========================================!!!Evaluating!!!==========================================
================================================Evaluating================================================
Epoch: 250/250 | Accuracy: 0.7730250142875984 | Normal Acc: 0.8334885577434806 | Anormal Acc: 0.6552171095268956 | Threshold: 0.6
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  12777.573498487473

# Eperiment 9:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.0), 2 separated projection heads, data shuffle (wrong shuffle for NCE)

## Train:
### Command:

```
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32 --loss cence --head two_heads_cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32 --loss cence --head two_heads_cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32 --loss cence --head two_heads_cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32 --loss cence --head two_heads_cence
```

## Test:
```bash
python main.py --root_path /mnt/dad/hungvm/DAD --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32
```
Mode: Top(D):      Best Acc: 84.02 | Threshold: 0.97 | AUC: 0.8695
View: Top(D)(post-processed):       Best Acc: 84.11 | Threshold: 0.97 | AUC: 0.8714

Mode: Top(IR):      Best Acc: 80.99 | Threshold: 0.9 | AUC: 0.8498
View: Top(IR)(post-processed):       Best Acc: 81.11 | Threshold: 0.9 | AUC: 0.8521

Mode: Top(DIR):      Best Acc: 83.15 | Threshold: 0.94 | AUC: 0.8779
View: Top(DIR)(post-processed):       Best Acc: 83.23 | Threshold: 0.94 | AUC: 0.8797

Mode: Front(D):      Best Acc: 85.61 | Threshold: 0.87 | AUC: 0.8642
View: Front(D)(post-processed):       Best Acc: 85.68 | Threshold: 0.87 | AUC: 0.8657

Mode: Front(IR):      Best Acc: 83.88 | Threshold: 0.97 | AUC: 0.8746
View: Front(IR)(post-processed):       Best Acc: 84.16 | Threshold: 0.97 | AUC: 0.8785

Mode: Front(DIR):      Best Acc: 87.4 | Threshold: 0.92 | AUC: 0.8933
View: Front(DIR)(post-processed):       Best Acc: 87.48 | Threshold: 0.92 | AUC: 0.8952

Mode: Fusion(D):      Best Acc: 87.57 | Threshold: 0.92 | AUC: 0.913
View: Fusion(D)(post-processed):       Best Acc: 87.66 | Threshold: 0.93 | AUC: 0.9145

Mode: Fusion(IR):      Best Acc: 84.94 | Threshold: 0.94 | AUC: 0.912
View: Fusion(IR)(post-processed):       Best Acc: 85.13 | Threshold: 0.94 | AUC: 0.9144

Mode: Fusion(DIR):      Best Acc: 89.47 | Threshold: 0.94 | AUC: 0.9457
View: Fusion(DIR)(post-processed):       Best Acc: 89.59 | Threshold: 0.94 | AUC: 0.9474

Total testing time: 4015.3029034137726

# Eperiment 10:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.1), 1 projection heads, data shuffle (wrong shuffle for NCE)

## Train:
### Command:

```
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32 --loss cence
```

## Test:
```bash
python main.py --root_path /mnt/dad/hungvm/DAD --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32
```
Mode: Top(D):      Best Acc: 80.92 | Threshold: 0.97 | AUC: 0.8398
View: Top(D)(post-processed):       Best Acc: 80.98 | Threshold: 0.97 | AUC: 0.8414

Mode: Top(IR):      Best Acc: 81.32 | Threshold: 0.93 | AUC: 0.8603
View: Top(IR)(post-processed):       Best Acc: 81.4 | Threshold: 0.93 | AUC: 0.8622

Mode: Top(DIR):      Best Acc: 82.73 | Threshold: 0.95 | AUC: 0.8786
View: Top(DIR)(post-processed):       Best Acc: 82.79 | Threshold: 0.95 | AUC: 0.88

Mode: Front(D):      Best Acc: 84.17 | Threshold: 0.9 | AUC: 0.8526
View: Front(D)(post-processed):       Best Acc: 84.24 | Threshold: 0.9 | AUC: 0.8541

Mode: Front(IR):      Best Acc: 78.5 | Threshold: 0.97 | AUC: 0.801
View: Front(IR)(post-processed):       Best Acc: 78.63 | Threshold: 0.97 | AUC: 0.8043

Mode: Front(DIR):      Best Acc: 85.14 | Threshold: 0.94 | AUC: 0.8745
View: Front(DIR)(post-processed):       Best Acc: 85.22 | Threshold: 0.94 | AUC: 0.8762

Mode: Fusion(D):      Best Acc: 84.85 | Threshold: 0.94 | AUC: 0.8911
View: Fusion(D)(post-processed):       Best Acc: 84.9 | Threshold: 0.94 | AUC: 0.8924

Mode: Fusion(IR):      Best Acc: 83.54 | Threshold: 0.96 | AUC: 0.8989
View: Fusion(IR)(post-processed):       Best Acc: 83.66 | Threshold: 0.96 | AUC: 0.901

Mode: Fusion(DIR):      Best Acc: 87.39 | Threshold: 0.95 | AUC: 0.933
View: Fusion(DIR)(post-processed):       Best Acc: 87.45 | Threshold: 0.95 | AUC: 0.9344

Total testing time: 4035.602260828018


# Eperiment 11:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.0), 2 projection heads, no data shuffle (not suitable for CE)

## Train:
### Command:

```
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment11 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment11 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment11 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment11 --loss cence
```

## Test:
```bash
python main.py --root_path /mnt/dad/hungvm/DAD --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name experiment11
```

Mode: Top(D):      Best Acc: 85.33 | Threshold: 0.79 | AUC: 0.903
View: Top(D)(post-processed):       Best Acc: 85.41 | Threshold: 0.79 | AUC: 0.9043

Mode: Top(IR):      Best Acc: 82.24 | Threshold: 0.64 | AUC: 0.8712
View: Top(IR)(post-processed):       Best Acc: 82.31 | Threshold: 0.64 | AUC: 0.8734

Mode: Top(DIR):      Best Acc: 85.4 | Threshold: 0.72 | AUC: 0.9021
View: Top(DIR)(post-processed):       Best Acc: 85.48 | Threshold: 0.72 | AUC: 0.9035

Mode: Front(D):      Best Acc: 85.02 | Threshold: 0.48 | AUC: 0.8848
View: Front(D)(post-processed):       Best Acc: 85.04 | Threshold: 0.52 | AUC: 0.8865

Mode: Front(IR):      Best Acc: 82.0 | Threshold: 0.52 | AUC: 0.846
View: Front(IR)(post-processed):       Best Acc: 82.08 | Threshold: 0.52 | AUC: 0.8488

Mode: Front(DIR):      Best Acc: 87.28 | Threshold: 0.64 | AUC: 0.9034
View: Front(DIR)(post-processed):       Best Acc: 87.37 | Threshold: 0.64 | AUC: 0.9054

Mode: Fusion(D):      Best Acc: 87.93 | Threshold: 0.73 | AUC: 0.9443
View: Fusion(D)(post-processed):       Best Acc: 88.0 | Threshold: 0.73 | AUC: 0.9456

Mode: Fusion(IR):      Best Acc: 87.0 | Threshold: 0.68 | AUC: 0.9227
View: Fusion(IR)(post-processed):       Best Acc: 87.14 | Threshold: 0.68 | AUC: 0.9251

Mode: Fusion(DIR):      Best Acc: 90.45 | Threshold: 0.7 | AUC: 0.9537
View: Fusion(DIR)(post-processed):       Best Acc: 90.55 | Threshold: 0.7 | AUC: 0.9553

Total testing time: 4016.4514017105103

# Eperiment 12:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.1), ce label smoothing, 2 projection heads correct output, no data shuffle (not suitable for CE)

## Train:
### Command:

```
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment12 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment12 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment12 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment12 --loss cence
```

## Test:
```bash
python main.py --root_path /mnt/dad/hungvm/DAD --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name experiment12
```
Mode: Top(D):      Best Acc: 86.87 | Threshold: 0.78 | AUC: 0.8999
View: Top(D)(post-processed):       Best Acc: 86.95 | Threshold: 0.8 | AUC: 0.9013

Mode: Top(IR):      Best Acc: 79.57 | Threshold: 0.68 | AUC: 0.8456
View: Top(IR)(post-processed):       Best Acc: 79.67 | Threshold: 0.68 | AUC: 0.8478

Mode: Top(DIR):      Best Acc: 84.1 | Threshold: 0.66 | AUC: 0.8936
View: Top(DIR)(post-processed):       Best Acc: 84.16 | Threshold: 0.67 | AUC: 0.8951

Mode: Front(D):      Best Acc: 83.49 | Threshold: 0.26 | AUC: 0.8656
View: Front(D)(post-processed):       Best Acc: 83.52 | Threshold: 0.26 | AUC: 0.8668

Mode: Front(IR):      Best Acc: 83.58 | Threshold: 0.51 | AUC: 0.8721
View: Front(IR)(post-processed):       Best Acc: 83.68 | Threshold: 0.51 | AUC: 0.8748

Mode: Front(DIR):      Best Acc: 85.67 | Threshold: 0.46 | AUC: 0.8991
View: Front(DIR)(post-processed):       Best Acc: 85.81 | Threshold: 0.47 | AUC: 0.9009

Mode: Fusion(D):      Best Acc: 88.69 | Threshold: 0.6 | AUC: 0.9205
View: Fusion(D)(post-processed):       Best Acc: 88.77 | Threshold: 0.6 | AUC: 0.9218

Mode: Fusion(IR):      Best Acc: 86.95 | Threshold: 0.65 | AUC: 0.9234
View: Fusion(IR)(post-processed):       Best Acc: 87.08 | Threshold: 0.65 | AUC: 0.9255

Mode: Fusion(DIR):      Best Acc: 90.02 | Threshold: 0.63 | AUC: 0.9446
View: Fusion(DIR)(post-processed):       Best Acc: 90.12 | Threshold: 0.64 | AUC: 0.9462

Total testing time: 3944.7568674087524

# Eperiment 13:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.1), 2 projection heads correct output, correct data shuffle

## Train:
### Command:

```
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment13 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment13 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment13 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment13 --loss cence
```

## Test:
```bash
python main.py --root_path /mnt/dad/hungvm/DAD --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name experiment13
```

Mode: Top(D):      Best Acc: 84.56 | Threshold: 0.79 | AUC: 0.8859
View: Top(D)(post-processed):       Best Acc: 84.62 | Threshold: 0.79 | AUC: 0.8871

Mode: Top(IR):      Best Acc: 81.47 | Threshold: 0.64 | AUC: 0.864
View: Top(IR)(post-processed):       Best Acc: 81.51 | Threshold: 0.64 | AUC: 0.8658

Mode: Top(DIR):      Best Acc: 85.72 | Threshold: 0.7 | AUC: 0.8967
View: Top(DIR)(post-processed):       Best Acc: 85.77 | Threshold: 0.7 | AUC: 0.898

Mode: Front(D):      Best Acc: 85.59 | Threshold: 0.62 | AUC: 0.8971
View: Front(D)(post-processed):       Best Acc: 85.72 | Threshold: 0.63 | AUC: 0.8992

Mode: Front(IR):      Best Acc: 82.11 | Threshold: 0.38 | AUC: 0.8472
View: Front(IR)(post-processed):       Best Acc: 82.16 | Threshold: 0.38 | AUC: 0.8485

Mode: Front(DIR):      Best Acc: 87.02 | Threshold: 0.59 | AUC: 0.9113
View: Front(DIR)(post-processed):       Best Acc: 87.16 | Threshold: 0.58 | AUC: 0.9131

Mode: Fusion(D):      Best Acc: 88.92 | Threshold: 0.72 | AUC: 0.9435
View: Fusion(D)(post-processed):       Best Acc: 89.03 | Threshold: 0.72 | AUC: 0.945

Mode: Fusion(IR):      Best Acc: 85.58 | Threshold: 0.6 | AUC: 0.9125
View: Fusion(IR)(post-processed):       Best Acc: 85.7 | Threshold: 0.61 | AUC: 0.9143

Mode: Fusion(DIR):      Best Acc: 90.7 | Threshold: 0.68 | AUC: 0.9541
View: Fusion(DIR)(post-processed):       Best Acc: 90.8 | Threshold: 0.68 | AUC: 0.9556

Total testing time: 4018.727103471756


# Experiment 14:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.0), no ce label smoothing, 2 projection heads correct output, correct data shuffle

## Train:
### Command:

```
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment14 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment14 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment14 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment14 --loss cence
```

## Test:
```bash
python main.py --root_path /mnt/dad/hungvm/DAD --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name experiment14
```

Mode: Top(D):      Best Acc: 85.31 | Threshold: 0.74 | AUC: 0.8998
View: Top(D)(post-processed):       Best Acc: 85.41 | Threshold: 0.75 | AUC: 0.9009

Mode: Top(IR):      Best Acc: 81.98 | Threshold: 0.71 | AUC: 0.8636
View: Top(IR)(post-processed):       Best Acc: 82.07 | Threshold: 0.71 | AUC: 0.8657

Mode: Top(DIR):      Best Acc: 85.93 | Threshold: 0.7 | AUC: 0.9008
View: Top(DIR)(post-processed):       Best Acc: 86.0 | Threshold: 0.7 | AUC: 0.9021

Mode: Front(D):      Best Acc: 86.23 | Threshold: 0.47 | AUC: 0.8896
View: Front(D)(post-processed):       Best Acc: 86.29 | Threshold: 0.47 | AUC: 0.8916

Mode: Front(IR):      Best Acc: 82.88 | Threshold: 0.39 | AUC: 0.8697
View: Front(IR)(post-processed):       Best Acc: 82.99 | Threshold: 0.39 | AUC: 0.8713

Mode: Front(DIR):      Best Acc: 86.51 | Threshold: 0.45 | AUC: 0.9134
View: Front(DIR)(post-processed):       Best Acc: 86.59 | Threshold: 0.45 | AUC: 0.915

Mode: Fusion(D):      Best Acc: 89.14 | Threshold: 0.65 | AUC: 0.9403
View: Fusion(D)(post-processed):       Best Acc: 89.21 | Threshold: 0.66 | AUC: 0.9417

Mode: Fusion(IR):      Best Acc: 86.32 | Threshold: 0.63 | AUC: 0.9211
View: Fusion(IR)(post-processed):       Best Acc: 86.46 | Threshold: 0.63 | AUC: 0.9228

Mode: Fusion(DIR):      Best Acc: 89.77 | Threshold: 0.65 | AUC: 0.9519
View: Fusion(DIR)(post-processed):       Best Acc: 89.87 | Threshold: 0.65 | AUC: 0.9533

Total testing time: 4004.8939015865326

# Experiment 15:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.0), no ce label smoothing, 2 projection heads correct output, correct data shuffle, ce head only has 1 hidden layer 64 nodes.

## Test:
```bash
python main.py --root_path /mnt/dad/hungvm/DAD --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name experiment15
```
Mode: Top(D):      Best Acc: 84.74 | Threshold: 0.68 | AUC: 0.8875
View: Top(D)(post-processed):       Best Acc: 84.78 | Threshold: 0.68 | AUC: 0.8888 

Mode: Top(IR):      Best Acc: 81.27 | Threshold: 0.65 | AUC: 0.8698
View: Top(IR)(post-processed):       Best Acc: 81.37 | Threshold: 0.67 | AUC: 0.8714 

Mode: Top(DIR):      Best Acc: 84.65 | Threshold: 0.65 | AUC: 0.8989
View: Top(DIR)(post-processed):       Best Acc: 84.72 | Threshold: 0.65 | AUC: 0.9001 

Mode: Front(D):      Best Acc: 84.83 | Threshold: 0.64 | AUC: 0.8672
View: Front(D)(post-processed):       Best Acc: 84.95 | Threshold: 0.66 | AUC: 0.8698 

Mode: Front(IR):      Best Acc: 79.87 | Threshold: 0.31 | AUC: 0.8317
View: Front(IR)(post-processed):       Best Acc: 79.95 | Threshold: 0.33 | AUC: 0.8335 

Mode: Front(DIR):      Best Acc: 85.1 | Threshold: 0.55 | AUC: 0.8827
View: Front(DIR)(post-processed):       Best Acc: 85.23 | Threshold: 0.54 | AUC: 0.8847 

Mode: Fusion(D):      Best Acc: 90.67 | Threshold: 0.73 | AUC: 0.9462
View: Fusion(D)(post-processed):       Best Acc: 90.78 | Threshold: 0.73 | AUC: 0.948 

Mode: Fusion(IR):      Best Acc: 84.31 | Threshold: 0.57 | AUC: 0.905
View: Fusion(IR)(post-processed):       Best Acc: 84.45 | Threshold: 0.57 | AUC: 0.9067 

Mode: Fusion(DIR):      Best Acc: 89.35 | Threshold: 0.68 | AUC: 0.9454
View: Fusion(DIR)(post-processed):       Best Acc: 89.48 | Threshold: 0.68 | AUC: 0.947 

Total testing time: 4020.322322368622

# Experiment 16:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.1), ce label smoothing, 2 projection heads correct output, correct data shuffle, lr 0.001. (not good since source code already has lr schedule, * 0.1 every 100 epoches)

## Train:
### Command:

```
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.001 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment16 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.001 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment16 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.001 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment16 --loss cence
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.001 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment16 --loss cence
```

## Test:
```bash
python main.py --root_path /mnt/dad/hungvm/DAD --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name experiment16
```
Mode: Top(D):      Best Acc: 83.81 | Threshold: 0.78 | AUC: 0.8789
View: Top(D)(post-processed):       Best Acc: 83.89 | Threshold: 0.78 | AUC: 0.8802 

Mode: Top(IR):      Best Acc: 82.71 | Threshold: 0.78 | AUC: 0.87
View: Top(IR)(post-processed):       Best Acc: 82.81 | Threshold: 0.79 | AUC: 0.8718 

Mode: Top(DIR):      Best Acc: 84.52 | Threshold: 0.81 | AUC: 0.8965
View: Top(DIR)(post-processed):       Best Acc: 84.6 | Threshold: 0.81 | AUC: 0.8977 

Mode: Front(D):      Best Acc: 85.29 | Threshold: 0.75 | AUC: 0.8961
View: Front(D)(post-processed):       Best Acc: 85.41 | Threshold: 0.75 | AUC: 0.8979 

Mode: Front(IR):      Best Acc: 83.12 | Threshold: 0.53 | AUC: 0.8579
View: Front(IR)(post-processed):       Best Acc: 83.2 | Threshold: 0.54 | AUC: 0.8598 

Mode: Front(DIR):      Best Acc: 87.68 | Threshold: 0.68 | AUC: 0.9135
View: Front(DIR)(post-processed):       Best Acc: 87.8 | Threshold: 0.68 | AUC: 0.9154 

Mode: Fusion(D):      Best Acc: 88.75 | Threshold: 0.78 | AUC: 0.9415
View: Fusion(D)(post-processed):       Best Acc: 88.82 | Threshold: 0.78 | AUC: 0.9429 

Mode: Fusion(IR):      Best Acc: 86.58 | Threshold: 0.71 | AUC: 0.9188
View: Fusion(IR)(post-processed):       Best Acc: 86.73 | Threshold: 0.71 | AUC: 0.9207 

Mode: Fusion(DIR):      Best Acc: 90.24 | Threshold: 0.77 | AUC: 0.9522
View: Fusion(DIR)(post-processed):       Best Acc: 90.35 | Threshold: 0.77 | AUC: 0.9537 

Total testing time: 4017.3832199573517

# Experiment 17:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.2), ce label smoothing, 2 projection heads correct output, correct data shuffle.

## Train:
### Command:
```bash
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment17 --loss cence
```

Mode: Top(D):      Best Acc: 82.8 | Threshold: 0.88 | AUC: 0.8827
View: Top(D)(post-processed):       Best Acc: 82.86 | Threshold: 0.88 | AUC: 0.8841

Mode: Top(IR):      Best Acc: 82.56 | Threshold: 0.78 | AUC: 0.8787
View: Top(IR)(post-processed):       Best Acc: 82.64 | Threshold: 0.78 | AUC: 0.8807

Mode: Top(DIR):      Best Acc: 84.36 | Threshold: 0.84 | AUC: 0.8982
View: Top(DIR)(post-processed):       Best Acc: 84.44 | Threshold: 0.83 | AUC: 0.8995

Mode: Front(D):      Best Acc: 85.32 | Threshold: 0.66 | AUC: 0.8935
View: Front(D)(post-processed):       Best Acc: 85.43 | Threshold: 0.67 | AUC: 0.8953

Mode: Front(IR):      Best Acc: 81.13 | Threshold: 0.59 | AUC: 0.849
View: Front(IR)(post-processed):       Best Acc: 81.21 | Threshold: 0.59 | AUC: 0.8515

Mode: Front(DIR):      Best Acc: 86.45 | Threshold: 0.69 | AUC: 0.9084
View: Front(DIR)(post-processed):       Best Acc: 86.55 | Threshold: 0.69 | AUC: 0.9103

Mode: Fusion(D):      Best Acc: 87.55 | Threshold: 0.76 | AUC: 0.9349
View: Fusion(D)(post-processed):       Best Acc: 87.66 | Threshold: 0.77 | AUC: 0.9363

Mode: Fusion(IR):      Best Acc: 85.65 | Threshold: 0.73 | AUC: 0.9176
View: Fusion(IR)(post-processed):       Best Acc: 85.77 | Threshold: 0.73 | AUC: 0.9196

Mode: Fusion(DIR):      Best Acc: 88.88 | Threshold: 0.78 | AUC: 0.9469
View: Fusion(DIR)(post-processed):       Best Acc: 88.99 | Threshold: 0.78 | AUC: 0.9484

Total testing time: 4041.0384356975555

# Experiment 18:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.5, eps 0.1), ce label smoothing, 2 projection heads correct output, correct data shuffle.

## Train:
### Command:
```bash
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment18 --loss cence
```

Mode: Top(D):      Best Acc: 84.38 | Threshold: 0.67 | AUC: 0.8876
View: Top(D)(post-processed):       Best Acc: 84.4 | Threshold: 0.68 | AUC: 0.8888

Mode: Top(IR):      Best Acc: 81.49 | Threshold: 0.67 | AUC: 0.8656
View: Top(IR)(post-processed):       Best Acc: 81.57 | Threshold: 0.67 | AUC: 0.8679

Mode: Top(DIR):      Best Acc: 84.96 | Threshold: 0.7 | AUC: 0.896
View: Top(DIR)(post-processed):       Best Acc: 85.03 | Threshold: 0.7 | AUC: 0.8972

Mode: Front(D):      Best Acc: 85.16 | Threshold: 0.65 | AUC: 0.8786
View: Front(D)(post-processed):       Best Acc: 85.23 | Threshold: 0.66 | AUC: 0.8808

Mode: Front(IR):      Best Acc: 83.56 | Threshold: 0.46 | AUC: 0.8592
View: Front(IR)(post-processed):       Best Acc: 83.65 | Threshold: 0.46 | AUC: 0.8616

Mode: Front(DIR):      Best Acc: 87.29 | Threshold: 0.65 | AUC: 0.9043
View: Front(DIR)(post-processed):       Best Acc: 87.4 | Threshold: 0.65 | AUC: 0.9062

Mode: Fusion(D):      Best Acc: 88.22 | Threshold: 0.72 | AUC: 0.9321
View: Fusion(D)(post-processed):       Best Acc: 88.27 | Threshold: 0.72 | AUC: 0.9335

Mode: Fusion(IR):      Best Acc: 87.75 | Threshold: 0.66 | AUC: 0.9261
View: Fusion(IR)(post-processed):       Best Acc: 87.9 | Threshold: 0.66 | AUC: 0.9283

Mode: Fusion(DIR):      Best Acc: 89.86 | Threshold: 0.71 | AUC: 0.9503
View: Fusion(DIR)(post-processed):       Best Acc: 89.92 | Threshold: 0.71 | AUC: 0.9518

Total testing time: 4022.2939965724945

# Experiment 19:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.1), ce label smoothing, 2 projection heads correct output, correct data shuffle. leaky relu activation.

## Train:
### Command:
```bash
python main.py --root_path /mnt/dad/hungvm/DAD --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name experiment19 --loss cence
```

Mode: Top(D):      Best Acc: 83.52 | Threshold: 0.74 | AUC: 0.8894
View: Top(D)(post-processed):       Best Acc: 83.58 | Threshold: 0.73 | AUC: 0.8906 

Mode: Top(IR):      Best Acc: 82.21 | Threshold: 0.72 | AUC: 0.8631
View: Top(IR)(post-processed):       Best Acc: 82.26 | Threshold: 0.74 | AUC: 0.8651 

Mode: Top(DIR):      Best Acc: 85.48 | Threshold: 0.74 | AUC: 0.8951
View: Top(DIR)(post-processed):       Best Acc: 85.54 | Threshold: 0.71 | AUC: 0.8965 

Mode: Front(D):      Best Acc: 84.19 | Threshold: 0.46 | AUC: 0.8744
View: Front(D)(post-processed):       Best Acc: 84.24 | Threshold: 0.47 | AUC: 0.8761 

Mode: Front(IR):      Best Acc: 80.03 | Threshold: 0.41 | AUC: 0.8084
View: Front(IR)(post-processed):       Best Acc: 80.1 | Threshold: 0.41 | AUC: 0.8104 

Mode: Front(DIR):      Best Acc: 83.96 | Threshold: 0.53 | AUC: 0.8838
View: Front(DIR)(post-processed):       Best Acc: 84.09 | Threshold: 0.53 | AUC: 0.8858 

Mode: Fusion(D):      Best Acc: 88.8 | Threshold: 0.68 | AUC: 0.9328
View: Fusion(D)(post-processed):       Best Acc: 88.91 | Threshold: 0.68 | AUC: 0.9343 

Mode: Fusion(IR):      Best Acc: 83.75 | Threshold: 0.65 | AUC: 0.8916
View: Fusion(IR)(post-processed):       Best Acc: 83.91 | Threshold: 0.65 | AUC: 0.8937 

Mode: Fusion(DIR):      Best Acc: 89.8 | Threshold: 0.69 | AUC: 0.941
View: Fusion(DIR)(post-processed):       Best Acc: 89.92 | Threshold: 0.69 | AUC: 0.9427 

Total testing time: 3862.8063626289368

- csp network




Traceback (most recent call last):                                                                                                                                                                                    
  File "/mnt/dad/hungvm/Driver-Anomaly-Detection/dataset.py", line 17, in pil_loader                                                                                                                                  
    with open(path, 'rb') as f:                                                                                                                                                                                       
FileNotFoundError: [Errno 2] No such file or directory: '/mnt/dad/hungvm/DAD/Tester4/normal_driving_5/front_IR/img_14528.png'                                                                                         
/mnt/dad/hungvm/DAD/Tester4/normal_driving_5/front_IR/img_14528.png                                                                                                                                                   
Traceback (most recent call last):                                                                                                                                                                                    
  File "/mnt/dad/hungvm/Driver-Anomaly-Detection/dataset.py", line 17, in pil_loader                                                                                                                                  
    with open(path, 'rb') as f:                                                                                                                                                                                       
FileNotFoundError: [Errno 2] No such file or directory: '/mnt/dad/hungvm/DAD/Tester2/normal_driving_4/front_IR/img_19872.png'                                                                                         
/mnt/dad/hungvm/DAD/Tester2/normal_driving_4/front_IR/img_19872.png                                                                                                                                                   
Traceback (most recent call last):                                                                                                                                                                                    
  File "/mnt/dad/hungvm/Driver-Anomaly-Detection/dataset.py", line 17, in pil_loader                                                                                                                                  
    with open(path, 'rb') as f:                                                                                                                                                                                       
FileNotFoundError: [Errno 2] No such file or directory: '/mnt/dad/hungvm/DAD/Tester25/normal_driving_2/front_IR/img_10080.png'                                                                                        
/mnt/dad/hungvm/DAD/Tester25/normal_driving_2/front_IR/img_10080.png                                                                                                                                                  
Traceback (most recent call last):                                                                                                                                                                                    
  File "/mnt/dad/hungvm/Driver-Anomaly-Detection/dataset.py", line 17, in pil_loader                                                                                                                                  
    with open(path, 'rb') as f:                                                      
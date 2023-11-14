```bash
cd /content/Driver-Anomaly-Detection
python3 run.py -m train -n experiment<number>
```

Train 1->8
Val 1->2
epoches 100
val_step 1
nthreads 4

# Experiment 2:

Default (SGD optimizer, NCE loss, n/a batch 10/140, lr 0.01)
Epoches 250

TRAIN_COMMAND = "python main.py \
 --root_path /content/DAD/ \
 --mode train \
 --view %s \
 --model_type resnet \
 --model_depth 18 \
 --shortcut_type A \
 --pre_train_model False \
 --n_train_batch_size 10 \
 --a_train_batch_size 140 \
 --val_batch_size 70 \
 --learning_rate 0.01 \
 --epochs 200 \
 --norm_value 255 \
 --cal_vec_batch_size 100 \
 --tau 0.1 \
 --manual_seed 26 \
 --memory_bank_size 200 \
 --resume_path '' \
 --resume_head_path '' \
 --val_step 1 \
 --save_step 50 \
 --train_crop 'random' \
 --n_scales 5 \
 --downsample 2 \
 --log_resume False \
 --width_mult 2.0 \
 --n_split_ratio 1.0 \
 --a_split_ratio 1.0 \
 --n_threads 4 \
 --name %s"
TEST_COMMAND = "python main.py --root_path /content/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 20 --cal_vec_batch_size 10 --n_threads 4 --name %s"

### Results:

**On Colab**
Mode: Top(D): Best Acc: 73.96 | Threshold: 0.64 | AUC: 0.6745
View: Top(D)(post-processed): Best Acc: 73.99 | Threshold: 0.64 | AUC: 0.6771

Mode: Top(IR): Best Acc: 80.67 | Threshold: 0.7 | AUC: 0.846
View: Top(IR)(post-processed): Best Acc: 80.88 | Threshold: 0.7 | AUC: 0.8491

Mode: Top(DIR): Best Acc: 81.66 | Threshold: 0.68 | AUC: 0.8423
View: Top(DIR)(post-processed): Best Acc: 81.85 | Threshold: 0.68 | AUC: 0.8456

Mode: Front(D): Best Acc: 71.48 | Threshold: 0.51 | AUC: 0.7327
View: Front(D)(post-processed): Best Acc: 71.51 | Threshold: 0.51 | AUC: 0.7344

Mode: Front(IR): Best Acc: 71.73 | Threshold: 0.63 | AUC: 0.7502
View: Front(IR)(post-processed): Best Acc: 71.92 | Threshold: 0.64 | AUC: 0.7541

Mode: Front(DIR): Best Acc: 74.32 | Threshold: 0.58 | AUC: 0.7887
View: Front(DIR)(post-processed): Best Acc: 74.44 | Threshold: 0.58 | AUC: 0.792

Mode: Fusion(D): Best Acc: 81.29 | Threshold: 0.59 | AUC: 0.8388
View: Fusion(D)(post-processed): Best Acc: 81.4 | Threshold: 0.59 | AUC: 0.8414

Mode: Fusion(IR): Best Acc: 78.75 | Threshold: 0.66 | AUC: 0.8684
View: Fusion(IR)(post-processed): Best Acc: 79.02 | Threshold: 0.66 | AUC: 0.8716

Mode: Fusion(DIR): Best Acc: 84.08 | Threshold: 0.62 | AUC: 0.9051
View: Fusion(DIR)(post-processed): Best Acc: 84.28 | Threshold: 0.62 | AUC: 0.9077

**250 epoches on colab**
get_fusion_label...
Mode: Top(D): Best Acc: 56.75 | Threshold: 0.51 | AUC: 0.3754
View: Top(D)(post-processed): Best Acc: 56.71 | Threshold: 0.51 | AUC: 0.374

Mode: Top(IR): Best Acc: 76.0 | Threshold: 0.67 | AUC: 0.7512
View: Top(IR)(post-processed): Best Acc: 76.2 | Threshold: 0.67 | AUC: 0.7569

Mode: Top(DIR): Best Acc: 71.86 | Threshold: 0.6 | AUC: 0.6737
View: Top(DIR)(post-processed): Best Acc: 71.98 | Threshold: 0.6 | AUC: 0.676

Mode: Front(D): Best Acc: 64.05 | Threshold: 0.41 | AUC: 0.6629
View: Front(D)(post-processed): Best Acc: 64.15 | Threshold: 0.41 | AUC: 0.6643

Mode: Front(IR): Best Acc: 58.8 | Threshold: 0.5 | AUC: 0.5979
View: Front(IR)(post-processed): Best Acc: 59.01 | Threshold: 0.5 | AUC: 0.6006

Mode: Front(DIR): Best Acc: 62.76 | Threshold: 0.45 | AUC: 0.6652
View: Front(DIR)(post-processed): Best Acc: 62.92 | Threshold: 0.45 | AUC: 0.6686

Mode: Fusion(D): Best Acc: 56.42 | Threshold: 0.47 | AUC: 0.5259
View: Fusion(D)(post-processed): Best Acc: 56.45 | Threshold: 0.47 | AUC: 0.5267

Mode: Fusion(IR): Best Acc: 72.74 | Threshold: 0.56 | AUC: 0.7727
View: Fusion(IR)(post-processed): Best Acc: 72.95 | Threshold: 0.56 | AUC: 0.7773

Mode: Fusion(DIR): Best Acc: 70.08 | Threshold: 0.53 | AUC: 0.7409
View: Fusion(DIR)(post-processed): Best Acc: 70.33 | Threshold: 0.53 | AUC: 0.7443

# Experiment 22:

SGD optimizer, n_threads 4, CENCE loss (beta0.5, eps 0.0), no ce label smoothing

TRAIN_COMMAND = "python main.py \
 --root_path /content/DAD/ \
 --mode train \
 --view %s \
 --model_type resnet \
 --model_depth 18 \
 --shortcut_type A \
 --pre_train_model False \
 --n_train_batch_size 10 \
 --a_train_batch_size 150 \
 --val_batch_size 70 \
 --learning_rate 0.01 \
 --epochs 100 \
 --norm_value 255 \
 --cal_vec_batch_size 100 \
 --tau 0.1 \
 --manual_seed 26 \
 --memory_bank_size 200 \
 --resume_path '' \
 --resume_head_path '' \
 --val_step 1 \
 --save_step 50 \
 --train_crop 'random' \
 --n_scales 5 \
 --downsample 2 \
 --log_resume False \
 --width_mult 2.0 \
 --n_split_ratio 1.0 \
 --a_split_ratio 1.0 \
 --n_threads 4 \
 --loss cence \
 --head two_heads_cence \
 --name %s"
TEST_COMMAND = "python main.py --root_path /content/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name %s"

### result

Mode: Top(D): Best Acc: 85.37 | Threshold: 0.96 | AUC: 0.9145
View: Top(D)(post-processed): Best Acc: 85.51 | Threshold: 0.96 | AUC: 0.916

Mode: Top(IR): Best Acc: 79.96 | Threshold: 0.92 | AUC: 0.8674
View: Top(IR)(post-processed): Best Acc: 80.15 | Threshold: 0.92 | AUC: 0.8703

Mode: Top(DIR): Best Acc: 84.66 | Threshold: 0.93 | AUC: 0.9127
View: Top(DIR)(post-processed): Best Acc: 84.82 | Threshold: 0.93 | AUC: 0.9145

Mode: Front(D): Best Acc: 74.04 | Threshold: 0.92 | AUC: 0.7478
View: Front(D)(post-processed): Best Acc: 74.12 | Threshold: 0.92 | AUC: 0.7491

Mode: Front(IR): Best Acc: 77.43 | Threshold: 0.81 | AUC: 0.8335
View: Front(IR)(post-processed): Best Acc: 77.6 | Threshold: 0.83 | AUC: 0.8361

Mode: Front(DIR): Best Acc: 79.17 | Threshold: 0.89 | AUC: 0.8437
View: Front(DIR)(post-processed): Best Acc: 79.37 | Threshold: 0.89 | AUC: 0.8459

Mode: Fusion(D): Best Acc: 86.65 | Threshold: 0.94 | AUC: 0.9207
View: Fusion(D)(post-processed): Best Acc: 86.76 | Threshold: 0.94 | AUC: 0.9222

Mode: Fusion(IR): Best Acc: 85.31 | Threshold: 0.87 | AUC: 0.9162
View: Fusion(IR)(post-processed): Best Acc: 85.46 | Threshold: 0.87 | AUC: 0.9185

Mode: Fusion(DIR): Best Acc: 88.34 | Threshold: 0.9 | AUC: 0.9407
View: Fusion(DIR)(post-processed): Best Acc: 88.48 | Threshold: 0.9 | AUC: 0.9424

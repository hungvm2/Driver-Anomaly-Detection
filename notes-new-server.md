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

Default (SGD optimizer, NCE loss, n/a batch 10/150, lr 0.01)
Epoches 100

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
 --name %s"
TEST_COMMAND = "python main.py --root_path /content/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name %s"

### Results:

**On Colab**
Mode: Top(D): Best Acc: 86.58 | Threshold: 0.91 | AUC: 0.92
View: Top(D)(post-processed): Best Acc: 86.75 | Threshold: 0.91 | AUC: 0.9219

Mode: Top(IR): Best Acc: 79.06 | Threshold: 0.83 | AUC: 0.8442
View: Top(IR)(post-processed): Best Acc: 79.18 | Threshold: 0.83 | AUC: 0.8463

Mode: Top(DIR): Best Acc: 85.14 | Threshold: 0.87 | AUC: 0.912
View: Top(DIR)(post-processed): Best Acc: 85.3 | Threshold: 0.87 | AUC: 0.9136

Mode: Front(D): Best Acc: 71.61 | Threshold: 0.98 | AUC: 0.7196
View: Front(D)(post-processed): Best Acc: 71.68 | Threshold: 0.98 | AUC: 0.721

Mode: Front(IR): Best Acc: 71.18 | Threshold: 0.86 | AUC: 0.7713
View: Front(IR)(post-processed): Best Acc: 71.36 | Threshold: 0.84 | AUC: 0.7741

Mode: Front(DIR): Best Acc: 71.93 | Threshold: 0.91 | AUC: 0.78
View: Front(DIR)(post-processed): Best Acc: 72.07 | Threshold: 0.91 | AUC: 0.7825

Mode: Fusion(D): Best Acc: 88.74 | Threshold: 0.94 | AUC: 0.9429
View: Fusion(D)(post-processed): Best Acc: 88.9 | Threshold: 0.94 | AUC: 0.9447

Mode: Fusion(IR): Best Acc: 80.03 | Threshold: 0.83 | AUC: 0.8638
View: Fusion(IR)(post-processed): Best Acc: 80.2 | Threshold: 0.83 | AUC: 0.8661

Mode: Fusion(DIR): Best Acc: 84.66 | Threshold: 0.87 | AUC: 0.9213
View: Fusion(DIR)(post-processed): Best Acc: 84.84 | Threshold: 0.88 | AUC: 0.9232

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

# Experiment 23:
SGD optimizer, CENCE loss (beta0.5, eps 0.1), ce label smoothing, n/a batch 10/150

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
Mode: Top(D):      Best Acc: 84.44 | Threshold: 0.9 | AUC: 0.9019
View: Top(D)(post-processed):       Best Acc: 84.53 | Threshold: 0.9 | AUC: 0.903 

Mode: Top(IR):      Best Acc: 76.13 | Threshold: 0.84 | AUC: 0.8237
View: Top(IR)(post-processed):       Best Acc: 76.36 | Threshold: 0.84 | AUC: 0.8273 

Mode: Top(DIR):      Best Acc: 83.6 | Threshold: 0.88 | AUC: 0.9005
View: Top(DIR)(post-processed):       Best Acc: 83.7 | Threshold: 0.88 | AUC: 0.9024 

Mode: Front(D):      Best Acc: 76.85 | Threshold: 0.9 | AUC: 0.82
View: Front(D)(post-processed):       Best Acc: 76.96 | Threshold: 0.9 | AUC: 0.8224 

Mode: Front(IR):      Best Acc: 69.97 | Threshold: 0.88 | AUC: 0.7612
View: Front(IR)(post-processed):       Best Acc: 70.18 | Threshold: 0.87 | AUC: 0.765 

Mode: Front(DIR):      Best Acc: 77.66 | Threshold: 0.88 | AUC: 0.8404
View: Front(DIR)(post-processed):       Best Acc: 77.8 | Threshold: 0.88 | AUC: 0.843 

Mode: Fusion(D):      Best Acc: 88.28 | Threshold: 0.88 | AUC: 0.94
View: Fusion(D)(post-processed):       Best Acc: 88.39 | Threshold: 0.88 | AUC: 0.9416 

Mode: Fusion(IR):      Best Acc: 79.66 | Threshold: 0.85 | AUC: 0.8638
View: Fusion(IR)(post-processed):       Best Acc: 79.88 | Threshold: 0.85 | AUC: 0.8673 

Mode: Fusion(DIR):      Best Acc: 88.19 | Threshold: 0.87 | AUC: 0.9388
View: Fusion(DIR)(post-processed):       Best Acc: 88.32 | Threshold: 0.87 | AUC: 0.9407 

# Experiment 24:
SGD optimizer, NCE loss, n/a batch 10/150, BasicCSP block in backbone

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
 --block basiccsp \
 --name %s"
TEST_COMMAND = "python main.py --root_path /content/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name %s"

### Result:
Mode: Top(D):      Best Acc: 86.36 | Threshold: 0.63 | AUC: 0.907
View: Top(D)(post-processed):       Best Acc: 86.5 | Threshold: 0.64 | AUC: 0.9095 

Mode: Top(IR):      Best Acc: 80.79 | Threshold: 0.98 | AUC: 0.8783
View: Top(IR)(post-processed):       Best Acc: 80.99 | Threshold: 0.98 | AUC: 0.8811 

Mode: Top(DIR):      Best Acc: 87.34 | Threshold: 0.81 | AUC: 0.9173
View: Top(DIR)(post-processed):       Best Acc: 87.5 | Threshold: 0.81 | AUC: 0.9194 

Mode: Front(D):      Best Acc: 69.78 | Threshold: 0.94 | AUC: 0.7415
View: Front(D)(post-processed):       Best Acc: 69.86 | Threshold: 0.94 | AUC: 0.7437 

Mode: Front(IR):      Best Acc: 70.13 | Threshold: 0.79 | AUC: 0.7373
View: Front(IR)(post-processed):       Best Acc: 70.36 | Threshold: 0.81 | AUC: 0.7405 

Mode: Front(DIR):      Best Acc: 71.44 | Threshold: 0.91 | AUC: 0.7733
View: Front(DIR)(post-processed):       Best Acc: 71.58 | Threshold: 0.91 | AUC: 0.7756 

Mode: Fusion(D):      Best Acc: 88.0 | Threshold: 0.81 | AUC: 0.9339
View: Fusion(D)(post-processed):       Best Acc: 88.16 | Threshold: 0.81 | AUC: 0.9358 

Mode: Fusion(IR):      Best Acc: 79.44 | Threshold: 0.93 | AUC: 0.8707
View: Fusion(IR)(post-processed):       Best Acc: 79.6 | Threshold: 0.93 | AUC: 0.873 

Mode: Fusion(DIR):      Best Acc: 87.02 | Threshold: 0.86 | AUC: 0.9337
View: Fusion(DIR)(post-processed):       Best Acc: 87.21 | Threshold: 0.86 | AUC: 0.9361 

Total testing time: 2109.534331560135

# Experiment 25:
SGD optimizer, n/a batch 10/150, BasicCSP block in backbone, CENCE loss (beta0.5, eps 0.0), no ce label smoothing,

Mode: Top(D):      Best Acc: 86.8 | Threshold: 0.93 | AUC: 0.9155
View: Top(D)(post-processed):       Best Acc: 87.02 | Threshold: 0.93 | AUC: 0.9184 

Mode: Top(IR):      Best Acc: 80.43 | Threshold: 0.95 | AUC: 0.8775
View: Top(IR)(post-processed):       Best Acc: 80.71 | Threshold: 0.95 | AUC: 0.881 

Mode: Top(DIR):      Best Acc: 87.67 | Threshold: 0.93 | AUC: 0.9247
View: Top(DIR)(post-processed):       Best Acc: 87.85 | Threshold: 0.93 | AUC: 0.927 

Mode: Front(D):      Best Acc: 72.22 | Threshold: 0.98 | AUC: 0.7367
View: Front(D)(post-processed):       Best Acc: 72.31 | Threshold: 0.98 | AUC: 0.7379 

Mode: Front(IR):      Best Acc: 73.21 | Threshold: 0.79 | AUC: 0.7873
View: Front(IR)(post-processed):       Best Acc: 73.41 | Threshold: 0.79 | AUC: 0.7898 

Mode: Front(DIR):      Best Acc: 73.56 | Threshold: 0.88 | AUC: 0.7951
View: Front(DIR)(post-processed):       Best Acc: 73.75 | Threshold: 0.89 | AUC: 0.7971 

Mode: Fusion(D):      Best Acc: 89.06 | Threshold: 0.95 | AUC: 0.9396
View: Fusion(D)(post-processed):       Best Acc: 89.23 | Threshold: 0.95 | AUC: 0.942 

Mode: Fusion(IR):      Best Acc: 80.35 | Threshold: 0.88 | AUC: 0.8813
View: Fusion(IR)(post-processed):       Best Acc: 80.52 | Threshold: 0.87 | AUC: 0.8839 

Mode: Fusion(DIR):      Best Acc: 86.24 | Threshold: 0.87 | AUC: 0.9383
View: Fusion(DIR)(post-processed):       Best Acc: 86.49 | Threshold: 0.87 | AUC: 0.9406 

Total testing time: 2111.0074281692505
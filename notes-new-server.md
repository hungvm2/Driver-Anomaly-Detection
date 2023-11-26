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

Mode: Top(D): Best Acc: 84.44 | Threshold: 0.9 | AUC: 0.9019
View: Top(D)(post-processed): Best Acc: 84.53 | Threshold: 0.9 | AUC: 0.903

Mode: Top(IR): Best Acc: 76.13 | Threshold: 0.84 | AUC: 0.8237
View: Top(IR)(post-processed): Best Acc: 76.36 | Threshold: 0.84 | AUC: 0.8273

Mode: Top(DIR): Best Acc: 83.6 | Threshold: 0.88 | AUC: 0.9005
View: Top(DIR)(post-processed): Best Acc: 83.7 | Threshold: 0.88 | AUC: 0.9024

Mode: Front(D): Best Acc: 76.85 | Threshold: 0.9 | AUC: 0.82
View: Front(D)(post-processed): Best Acc: 76.96 | Threshold: 0.9 | AUC: 0.8224

Mode: Front(IR): Best Acc: 69.97 | Threshold: 0.88 | AUC: 0.7612
View: Front(IR)(post-processed): Best Acc: 70.18 | Threshold: 0.87 | AUC: 0.765

Mode: Front(DIR): Best Acc: 77.66 | Threshold: 0.88 | AUC: 0.8404
View: Front(DIR)(post-processed): Best Acc: 77.8 | Threshold: 0.88 | AUC: 0.843

Mode: Fusion(D): Best Acc: 88.28 | Threshold: 0.88 | AUC: 0.94
View: Fusion(D)(post-processed): Best Acc: 88.39 | Threshold: 0.88 | AUC: 0.9416

Mode: Fusion(IR): Best Acc: 79.66 | Threshold: 0.85 | AUC: 0.8638
View: Fusion(IR)(post-processed): Best Acc: 79.88 | Threshold: 0.85 | AUC: 0.8673

Mode: Fusion(DIR): Best Acc: 88.19 | Threshold: 0.87 | AUC: 0.9388
View: Fusion(DIR)(post-processed): Best Acc: 88.32 | Threshold: 0.87 | AUC: 0.9407

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
TEST_COMMAND = "python main.py --root_path /content/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --block basiccsp --name %s"

### Result:

Mode: Top(D): Best Acc: 86.36 | Threshold: 0.63 | AUC: 0.907
View: Top(D)(post-processed): Best Acc: 86.5 | Threshold: 0.64 | AUC: 0.9095

Mode: Top(IR): Best Acc: 80.79 | Threshold: 0.98 | AUC: 0.8783
View: Top(IR)(post-processed): Best Acc: 80.99 | Threshold: 0.98 | AUC: 0.8811

Mode: Top(DIR): Best Acc: 87.34 | Threshold: 0.81 | AUC: 0.9173
View: Top(DIR)(post-processed): Best Acc: 87.5 | Threshold: 0.81 | AUC: 0.9194

Mode: Front(D): Best Acc: 69.78 | Threshold: 0.94 | AUC: 0.7415
View: Front(D)(post-processed): Best Acc: 69.86 | Threshold: 0.94 | AUC: 0.7437

Mode: Front(IR): Best Acc: 70.13 | Threshold: 0.79 | AUC: 0.7373
View: Front(IR)(post-processed): Best Acc: 70.36 | Threshold: 0.81 | AUC: 0.7405

Mode: Front(DIR): Best Acc: 71.44 | Threshold: 0.91 | AUC: 0.7733
View: Front(DIR)(post-processed): Best Acc: 71.58 | Threshold: 0.91 | AUC: 0.7756

Mode: Fusion(D): Best Acc: 88.0 | Threshold: 0.81 | AUC: 0.9339
View: Fusion(D)(post-processed): Best Acc: 88.16 | Threshold: 0.81 | AUC: 0.9358

Mode: Fusion(IR): Best Acc: 79.44 | Threshold: 0.93 | AUC: 0.8707
View: Fusion(IR)(post-processed): Best Acc: 79.6 | Threshold: 0.93 | AUC: 0.873

Mode: Fusion(DIR): Best Acc: 87.02 | Threshold: 0.86 | AUC: 0.9337
View: Fusion(DIR)(post-processed): Best Acc: 87.21 | Threshold: 0.86 | AUC: 0.9361

Total testing time: 2109.534331560135

# Experiment 25:

SGD optimizer, n/a batch 10/150, BasicCSP block in backbone, CENCE loss (beta0.5, eps 0.0), no ce label smoothing,

Mode: Top(D): Best Acc: 86.8 | Threshold: 0.93 | AUC: 0.9155
View: Top(D)(post-processed): Best Acc: 87.02 | Threshold: 0.93 | AUC: 0.9184

Mode: Top(IR): Best Acc: 80.43 | Threshold: 0.95 | AUC: 0.8775
View: Top(IR)(post-processed): Best Acc: 80.71 | Threshold: 0.95 | AUC: 0.881

Mode: Top(DIR): Best Acc: 87.67 | Threshold: 0.93 | AUC: 0.9247
View: Top(DIR)(post-processed): Best Acc: 87.85 | Threshold: 0.93 | AUC: 0.927

Mode: Front(D): Best Acc: 72.22 | Threshold: 0.98 | AUC: 0.7367
View: Front(D)(post-processed): Best Acc: 72.31 | Threshold: 0.98 | AUC: 0.7379

Mode: Front(IR): Best Acc: 73.21 | Threshold: 0.79 | AUC: 0.7873
View: Front(IR)(post-processed): Best Acc: 73.41 | Threshold: 0.79 | AUC: 0.7898

Mode: Front(DIR): Best Acc: 73.56 | Threshold: 0.88 | AUC: 0.7951
View: Front(DIR)(post-processed): Best Acc: 73.75 | Threshold: 0.89 | AUC: 0.7971

Mode: Fusion(D): Best Acc: 89.06 | Threshold: 0.95 | AUC: 0.9396
View: Fusion(D)(post-processed): Best Acc: 89.23 | Threshold: 0.95 | AUC: 0.942

Mode: Fusion(IR): Best Acc: 80.35 | Threshold: 0.88 | AUC: 0.8813
View: Fusion(IR)(post-processed): Best Acc: 80.52 | Threshold: 0.87 | AUC: 0.8839

Mode: Fusion(DIR): Best Acc: 86.24 | Threshold: 0.87 | AUC: 0.9383
View: Fusion(DIR)(post-processed): Best Acc: 86.49 | Threshold: 0.87 | AUC: 0.9406

Total testing time: 2111.0074281692505

# Experiment 26:

SGD optimizer, n_threads 4, CENCE loss (beta0.4, eps 0.0), no ce label smoothing

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
 --beta 0.4 \
 --name %s"
TEST_COMMAND = "python main.py --root_path /content/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name %s"

### result

Mode: Top(D): Best Acc: 84.72 | Threshold: 0.93 | AUC: 0.8989
View: Top(D)(post-processed): Best Acc: 84.81 | Threshold: 0.93 | AUC: 0.9004

Mode: Top(IR): Best Acc: 80.59 | Threshold: 0.87 | AUC: 0.8707
View: Top(IR)(post-processed): Best Acc: 80.8 | Threshold: 0.87 | AUC: 0.8731

Mode: Top(DIR): Best Acc: 85.74 | Threshold: 0.9 | AUC: 0.9125
View: Top(DIR)(post-processed): Best Acc: 85.9 | Threshold: 0.9 | AUC: 0.9139

Mode: Front(D): Best Acc: 74.84 | Threshold: 0.69 | AUC: 0.8042
View: Front(D)(post-processed): Best Acc: 74.92 | Threshold: 0.69 | AUC: 0.806

Mode: Front(IR): Best Acc: 73.98 | Threshold: 0.78 | AUC: 0.8055
View: Front(IR)(post-processed): Best Acc: 74.28 | Threshold: 0.78 | AUC: 0.8082

Mode: Front(DIR): Best Acc: 76.33 | Threshold: 0.77 | AUC: 0.8299
View: Front(DIR)(post-processed): Best Acc: 76.64 | Threshold: 0.75 | AUC: 0.8327

Mode: Fusion(D): Best Acc: 87.3 | Threshold: 0.8 | AUC: 0.9141
View: Fusion(D)(post-processed): Best Acc: 87.37 | Threshold: 0.8 | AUC: 0.9157

Mode: Fusion(IR): Best Acc: 80.5 | Threshold: 0.87 | AUC: 0.8863
View: Fusion(IR)(post-processed): Best Acc: 80.77 | Threshold: 0.86 | AUC: 0.889

Mode: Fusion(DIR): Best Acc: 85.6 | Threshold: 0.82 | AUC: 0.922
View: Fusion(DIR)(post-processed): Best Acc: 85.86 | Threshold: 0.82 | AUC: 0.924

Total testing time: 1997.8584575653076

# Experiment 27:

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
 --beta 0.6 \
 --name %s"
TEST_COMMAND = "python main.py --root_path /content/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name %s"

### Result:

Mode: Top(D): Best Acc: 82.95 | Threshold: 0.9 | AUC: 0.8882
View: Top(D)(post-processed): Best Acc: 83.08 | Threshold: 0.9 | AUC: 0.8894

Mode: Top(IR): Best Acc: 79.1 | Threshold: 0.75 | AUC: 0.8396
View: Top(IR)(post-processed): Best Acc: 79.22 | Threshold: 0.75 | AUC: 0.8424

Mode: Top(DIR): Best Acc: 84.08 | Threshold: 0.83 | AUC: 0.8901
View: Top(DIR)(post-processed): Best Acc: 84.23 | Threshold: 0.83 | AUC: 0.8919

Mode: Front(D): Best Acc: 77.16 | Threshold: 0.79 | AUC: 0.8066
View: Front(D)(post-processed): Best Acc: 77.22 | Threshold: 0.79 | AUC: 0.8083

Mode: Front(IR): Best Acc: 71.63 | Threshold: 0.86 | AUC: 0.7709
View: Front(IR)(post-processed): Best Acc: 71.84 | Threshold: 0.86 | AUC: 0.7742

Mode: Front(DIR): Best Acc: 77.17 | Threshold: 0.82 | AUC: 0.8238
View: Front(DIR)(post-processed): Best Acc: 77.26 | Threshold: 0.82 | AUC: 0.8264

Mode: Fusion(D): Best Acc: 87.46 | Threshold: 0.84 | AUC: 0.9281
View: Fusion(D)(post-processed): Best Acc: 87.54 | Threshold: 0.84 | AUC: 0.9298

Mode: Fusion(IR): Best Acc: 80.92 | Threshold: 0.85 | AUC: 0.8609
View: Fusion(IR)(post-processed): Best Acc: 81.09 | Threshold: 0.85 | AUC: 0.8639

Mode: Fusion(DIR): Best Acc: 85.75 | Threshold: 0.84 | AUC: 0.9282
View: Fusion(DIR)(post-processed): Best Acc: 85.92 | Threshold: 0.84 | AUC: 0.9303

Total testing time: 1957.3686594963074

# Experiment 28:

SGD optimizer, CENCE loss (beta0.5, eps 0.2), ce label smoothing, n/a batch 10/150

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

Mode: Top(D): Best Acc: 84.18 | Threshold: 0.98 | AUC: 0.906'-
'View: Top(D)(post-processed): Best Acc: 84.26 | Threshold: 0.98 | AUC: 0.9076
'-
'Mode: Top(IR): Best Acc: 79.5 | Threshold: 0.81 | AUC: 0.8377'-
'View: Top(IR)(post-processed): Best Acc: 79.69 | Threshold: 0.81 | AUC: 0.8403
'-
'Mode: Top(DIR): Best Acc: 82.96 | Threshold: 0.89 | AUC: 0.8854'-
'View: Top(DIR)(post-processed): Best Acc: 83.17 | Threshold: 0.89 | AUC: 0.8877
'-
'Mode: Front(D): Best Acc: 72.73 | Threshold: 0.62 | AUC: 0.7926'-
'View: Front(D)(post-processed): Best Acc: 72.79 | Threshold: 0.65 | AUC: 0.7937
'-
'Mode: Front(IR): Best Acc: 74.28 | Threshold: 0.67 | AUC: 0.8092'-
'View: Front(IR)(post-processed): Best Acc: 74.6 | Threshold: 0.67 | AUC: 0.8127
'-
'Mode: Front(DIR): Best Acc: 76.3 | Threshold: 0.71 | AUC: 0.8339'-
'View: Front(DIR)(post-processed): Best Acc: 76.45 | Threshold: 0.71 | AUC: 0.8357
'-
'Mode: Fusion(D): Best Acc: 79.52 | Threshold: 0.8 | AUC: 0.8759'-
'View: Fusion(D)(post-processed): Best Acc: 79.61 | Threshold: 0.8 | AUC: 0.8773
'-
'Mode: Fusion(IR): Best Acc: 81.69 | Threshold: 0.77 | AUC: 0.8849'-
'View: Fusion(IR)(post-processed): Best Acc: 81.9 | Threshold: 0.77 | AUC: 0.8875
'-
'Mode: Fusion(DIR): Best Acc: 84.71 | Threshold: 0.8 | AUC: 0.9137'-
'View: Fusion(DIR)(post-processed): Best Acc: 84.81 | Threshold: 0.79 | AUC: 0.9154
'-
'Total testing time: 2006.791749238968'-

# Experiment 29:

SGD optimizer, CENCE loss (beta0.5, eps 0.05), ce label smoothing, n/a batch 10/150

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

Mode: Top(D): Best Acc: 83.1 | Threshold: 0.95 | AUC: 0.8876
View: Top(D)(post-processed): Best Acc: 83.24 | Threshold: 0.95 | AUC: 0.8892

Mode: Top(IR): Best Acc: 79.99 | Threshold: 0.91 | AUC: 0.8653
View: Top(IR)(post-processed): Best Acc: 80.17 | Threshold: 0.91 | AUC: 0.8678

Mode: Top(DIR): Best Acc: 83.95 | Threshold: 0.92 | AUC: 0.8982
View: Top(DIR)(post-processed): Best Acc: 84.09 | Threshold: 0.92 | AUC: 0.8999

Mode: Front(D): Best Acc: 66.68 | Threshold: 0.96 | AUC: 0.6742
View: Front(D)(post-processed): Best Acc: 66.68 | Threshold: 0.96 | AUC: 0.6758

Mode: Front(IR): Best Acc: 73.58 | Threshold: 0.55 | AUC: 0.7831
View: Front(IR)(post-processed): Best Acc: 73.69 | Threshold: 0.57 | AUC: 0.7855

Mode: Front(DIR): Best Acc: 74.01 | Threshold: 0.76 | AUC: 0.7871
View: Front(DIR)(post-processed): Best Acc: 74.09 | Threshold: 0.77 | AUC: 0.7893

Mode: Fusion(D): Best Acc: 84.39 | Threshold: 0.97 | AUC: 0.8904
View: Fusion(D)(post-processed): Best Acc: 84.48 | Threshold: 0.97 | AUC: 0.8922

Mode: Fusion(IR): Best Acc: 79.18 | Threshold: 0.73 | AUC: 0.861
View: Fusion(IR)(post-processed): Best Acc: 79.33 | Threshold: 0.73 | AUC: 0.8633

Mode: Fusion(DIR): Best Acc: 84.52 | Threshold: 0.84 | AUC: 0.9002
View: Fusion(DIR)(post-processed): Best Acc: 84.66 | Threshold: 0.84 | AUC: 0.9023

Total testing time: 2039.2392091751099

# Experiment 30:

SGD optimizer, CENCE loss (beta0.9, eps 0.0), no ce label smoothing, n/a batch 10/150
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
 --beta 0.9 \
 --name %s"
TEST_COMMAND = "python main.py --root_path /content/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name %s"

### Result:

View: Top(D)(post-processed): Best Acc: 83.62 | Threshold: 0.83 | AUC: 0.8913

Mode: Top(IR): Best Acc: 81.46 | Threshold: 0.95 | AUC: 0.8891
View: Top(IR)(post-processed): Best Acc: 81.62 | Threshold: 0.95 | AUC: 0.8911

Mode: Top(DIR): Best Acc: 84.83 | Threshold: 0.87 | AUC: 0.9106
View: Top(DIR)(post-processed): Best Acc: 84.96 | Threshold: 0.87 | AUC: 0.912

Mode: Front(D): Best Acc: 73.28 | Threshold: 0.57 | AUC: 0.7204
View: Front(D)(post-processed): Best Acc: 73.34 | Threshold: 0.57 | AUC: 0.7218

Mode: Front(IR): Best Acc: 70.26 | Threshold: 0.61 | AUC: 0.7686
View: Front(IR)(post-processed): Best Acc: 70.48 | Threshold: 0.61 | AUC: 0.7724

Mode: Front(DIR): Best Acc: 74.16 | Threshold: 0.59 | AUC: 0.7754
View: Front(DIR)(post-processed): Best Acc: 74.27 | Threshold: 0.59 | AUC: 0.778

Mode: Fusion(D): Best Acc: 84.14 | Threshold: 0.72 | AUC: 0.8804
View: Fusion(D)(post-processed): Best Acc: 84.3 | Threshold: 0.72 | AUC: 0.8826

Mode: Fusion(IR): Best Acc: 79.36 | Threshold: 0.75 | AUC: 0.8605
View: Fusion(IR)(post-processed): Best Acc: 79.54 | Threshold: 0.75 | AUC: 0.8636

Mode: Fusion(DIR): Best Acc: 85.17 | Threshold: 0.74 | AUC: 0.8965
View: Fusion(DIR)(post-processed): Best Acc: 85.29 | Threshold: 0.74 | AUC: 0.8989

Total testing time: 1975.0673003196716

# Experiment 31:

SGD optimizer, NCE loss, n/a batch 10/150, BasicCSP block in backbone, (c type: transition first)

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
 --t_type c \
 --name %s"
TEST_COMMAND = "python main.py --root_path /content/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --block basiccsp --t_type c --name %s"

### results:
Mode: Top(D):      Best Acc: 86.49 | Threshold: 0.97 | AUC: 0.9179
View: Top(D)(post-processed):       Best Acc: 86.8 | Threshold: 0.97 | AUC: 0.9214 

Mode: Top(IR):      Best Acc: 78.14 | Threshold: 0.98 | AUC: 0.8447
View: Top(IR)(post-processed):       Best Acc: 78.31 | Threshold: 0.98 | AUC: 0.849 

Mode: Top(DIR):      Best Acc: 84.28 | Threshold: 0.97 | AUC: 0.9188
View: Top(DIR)(post-processed):       Best Acc: 84.41 | Threshold: 0.97 | AUC: 0.9215 

Mode: Front(D):      Best Acc: 72.34 | Threshold: 0.93 | AUC: 0.7038
View: Front(D)(post-processed):       Best Acc: 72.47 | Threshold: 0.93 | AUC: 0.7056 

Mode: Front(IR):      Best Acc: 70.73 | Threshold: 0.3 | AUC: 0.7589
View: Front(IR)(post-processed):       Best Acc: 70.85 | Threshold: 0.3 | AUC: 0.7625 

Mode: Front(DIR):      Best Acc: 72.11 | Threshold: 0.63 | AUC: 0.7759
View: Front(DIR)(post-processed):       Best Acc: 72.26 | Threshold: 0.63 | AUC: 0.7794 

Mode: Fusion(D):      Best Acc: 87.13 | Threshold: 0.95 | AUC: 0.9052
View: Fusion(D)(post-processed):       Best Acc: 87.33 | Threshold: 0.95 | AUC: 0.9086 

Mode: Fusion(IR):      Best Acc: 77.38 | Threshold: 0.61 | AUC: 0.8373
View: Fusion(IR)(post-processed):       Best Acc: 77.53 | Threshold: 0.61 | AUC: 0.841 

Mode: Fusion(DIR):      Best Acc: 85.82 | Threshold: 0.78 | AUC: 0.9091
View: Fusion(DIR)(post-processed):       Best Acc: 86.0 | Threshold: 0.79 | AUC: 0.9125 

Total testing time: 2044.8548233509064


# Experiment 32:

SGD optimizer, NCE loss, n/a batch 10/150, BasicCSP block in backbone, (d type: transition last)

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
 --t_type d \
 --name %s"
TEST_COMMAND = "python main.py --root_path /content/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --block basiccsp --t_type d --name %s"

## Result:
Mode: Top(D):      Best Acc: 85.96 | Threshold: 0.96 | AUC: 0.9077
View: Top(D)(post-processed):       Best Acc: 86.22 | Threshold: 0.96 | AUC: 0.9115 

Mode: Top(IR):      Best Acc: 81.35 | Threshold: 0.96 | AUC: 0.8657
View: Top(IR)(post-processed):       Best Acc: 81.57 | Threshold: 0.96 | AUC: 0.8698 

Mode: Top(DIR):      Best Acc: 85.52 | Threshold: 0.95 | AUC: 0.9201
View: Top(DIR)(post-processed):       Best Acc: 85.68 | Threshold: 0.95 | AUC: 0.9231 

Mode: Front(D):      Best Acc: 75.36 | Threshold: 0.24 | AUC: 0.7656
View: Front(D)(post-processed):       Best Acc: 75.36 | Threshold: 0.24 | AUC: 0.7658 

Mode: Front(IR):      Best Acc: 71.93 | Threshold: 0.64 | AUC: 0.7538
View: Front(IR)(post-processed):       Best Acc: 72.04 | Threshold: 0.64 | AUC: 0.7583 

Mode: Front(DIR):      Best Acc: 72.63 | Threshold: 0.48 | AUC: 0.7787
View: Front(DIR)(post-processed):       Best Acc: 72.81 | Threshold: 0.48 | AUC: 0.781 

Mode: Fusion(D):      Best Acc: 85.64 | Threshold: 0.58 | AUC: 0.8729
View: Fusion(D)(post-processed):       Best Acc: 85.71 | Threshold: 0.58 | AUC: 0.8737 

Mode: Fusion(IR):      Best Acc: 78.81 | Threshold: 0.75 | AUC: 0.8365
View: Fusion(IR)(post-processed):       Best Acc: 79.01 | Threshold: 0.76 | AUC: 0.8402 

Mode: Fusion(DIR):      Best Acc: 83.26 | Threshold: 0.67 | AUC: 0.8873
View: Fusion(DIR)(post-processed):       Best Acc: 83.43 | Threshold: 0.69 | AUC: 0.8894 

Total testing time: 2147.911495447159
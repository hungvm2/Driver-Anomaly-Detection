# Demo:

**=> DONE**

```bash
conda activate thesis

cd /mnt/Data/MasterofDataScience/Thesis/Driver-Anomaly-Detection

python3 demo_live.py
```

# Train:

- Remove redundant files:

```bash
find . -name '*._*' -delete`
```

- Training from scratch: **=> DONE**

```
python main.py \
  --root_path /mnt/Data/MasterofDataScience/Thesis/Driver-Anomaly-Detection/DAD/ \
  --mode train \
  --view top_depth \
  --model_type resnet \
  --model_depth 18 \
  --shortcut_type A \
  --pre_train_model False \
  --n_train_batch_size 5 \
  --a_train_batch_size 25 \
  --val_batch_size 25\
  --learning_rate 0.01 \
  --epochs 1 \
  --cal_vec_batch_size 100 \
  --tau 0.1 \
  --train_crop 'random' \
  --n_scales 5 \
  --downsample 2 \
  --n_split_ratio 1.0 \
  --a_split_ratio 1.0 \
  --save_step 1 \
  --val_step 1
```

- Resuming training from a checkpoint: (the resumed models consist of a base encoder model and a
  projection head model)
  **=> DONE**

```bash
python main.py \
  --root_path /mnt/Data/MasterofDataScience/Thesis/Driver-Anomaly-Detection/DAD/ \
  --mode train \
  --view top_depth \
  --model_type resnet \
  --model_depth 18 \
  --shortcut_type A \
  --pre_train_model False \
  --n_train_batch_size 5 \
  --a_train_batch_size 25 \
  --val_batch_size 25\
  --learning_rate 0.01 \
  --epochs 1 \
  --cal_vec_batch_size 100 \
  --tau 0.1 \
  --resume_path 'best_model_resnet_top_depth.pth' \
  --resume_head_path 'best_model_resnet_top_depth_head.pth' \
  --train_crop 'random' \
  --n_scales 5 \
  --downsample 2 \
  --n_split_ratio 1.0 \
  --a_split_ratio 1.0 \
  --save_step 1 \
  --val_step 1
```

- Training from a pretrained model. Find the corredponding model type in models.py and set the '
  pre_model_path' as the path of the pretrained model. Then set '--pre_train_model True ':
  Need to find the pre-trained weights first (trained with 3-channel imgs.)
  In model.py file:

```
pre_model_path = './premodels/kinetics_resnet_18_RGB_16_best.pth'
```

```
python main.py \
  --root_path /mnt/Data/MasterofDataScience/Thesis/Driver-Anomaly-Detection/DAD/ \
  --mode train \
  --view top_depth \
  --model_type resnet \
  --model_depth 18 \
  --shortcut_type A \
  --pre_train_model True \
  --n_train_batch_size 5 \
  --a_train_batch_size 25 \
  --val_batch_size 25\
  --learning_rate 0.01 \
  --epochs 1 \
  --cal_vec_batch_size 100 \
  --tau 0.1 \
  --train_crop 'random' \
  --n_scales 5 \
  --downsample 2 \
  --n_split_ratio 1.0 \
  --a_split_ratio 1.0 \
  --save_step 1 \
  --val_step 1
```

# Test

Config `resume_path_front_d`, `resume_path_front_ir`, `resume_path_top_d`, `resume_path_top_ir`
paths.

```bash
python main.py \
  --root_path /mnt/Data/MasterofDataScience/Thesis/Driver-Anomaly-Detection/DAD/ \
  --mode test \
  --model_type resnet \
  --model_depth 18 \
  --shortcut_type A \
  --val_batch_size 25\
  --cal_vec_batch_size 20
```
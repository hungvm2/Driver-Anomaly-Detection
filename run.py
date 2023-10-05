import os

COMMAND = "python main.py --root_path /home/username/DAD/ --mode train --view %s --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32  --a_train_batch_size 32  --val_batch_size 70  --learning_rate 0.01  --epochs 250  --cal_vec_batch_size 100  --tau 0.1  --train_crop 'random'  --n_scales 5  --downsample 2  --n_split_ratio 1.0  --a_split_ratio 1.0  --save_step 10  --val_step 10 --n_threads 4 --name experiment12 --loss cence --head two_heads_cence"
# COMMAND = "python main.py   --root_path /home/username/DAD/   --mode train   --view  %s   --model_type resnet   --model_depth 18   --shortcut_type A   --pre_train_model False   --n_train_batch_size 10   --a_train_batch_size 150   --val_batch_size 70  --learning_rate 0.01   --epochs 250   --cal_vec_batch_size 100   --tau 0.1   --train_crop 'random'   --n_scales 5   --downsample 2   --n_split_ratio 1.0   --a_split_ratio 1.0   --save_step 10   --val_step 10 --n_threads 4 --name nthreads4"

if __name__ == "__main__":
    datasets = ["front_IR", "front_depth", "top_depth", "top_IR"]
    for dataset in datasets:
        print(f"==== START DATASET: {dataset} ====")
        os.system(COMMAND % dataset)



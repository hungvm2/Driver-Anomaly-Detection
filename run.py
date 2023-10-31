import os
import argparse

TRAIN_COMMAND = "python main.py --root_path /mnt/data/hungvm/DAD/ --mode train --view %s --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False  --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name %s"
TEST_COMMAND = "python main.py --root_path /mnt/data/hungvm/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name %s"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run')
    parser.add_argument('-m', required=True, type=str, help='Running mode: train/test')
    parser.add_argument('-n', required=True, type=str, help='Experiment name')
    args = parser.parse_args()

    name = args.n
    if args.m == "train":
        datasets = ["front_IR", "front_depth", "top_depth", "top_IR"]
        for dataset in datasets:
            print(f"==== START DATASET: {dataset} - NAME: {name} ====")
            os.system(TRAIN_COMMAND % (dataset, name))
    else:
        print(f"==== START TESTING - NAME: {name} ====")
        os.system(TEST_COMMAND % name)


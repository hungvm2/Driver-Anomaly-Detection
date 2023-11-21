import argparse
import os
import time

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run')
    parser.add_argument('-n', required=True, type=str, help='Experiment name')
    parser.add_argument('-m', default="", type=str, help='Experiment name')
    parser.add_argument('-s', default=10, type=int, help='Sleeping time')
    args = parser.parse_args()

    name = args.n
    sleep_time = int(args.s)
    print("Sleeping time: ", sleep_time)
    datasets = [ "front_IR", "front_depth", "top_depth", "top_IR" ]
    if not args.m:
        for dataset in datasets:
            print(f"==== START DATASET: {dataset} - NAME: {name} ====")
            os.system(TRAIN_COMMAND % (dataset, name))
            time.sleep(sleep_time)
        print(f"==== START TESTING - NAME: {name} ====")
        os.system(TEST_COMMAND % name)
    elif args.m == "train":
        for dataset in datasets:
            print(f"==== START DATASET: {dataset} - NAME: {name} ====")
            os.system(TRAIN_COMMAND % (dataset, name))
            time.sleep(sleep_time)
    elif args.m == "test":
        print(f"==== START TESTING - NAME: {name} ====")
        os.system(TEST_COMMAND % name)

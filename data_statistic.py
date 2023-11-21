import os
from collections import defaultdict

if __name__ == "__main__":
    ROOT_DATA_FOLDER = "/Users/awlvn/hungvm/MoD/MoD_thesis/DAD"
    FPS = 45
    numb_of_test = 8
    numb_of_val = 2
    tester_dir_prefix = "Tester"
    val_dir_prefix = "val0"
    normal_state_prefix = "normal"
    testers = {tester_dir_prefix + str(i) for i in range(1, numb_of_test + 1)}
    val = {val_dir_prefix + str(i) for i in range(1, numb_of_val + 1)}
    states = defaultdict(lambda: 0)
    print(testers, val)
    total_tester_imgs = 0
    total_val_imgs = 0
    for dir_or_file in os.listdir(ROOT_DATA_FOLDER):
        if dir_or_file not in testers and dir_or_file not in val:
            continue
        if dir_or_file in testers:
            tester_path = os.path.join(ROOT_DATA_FOLDER, dir_or_file)
            print("tester_path: ", tester_path)
            for state_dir in os.listdir(tester_path):
                if state_dir[0] == ".":
                    continue
                state_path = os.path.join(tester_path, state_dir, "front_depth")
                numb_of_imgs = len(os.listdir(state_path))
                if normal_state_prefix in state_dir:
                    state_dir = normal_state_prefix
                states[state_dir] += numb_of_imgs
                total_tester_imgs += numb_of_imgs
        elif dir_or_file in val:
            val_path = os.path.join(ROOT_DATA_FOLDER, dir_or_file)
            for rec_dir in os.listdir(val_path):
                if rec_dir[0] == ".":
                    continue
                rec_path = os.path.join(val_path, rec_dir, "front_depth")
                numb_of_imgs = len(os.listdir(rec_path))
                total_val_imgs += numb_of_imgs
    print("Images by states: ", states)
    print("Total tester images: ", total_tester_imgs, ", minutes: ", total_tester_imgs / FPS / 60)
    print("Total val images: ", total_val_imgs, ", minutes: ", total_val_imgs / FPS / 60)

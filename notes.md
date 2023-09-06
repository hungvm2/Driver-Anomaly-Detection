```bash
cd ~/MoD_Thesis/Driver-Anomaly-Detection
conda activate dad
```

# Experiment1:
Default, n_threads 0
### Command: 
```
python main.py   --root_path /home/username/DAD/   --mode train   --view top_depth   --model_type resnet   --model_depth 18   --shortcut_type A   --pre_train_model False   --n_train_batch_size 10   --a_train_batch_size 150   --val_batch_size 70  --learning_rate 0.01   --epochs 250   --cal_vec_batch_size 100   --tau 0.1   --train_crop 'random'   --n_scales 5   --downsample 2   --n_split_ratio 1.0   --a_split_ratio 1.0   --save_step 10   --val_step 10 --n_threads 0 --name nthreads0
```

### Results:
Epoch: 250/250 | Accuracy: 0.8219105816151581 | Normal Acc: 0.9002128791910591 | Anormal Acc: 0.6693454309786131 | Threshold: 0.9                                                                                     
==========================================!!!Logging!!!==========================================                                                                                                                     
==========================================!!!Saving!!!========================================== 

Training Process is running: 250/250  | Batch: 50 | Loss: 0.6968151926994324 (0.7956859562911239) | Probs: 0.9885717034339905 (0.973745573385089)                                                                     
Training Process is running: 250/250  | Batch: 51 | Loss: 0.6957883238792419 (0.7937648479755108) | Probs: 0.9948939085006714 (0.9741522721373118)                                                                    
Training Process is running: 250/250  | Batch: 52 | Loss: 0.6968507766723633 (0.7919362805924326) | Probs: 0.9895426630973816 (0.9744426568724075)                                                                    
Training Process is running: 250/250  | Batch: 53 | Loss: 0.7089558839797974 (0.7903996065810874) | Probs: 0.9796726107597351 (0.974539507870321)                                                                     
Training Process is running: 250/250  | Batch: 54 | Loss: 0.7067698836326599 (0.7888790661638433) | Probs: 0.990074872970581 (0.974821969053962)                                                                      
Training Process is running: 250/250  | Batch: 55 | Loss: 0.7143720388412476 (0.7875485835330827) | Probs: 0.9932786822319031 (0.9751515532178539)                                                                    
Training Process is running: 250/250  | Batch: 56 | Loss: 0.6921696066856384 (0.7858752681497942) | Probs: 0.9950056672096252 (0.9754998710071832)                                                                    
Training Process is running: 250/250  | Batch: 57 | Loss: 0.8413665890693665 (0.7868320150622006) | Probs: 0.9888412952423096 (0.9757298955629612)

Training Process is running: 251/250  | Batch: 55 | Loss: 0.7435771822929382 (0.7383896761706897) | Probs: │
0.9734548926353455 (0.9822918953640121)                                                                    │
Training Process is running: 251/250  | Batch: 56 | Loss: 0.6972460746765137 (0.7376678586006165) | Probs: │
0.995873212814331 (0.9825301640912106)                                                                     │
Training Process is running: 251/250  | Batch: 57 | Loss: 0.3459683954715729 (0.7309144195811502) | Probs: │
0.999516487121582 (0.9828230317296653)                                                                     │
Total training time:  53467.22434306145


# Experiment 2:
Default, n_threads 4
### Command: 
```
python main.py   --root_path /home/username/DAD/   --mode train   --view top_depth   --model_type resnet   --model_depth 18   --shortcut_type A   --pre_train_model False   --n_train_batch_size 10   --a_train_batch_size 150   --val_batch_size 70  --learning_rate 0.01   --epochs 250   --cal_vec_batch_size 100   --tau 0.1   --train_crop 'random'   --n_scales 5   --downsample 2   --n_split_ratio 1.0   --a_split_ratio 1.0   --save_step 10   --val_step 10 --n_threads 4 --name nthreads4
```

### Results:
Epoch: 250/250 | Accuracy: 0.83694553127885 | Normal Acc: 0.9083954230973922 | Anormal Acc: 0.6977316915100453 | Threshold: 0.89
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  12538.629226922989

# Experiment 3:
Adam optimizer, n_threads 4
### Command: 
```
python main.py   --root_path /home/username/DAD/   --mode train   --view top_depth   --model_type resnet   --model_depth 18   --shortcut_type A   --pre_train_model False   --n_train_batch_size 10   --a_train_batch_size 150   --val_batch_size 70  --learning_rate 0.01   --epochs 250   --cal_vec_batch_size 100   --tau 0.1   --train_crop 'random'   --n_scales 5   --downsample 2   --n_split_ratio 1.0   --a_split_ratio 1.0   --save_step 10   --val_step 10 --n_threads 4 --name adam_nthreads4 --opt adam
```

### Results:
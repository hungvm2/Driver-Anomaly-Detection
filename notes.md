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

Epoch: 250/250 | Accuracy: 0.8219105816151581 | Normal Acc: 0.9002128791910591 | Anormal Acc:
0.6693454309786131 | Threshold:
0.9                                                                                     
==========================================!!!`
Logging!!!==========================================                                                                                                                     
==========================================!!!Saving!!!==========================================

Training Process is running: 250/250 | Batch: 50 | Loss: 0.6968151926994324 (0.7956859562911239) |
Probs: 0.9885717034339905 (
0.973745573385089)                                                                     
Training Process is running: 250/250 | Batch: 51 | Loss: 0.6957883238792419 (0.7937648479755108) |
Probs: 0.9948939085006714 (
0.9741522721373118)                                                                    
Training Process is running: 250/250 | Batch: 52 | Loss: 0.6968507766723633 (0.7919362805924326) |
Probs: 0.9895426630973816 (
0.9744426568724075)                                                                    
Training Process is running: 250/250 | Batch: 53 | Loss: 0.7089558839797974 (0.7903996065810874) |
Probs: 0.9796726107597351 (
0.974539507870321)                                                                     
Training Process is running: 250/250 | Batch: 54 | Loss: 0.7067698836326599 (0.7888790661638433) |
Probs: 0.990074872970581 (
0.974821969053962)                                                                      
Training Process is running: 250/250 | Batch: 55 | Loss: 0.7143720388412476 (0.7875485835330827) |
Probs: 0.9932786822319031 (
0.9751515532178539)                                                                    
Training Process is running: 250/250 | Batch: 56 | Loss: 0.6921696066856384 (0.7858752681497942) |
Probs: 0.9950056672096252 (
0.9754998710071832)                                                                    
Training Process is running: 250/250 | Batch: 57 | Loss: 0.8413665890693665 (0.7868320150622006) |
Probs: 0.9888412952423096 (0.9757298955629612)

Training Process is running: 251/250 | Batch: 55 | Loss: 0.7435771822929382 (0.7383896761706897) |
Probs: │
0.9734548926353455 (0.9822918953640121)
│
Training Process is running: 251/250 | Batch: 56 | Loss: 0.6972460746765137 (0.7376678586006165) |
Probs: │
0.995873212814331 (0.9825301640912106)
│
Training Process is running: 251/250 | Batch: 57 | Loss: 0.3459683954715729 (0.7309144195811502) |
Probs: │
0.999516487121582 (0.9828230317296653)
│
Total training time:  53467.22434306145

# Experiment 2:

Default, n_threads 4

### Command:

```
python main.py   --root_path /home/username/DAD/   --mode train   --view top_depth   --model_type resnet   --model_depth 18   --shortcut_type A   --pre_train_model False   --n_train_batch_size 10   --a_train_batch_size 150   --val_batch_size 70  --learning_rate 0.01   --epochs 250   --cal_vec_batch_size 100   --tau 0.1   --train_crop 'random'   --n_scales 5   --downsample 2   --n_split_ratio 1.0   --a_split_ratio 1.0   --save_step 10   --val_step 10 --n_threads 4 --name nthreads4
```

### Results:

Epoch: 250/250 | Accuracy: 0.83694553127885 | Normal Acc: 0.9083954230973922 | Anormal Acc:
0.6977316915100453 | Threshold: 0.89
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
#### round 1:
Epoch: 250/250 | Accuracy: 0.839759089110652 | Normal Acc: 0.9066657796700373 | Anormal Acc:
0.709397278029812 | Threshold: 0.88
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  12285.094248056412

#### round 2:
Training Process is running: 1/250  | Batch: 0 | Loss: 6.019641399383545 (6.019641399383545) | Probs: 0.006642041262239218 (0.006642041262239218)
Training Process is running: 1/250  | Batch: 1 | Loss: 6.171365261077881 (6.095503330230713) | Probs: 0.006678272038698196 (0.006660156650468707)
Training Process is running: 1/250  | Batch: 2 | Loss: 6.10604190826416 (6.099016189575195) | Probs: 0.006625032518059015 (0.006648448606332143)
Training Process is running: 1/250  | Batch: 3 | Loss: 6.084890365600586 (6.095484733581543) | Probs: 0.006624103989452124 (0.006642362452112138)
Training Process is running: 1/250  | Batch: 4 | Loss: 6.068761825561523 (6.090140151977539) | Probs: 0.006623690016567707 (0.006638627965003252)
Training Process is running: 1/250  | Batch: 5 | Loss: 6.056553363800049 (6.084542353947957) | Probs: 0.006623363588005304 (0.0066360839021702605)
Training Process is running: 1/250  | Batch: 6 | Loss: 6.047374248504639 (6.0792326245989114) | Probs: 0.006622840650379658 (0.006634192009057317)
Training Process is running: 1/250  | Batch: 7 | Loss: 6.040292739868164 (6.074365139007568) | Probs: 0.006622620392590761 (0.006632745556998998)
Training Process is running: 1/250  | Batch: 8 | Loss: 6.034710884094238 (6.069959110683865) | Probs: 0.0066232830286026 (0.006631694164954954)
Training Process is running: 1/250  | Batch: 9 | Loss: 6.030531406402588 (6.066016340255738) | Probs: 0.006622890010476112 (0.006630813749507069)

Training Process is running: 250/250  | Batch: 51 | Loss: 2.3309524059295654 (2.5836778856240787) | Probs: 0.2356434315443039 (0.3169891895869604)
Training Process is running: 250/250  | Batch: 52 | Loss: 2.562622308731079 (2.5832806105883614) | Probs: 0.19262075424194336 (0.3146426153351676)
Training Process is running: 250/250  | Batch: 53 | Loss: 4.226263999938965 (2.613706228909669) | Probs: 0.20373103022575378 (0.31258869709240067)
Training Process is running: 250/250  | Batch: 54 | Loss: 2.1144654750823975 (2.604629124294628) | Probs: 0.3153248429298401 (0.3126384451985359)
Training Process is running: 250/250  | Batch: 55 | Loss: 2.2610080242156982 (2.5984930332217897) | Probs: 0.48476937413215637 (0.3157122117866363)
Training Process is running: 250/250  | Batch: 56 | Loss: 2.487593650817871 (2.596547430021721) | Probs: 0.30304476618766785 (0.31548997589893507)
Training Process is running: 250/250  | Batch: 57 | Loss: 6.255130290985107 (2.6596264448659173) | Probs: 0.5275748372077942 (0.319146611438743)
==========================================!!!Evaluating!!!==========================================
================================================Evaluating================================================
Epoch: 250/250 | Accuracy: 0.843979425858355 | Normal Acc: 0.8818520489622139 | Anormal Acc: 0.7701879455605962 | Threshold: 0.9400000000000001
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  12304.389201164246

# Experiment 4:
Cross entropy eps 0.1
### command:
```
python main.py   --root_path /home/username/DAD/   --mode train   --view top_depth   --model_type resnet   --model_depth 18   --shortcut_type A   --pre_train_model False   --n_train_batch_size 10   --a_train_batch_size 150   --val_batch_size 70  --learning_rate 0.001   --epochs 250   --cal_vec_batch_size 100   --tau 0.1   --train_crop 'random'   --n_scales 5   --downsample 2   --n_split_ratio 1.0   --a_split_ratio 1.0   --save_step 10   --val_step 10 --n_threads 4 --name adam_nthreads4_ce --opt adam --loss ce --feature_dim 2
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

# Experiment 4:
Cross entropy eps 0.1, n/a_train_batch_size 32
### command:
```
python main.py   --root_path /home/username/DAD/   --mode train   --view top_depth   --model_type resnet   --model_depth 18   --shortcut_type A   --pre_train_model False   --n_train_batch_size 32   --a_train_batch_size 32   --val_batch_size 70  --learning_rate 0.001   --epochs 250   --cal_vec_batch_size 100   --tau 0.1   --train_crop 'random'   --n_scales 5   --downsample 2   --n_split_ratio 1.0   --a_split_ratio 1.0   --save_step 10   --val_step 10 --n_threads 4 --name adam_nthreads4_ce_na32 --opt adam --loss ce --feature_dim 2
```

### Results:
Training Process is running: 250/250  | Batch: 259 | Loss: 0.35904553532600403 (0.3608183489396022) | Probs: 0.8044255971908569 (0.8042767740212954)
Training Process is running: 250/250  | Batch: 260 | Loss: 0.35904595255851746 (0.36081155814887006) | Probs: 0.8044249415397644 (0.8042773417129371)
Training Process is running: 250/250  | Batch: 261 | Loss: 0.35904499888420105 (0.3608048155562568) | Probs: 0.8044264912605286 (0.8042779109860194)
Training Process is running: 250/250  | Batch: 262 | Loss: 0.35904455184936523 (0.3607981225383599) | Probs: 0.8044272661209106 (0.8042784788762661)
Training Process is running: 250/250  | Batch: 263 | Loss: 0.3590456247329712 (0.3607914842890971) | Probs: 0.8044254779815674 (0.804279035691059)
Training Process is running: 250/250  | Batch: 264 | Loss: 0.3590465784072876 (0.3607848997385997) | Probs: 0.8044238686561584 (0.80427958223055)
Training Process is running: 250/250  | Batch: 265 | Loss: 0.3590453565120697 (0.3607783601024097) | Probs: 0.8044258952140808 (0.8042801322793602)
Training Process is running: 250/250  | Batch: 266 | Loss: 0.359045147895813 (0.3607718686709243) | Probs: 0.8044263124465942 (0.8042806797706232)
Training Process is running: 250/250  | Batch: 267 | Loss: 0.35904461145401 (0.360765423681309) | Probs: 0.8044271469116211 (0.804281226289806)
Training Process is running: 250/250  | Batch: 268 | Loss: 0.35919591784477234 (0.3607603160379544) | Probs: 0.804188072681427 (0.804280923139988)
==========================================!!!Evaluating!!!==========================================
================================================Evaluating================================================
Epoch: 250/250 | Accuracy: 0.7906537125774827 | Normal Acc: 0.8984832357637041 | Anormal Acc: 0.5805573558003888 | Threshold: 0.8200000000000001
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  23711.698891878128

# Experiment 5:

Adam optimizer, n_threads 4, n/a_train_batch_size 32

### Command:

```
python main.py   --root_path /home/username/DAD/   --mode train   --view top_depth   --model_type resnet   --model_depth 18   --shortcut_type A   --pre_train_model False   --n_train_batch_size 32   --a_train_batch_size 32   --val_batch_size 70  --learning_rate 0.01   --epochs 250   --cal_vec_batch_size 100   --tau 0.1   --train_crop 'random'   --n_scales 5   --downsample 2   --n_split_ratio 1.0   --a_split_ratio 1.0   --save_step 10   --val_step 10 --n_threads 4 --name adam_nthreads4_na32 --opt adam
```

### Results:

```bash
cd ~/MoD_Thesis/Driver-Anomaly-Detection
conda activate dad
```

# Experiment1:

Default, n_threads 0

### Command:

```
python main.py --root_path /home/username/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 0 --name nthreads0
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

## Train:
### Command:

```
python main.py --root_path /home/username/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name nthreads4
python main.py --root_path /home/username/DAD/ --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name nthreads4
python main.py --root_path /home/username/DAD/ --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name nthreads4
python main.py --root_path /home/username/DAD/ --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name nthreads4
```

### Results:
*top_depth*
Training Process is running: 250/250  | Batch: 52 | Loss: 0.7049784660339355 (0.7572555766915375) | Probs: 0.988228976726532 (0.9822399627487615)
Training Process is running: 250/250  | Batch: 53 | Loss: 0.7168378233909607 (0.7565070997785639) | Probs: 0.9918341040611267 (0.9824176320323238)
Training Process is running: 250/250  | Batch: 54 | Loss: 0.7073952555656433 (0.7556141571565108) | Probs: 0.9852781891822815 (0.982469642162323)
Training Process is running: 250/250  | Batch: 55 | Loss: 0.6974807381629944 (0.7545760603887695) | Probs: 0.9956089854240417 (0.9827042732919965)
Training Process is running: 250/250  | Batch: 56 | Loss: 0.6989076137542725 (0.7535994209741291) | Probs: 0.9944750070571899 (0.9829107773931403)
Training Process is running: 250/250  | Batch: 57 | Loss: 1.157804250717163 (0.7605684697628021) | Probs: 0.9451361298561096 (0.9822594903666397)
==========================================!!!Evaluating!!!==========================================
================================================Evaluating================================================
Epoch: 250/250 | Accuracy: 0.8494746559985932 | Normal Acc: 0.8933608302288452 | Anormal Acc: 0.7639662994167207 | Threshold: 0.96
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  12662.759660482407

*front_depth*
Training Process is running: 250/250  | Batch: 51 | Loss: 1.0316704511642456 (1.1627649951439638) | Probs: 0.7458420991897583 (0.8118637530849531)
Training Process is running: 250/250  | Batch: 52 | Loss: 0.8232799172401428 (1.1563596163155898) | Probs: 0.9303492307662964 (0.8140993281355444)
Training Process is running: 250/250  | Batch: 53 | Loss: 0.9647115468978882 (1.1528105779930398) | Probs: 0.9210375547409058 (0.8160796656652733)
Training Process is running: 250/250  | Batch: 54 | Loss: 2.3986010551452637 (1.175461313941262) | Probs: 0.3231644928455353 (0.8071175716140053)
Training Process is running: 250/250  | Batch: 55 | Loss: 1.8611047267913818 (1.1877049463135856) | Probs: 0.7673401236534119 (0.8064072600432804)
Training Process is running: 250/250  | Batch: 56 | Loss: 0.7887557148933411 (1.1807058369904233) | Probs: 0.9443652629852295 (0.8088275758843673)
Training Process is running: 250/250  | Batch: 57 | Loss: 2.4358339309692383 (1.2023459765417823) | Probs: 0.7964515089988708 (0.8086141954208242)
==========================================!!!Evaluating!!!==========================================
================================================Evaluating================================================
Epoch: 250/250 | Accuracy: 0.8093374950542929 | Normal Acc: 0.920502927088877 | Anormal Acc: 0.5927414128321452 | Threshold: 0.41000000000000003
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  12465.272372722626

*front_IR*
Training Process is running: 250/250  | Batch: 51 | Loss: 0.898190438747406 (1.0735382919128125) | Probs: 0.8655473589897156 (0.8503426915177932)
Training Process is running: 250/250  | Batch: 52 | Loss: 0.7857805490493774 (1.0681089005380306) | Probs: 0.9705129265785217 (0.8526100544434674)
Training Process is running: 250/250  | Batch: 53 | Loss: 1.2144626379013062 (1.0708191549336468) | Probs: 0.6711331605911255 (0.8492493712239795)
Training Process is running: 250/250  | Batch: 54 | Loss: 0.8705462217330933 (1.067177828875455) | Probs: 0.8877233266830444 (0.8499488976868717)
Training Process is running: 250/250  | Batch: 55 | Loss: 1.6797977685928345 (1.0781174706561225) | Probs: 0.7784639596939087 (0.8486723809369973)
Training Process is running: 250/250  | Batch: 56 | Loss: 0.7544772624969482 (1.072439572267365) | Probs: 0.986762523651123 (0.8510950150197012)
Training Process is running: 250/250  | Batch: 57 | Loss: 2.600375175476074 (1.098783289564067) | Probs: 0.7399489879608154 (0.8491787042083412)
==========================================!!!Evaluating!!!==========================================
Epoch: 250/250 | Accuracy: 0.791005407306458 | Normal Acc: 0.8996141564662055 | Anormal Acc: 0.5793907971484121 | Threshold: 0.33
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time: 12867.891201734543

*top_IR*
Training Process is running: 250/250  | Batch: 50 | Loss: 0.7041268348693848 (0.765802335505392) | Probs: 0.9972270131111145 (0.9749286542920506)
Training Process is running: 250/250  | Batch: 51 | Loss: 0.7220402359962463 (0.7649607566686777) | Probs: 0.9789381623268127 (0.975005760215796)
Training Process is running: 250/250  | Batch: 52 | Loss: 0.705660879611969 (0.7638418910638342) | Probs: 0.993624746799469 (0.9753570618494501)
Training Process is running: 250/250  | Batch: 53 | Loss: 0.800632894039154 (0.7645232059337475) | Probs: 0.9875687956809998 (0.9755832050685529)
Training Process is running: 250/250  | Batch: 54 | Loss: 0.6977335810661316 (0.7633088491179726) | Probs: 0.9974101185798645 (0.9759800580414859)
Training Process is running: 250/250  | Batch: 55 | Loss: 0.7313422560691833 (0.7627380170992443) | Probs: 0.9959786534309387 (0.9763371758162975)
Training Process is running: 250/250  | Batch: 56 | Loss: 0.739230215549469 (0.7623255995281956) | Probs: 0.98378586769104 (0.9764678546211176)
Training Process is running: 250/250  | Batch: 57 | Loss: 0.807713508605957 (0.7631081496847087) | Probs: 0.9893768429756165 (0.9766904233858503)
==========================================!!!Evaluating!!!==========================================
Epoch: 250/250 | Accuracy: 0.7964127137644524 | Normal Acc: 0.875 | Anormal Acc: 0.6432922877511341 | Threshold: 0.73
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time: 13632.874663591385

## Test:
### Command: 
```bash
python main.py --root_path /home/username/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name nthreads4
```

### Results:
Mode: Top(D):      Best Acc: 86.45 | Threshold: 0.92 | AUC: 0.9057
View: Top(D)(post-processed):       Best Acc: 86.57 | Threshold: 0.92 | AUC: 0.9071 

Mode: Top(IR):      Best Acc: 82.1 | Threshold: 0.83 | AUC: 0.8651
View: Top(IR)(post-processed):       Best Acc: 82.2 | Threshold: 0.83 | AUC: 0.8672 

Mode: Top(DIR):      Best Acc: 85.33 | Threshold: 0.82 | AUC: 0.902
View: Top(DIR)(post-processed):       Best Acc: 85.43 | Threshold: 0.83 | AUC: 0.9034 

Mode: Front(D):      Best Acc: 85.82 | Threshold: 0.82 | AUC: 0.8981
View: Front(D)(post-processed):       Best Acc: 85.93 | Threshold: 0.82 | AUC: 0.9004 

Mode: Front(IR):      Best Acc: 80.29 | Threshold: 0.66 | AUC: 0.8265
View: Front(IR)(post-processed):       Best Acc: 80.4 | Threshold: 0.66 | AUC: 0.8298 

Mode: Front(DIR):      Best Acc: 85.7 | Threshold: 0.76 | AUC: 0.9011
View: Front(DIR)(post-processed):       Best Acc: 85.83 | Threshold: 0.76 | AUC: 0.9035 

Mode: Fusion(D):      Best Acc: 89.85 | Threshold: 0.8 | AUC: 0.9504
View: Fusion(D)(post-processed):       Best Acc: 89.95 | Threshold: 0.8 | AUC: 0.9522 

Mode: Fusion(IR):      Best Acc: 85.32 | Threshold: 0.76 | AUC: 0.9149
View: Fusion(IR)(post-processed):       Best Acc: 85.46 | Threshold: 0.76 | AUC: 0.9175 

Mode: Fusion(DIR):      Best Acc: 90.56 | Threshold: 0.79 | AUC: 0.9544
View: Fusion(DIR)(post-processed):       Best Acc: 90.66 | Threshold: 0.79 | AUC: 0.9562 

Total testing time: 3985.4153921604156

# Experiment 3:

Adam optimizer, n_threads 4, nce loss, n/a batch size 10/150

### Command:

```
python main.py --root_path /home/username/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name adam_nthreads4 --opt adam
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
python main.py --root_path /home/username/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 10 --a_train_batch_size 150 --val_batch_size 70  --learning_rate 0.001 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name adam_nthreads4_ce --opt adam --loss ce --feature_dim 2
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
python main.py --root_path /home/username/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.001 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name adam_nthreads4_ce_na32 --opt adam --loss ce --feature_dim 2
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
python main.py --root_path /home/username/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name adam_nthreads4_na32 --opt adam
python main.py --root_path /home/username/DAD/ --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name adam_nthreads4_na32 --opt adam
python main.py --root_path /home/username/DAD/ --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name adam_nthreads4_na32 --opt adam
python main.py --root_path /home/username/DAD/ --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name adam_nthreads4_na32 --opt adam
```

### Results:
**top_depth**

Training Process is running: 250/250  | Batch: 263 | Loss: 0.6817829608917236 (0.7308158551653227) | Probs: 0.9993310570716858 (0.9831317980406862)
Training Process is running: 250/250  | Batch: 264 | Loss: 0.6817736625671387 (0.7306307902875936) | Probs: 0.9993337988853455 (0.9831929376665152)
Training Process is running: 250/250  | Batch: 265 | Loss: 0.6863850355148315 (0.7304644528636359) | Probs: 0.9950204491615295 (0.9832374019954437)
Training Process is running: 250/250  | Batch: 266 | Loss: 0.6814977526664734 (0.7302810569827476) | Probs: 0.9992469549179077 (0.9832973628678126)
Training Process is running: 250/250  | Batch: 267 | Loss: 0.7623330950737 (0.7304006541398034) | Probs: 0.9975091814994812 (0.9833503920418113)
Training Process is running: 250/250  | Batch: 268 | Loss: 0.5606114268302917 (0.7297694674211807) | Probs: 0.9997305274009705 (0.9834112847383137)
==========================================!!!Evaluating!!!==========================================
================================================Evaluating================================================
Epoch: 250/250 | Accuracy: 0.8511012441201038 | Normal Acc: 0.917176689728579 | Anormal Acc: 0.7223590408295528 | Threshold: 0.85
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  23146.126896858215

**top_IR**
Training Process is running: 250/250  | Batch: 265 | Loss: 1.3968355655670166 (0.8584812209570318) | Probs: 0.49907952547073364 (0.9264569402413261)
Training Process is running: 250/250  | Batch: 266 | Loss: 0.7770047187805176 (0.8581760655181685) | Probs: 0.9909259080886841 (0.9266983970497431)
Training Process is running: 250/250  | Batch: 267 | Loss: 1.3816304206848145 (0.8601292534105813) | Probs: 0.5092896223068237 (0.9251409016215979)
Training Process is running: 250/250  | Batch: 268 | Loss: 0.6572629809379578 (0.8593751036987872) | Probs: 0.9995215535163879 (0.9254174096212068)
==========================================!!!Evaluating!!!==========================================
================================================Evaluating================================================
Epoch: 250/250 | Accuracy: 0.7678375170352134 | Normal Acc: 0.8385444385311336 | Anormal Acc: 0.6300712896953986 | Threshold: 0.59
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  23652.94761633873


**front_IR**
Training Process is running: 250/250  | Batch: 262 | Loss: 0.8326717615127563 (1.3251393052108387) | Probs: 0.9604284167289734 (0.7382381013364393)
Training Process is running: 250/250  | Batch: 263 | Loss: 1.3533555269241333 (1.3252461848385406) | Probs: 0.8396589756011963 (0.7386222713147149)
Training Process is running: 250/250  | Batch: 264 | Loss: 0.8576209545135498 (1.3234815613278803) | Probs: 0.9477787613868713 (0.7394115410885721)
Training Process is running: 250/250  | Batch: 265 | Loss: 1.6789015531539917 (1.3248177267106853) | Probs: 0.8383413553237915 (0.7397834576834413)
Training Process is running: 250/250  | Batch: 266 | Loss: 1.0507469177246094 (1.3237912442800257) | Probs: 0.7383818626403809 (0.7397782082638044)
Training Process is running: 250/250  | Batch: 267 | Loss: 2.055450439453125 (1.326521315903806) | Probs: 0.38209545612335205 (0.738443571128952)
Training Process is running: 250/250  | Batch: 268 | Loss: 0.9416888952255249 (1.3250907121094628) | Probs: 0.9175736904144287 (0.7391094823530615)
==========================================!!!Evaluating!!!==========================================
================================================Evaluating================================================
Epoch: 250/250 | Accuracy: 0.7372840374554887 | Normal Acc: 0.9040047897817989 | Anormal Acc: 0.4124432922877511 | Threshold: 0.26
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  23579.98558473587

**front_depth**
=> adam causes loss not to decrease... dont know why?

Training Process is running: 250/250  | Batch: 263 | Loss: 4.482058525085449 (4.4820591753179375) | Probs: 0.030303027480840683 (0.03030302794650197)
Training Process is running: 250/250  | Batch: 264 | Loss: 4.482058525085449 (4.48205917286423) | Probs: 0.030303027480840683 (0.030303027944744758)
Training Process is running: 250/250  | Batch: 265 | Loss: 4.482058525085449 (4.482059170428972) | Probs: 0.030303027480840683 (0.030303027943000757)
Training Process is running: 250/250  | Batch: 266 | Loss: 4.482058525085449 (4.482059168011955) | Probs: 0.030303027480840683 (0.030303027941269822)
Training Process is running: 250/250  | Batch: 267 | Loss: 4.482058525085449 (4.482059165612975) | Probs: 0.030303027480840683 (0.0303030279395518)
Training Process is running: 250/250  | Batch: 268 | Loss: 4.199463367462158 (4.481008623612414) | Probs: 0.03999999910593033 (0.030339076159501165)
==========================================!!!Evaluating!!!==========================================
================================================Evaluating================================================
Epoch: 250/250 | Accuracy: 0.33916560425550624 | Normal Acc: 0.0 | Anormal Acc: 1.0 | Threshold: 0.0
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  22960.860806941986

# Experiment 6:

SGD optimizer, n_threads 4, n/a_train_batch_size 32

### Command:

```
python main.py --root_path /home/username/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name nthreads4_na32
python main.py --root_path /home/username/DAD/ --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name nthreads4_na32
python main.py --root_path /home/username/DAD/ --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name nthreads4_na32
python main.py --root_path /home/username/DAD/ --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name nthreads4_na32
```
**top_depth**
Training Process is running: 250/250  | Batch: 263 | Loss: 0.6787092089653015 (0.6797690296714957) | Probs: 0.9999678730964661 (0.9997282111735055)
Training Process is running: 250/250  | Batch: 264 | Loss: 0.678794264793396 (0.679765351313465) | Probs: 0.9999661445617676 (0.999729109035348)
Training Process is running: 250/250  | Batch: 265 | Loss: 0.6788303256034851 (0.679761836179217) | Probs: 0.999933660030365 (0.9997298780240511)
Training Process is running: 250/250  | Batch: 266 | Loss: 0.6787531971931458 (0.6797580585051118) | Probs: 0.9999639391899109 (0.9997307546576311)
Training Process is running: 250/250  | Batch: 267 | Loss: 0.6787832975387573 (0.679754421337327) | Probs: 0.9999571442604065 (0.9997315993949548)
Training Process is running: 250/250  | Batch: 268 | Loss: 0.5608325004577637 (0.6793123324121241) | Probs: 0.9999866485595703 (0.9997325475331132)
==========================================!!!Evaluating!!!==========================================
================================================Evaluating================================================
Epoch: 250/250 | Accuracy: 0.8231854750076933 | Normal Acc: 0.9119877594465141 | Anormal Acc: 0.6501620220349967 | Threshold: 0.8200000000000001
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  23665.368068933487

**front_depth**
Training Process is running: 250/250  | Batch: 261 | Loss: 0.6773992776870728 (0.7191140615303098) | Probs: 0.9993960857391357 (0.9879862140608198)
Training Process is running: 250/250  | Batch: 262 | Loss: 0.7262994647026062 (0.7191413824549193) | Probs: 0.9537428021430969 (0.9878560109736801)
Training Process is running: 250/250  | Batch: 263 | Loss: 0.6899242997169495 (0.7190307116869724) | Probs: 0.9998316168785095 (0.987901373117259)
Training Process is running: 250/250  | Batch: 264 | Loss: 0.6768397092819214 (0.718871500357142) | Probs: 0.9997442364692688 (0.987946063167644)
Training Process is running: 250/250  | Batch: 265 | Loss: 0.6771759390830994 (0.7187147501267885) | Probs: 0.9997889399528503 (0.9879905852608215)
Training Process is running: 250/250  | Batch: 266 | Loss: 0.6776371002197266 (0.7185609012507321) | Probs: 0.9995172023773193 (0.9880337561114451)
Training Process is running: 250/250  | Batch: 267 | Loss: 0.7241435050964355 (0.7185817318620966) | Probs: 0.9582210183143616 (0.9879225145525007)
Training Process is running: 250/250  | Batch: 268 | Loss: 0.561248242855072 (0.7179968490033345) | Probs: 0.9999457001686096 (0.9879672104098096)
==========================================!!!Evaluating!!!==========================================
================================================Evaluating================================================
Epoch: 250/250 | Accuracy: 0.7968083703345497 | Normal Acc: 0.917176689728579 | Anormal Acc: 0.5622812702527544 | Threshold: 0.3
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time:  23427.982725143433

# Experiment 7:

SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.1) (wrong output CE)

## Train:
### Command:

```
python main.py --root_path /home/username/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_0.8_nthreads4_na32 --loss cence
python main.py --root_path /home/username/DAD/ --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_0.8_nthreads4_na32 --loss cence
python main.py --root_path /home/username/DAD/ --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_0.8_nthreads4_na32 --loss cence
python main.py --root_path /home/username/DAD/ --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_0.8_nthreads4_na32 --loss cence
```

**front_IR**

Training Process is running: 250/250  | Batch: 264 | Loss: 1.3413877487182617 (1.3714841478275803) | Probs: 0.8037793636322021 (0.7948359469197831)
Training Process is running: 250/250  | Batch: 265 | Loss: 1.3417409658432007 (1.3713723313539548) | Probs: 0.8037324547767639 (0.7948693924380424)
Training Process is running: 250/250  | Batch: 266 | Loss: 1.4068671464920044 (1.3715052707364943) | Probs: 0.8010793924331665 (0.7948926508649905)
Training Process is running: 250/250  | Batch: 267 | Loss: 1.3441970348358154 (1.3714033743338798) | Probs: 0.8002747893333435 (0.7949127334712157)
Training Process is running: 250/250  | Batch: 268 | Loss: 1.2434898614883423 (1.3709871053473996) | Probs: 0.8039356470108032 (0.7949420967416838)
==========================================!!!Evaluating!!!==========================================
Epoch: 250/250 | Accuracy: 0.7918406822877743 | Normal Acc: 0.915646620542842 | Anormal Acc: 0.5506156837329876 | Threshold: 0.27
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time: 23990.786917686462

**front_depth**
Training Process is running: 250/250  | Batch: 264 | Loss: 1.3452328443527222 (1.3613431165803154) | Probs: 0.803770899772644 (0.7950687344344157)
Training Process is running: 250/250  | Batch: 265 | Loss: 1.3458807468414307 (1.3612849873707706) | Probs: 0.803230881690979 (0.7950994191985381)
Training Process is running: 250/250  | Batch: 266 | Loss: 1.3444247245788574 (1.3612218403191156) | Probs: 0.8035125136375427 (0.7951309289155382)
Training Process is running: 250/250  | Batch: 267 | Loss: 1.3436529636383057 (1.3611562848091125) | Probs: 0.8035770654678345 (0.7951624443504348)
Training Process is running: 250/250  | Batch: 268 | Loss: 1.24691641330719 (1.3607845139581067) | Probs: 0.8039070963859558 (0.7951909020743998)
==========================================!!!Evaluating!!!==========================================
Epoch: 250/250 | Accuracy: 0.7678814788763353 | Normal Acc: 0.9267562533262373 | Anormal Acc: 0.4583279325988334 | Threshold: 0.21
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time: 23528.597244024277

*top_depth*
Training Process is running: 250/250  | Batch: 264 | Loss: 1.3365756273269653 (1.3371065661592303) | Probs: 0.8037865161895752 (0.8037389492088893)
Training Process is running: 250/250  | Batch: 265 | Loss: 1.3365888595581055 (1.3371046198938126) | Probs: 0.8037745952606201 (0.8037390832166026)
Training Process is running: 250/250  | Batch: 266 | Loss: 1.336437463760376 (1.3371021211817022) | Probs: 0.8038137555122375 (0.8037393628881219)
Training Process is running: 250/250  | Batch: 267 | Loss: 1.33648681640625 (1.337099825268361) | Probs: 0.8037856221199036 (0.8037395354971957)
Training Process is running: 250/250  | Batch: 268 | Loss: 1.2420098781585693 (1.3367903740225366) | Probs: 0.803920328617096 (0.8037401238523046)
==========================================!!!Evaluating!!!==========================================
Epoch: 250/250 | Accuracy: 0.7828724666989053 | Normal Acc: 0.9241617881852049 | Anormal Acc: 0.5075826312378483 | Threshold: 0.66
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time: 23749.79966855049

*top_IR*
Training Process is running: 250/250  | Batch: 264 | Loss: 1.3364652395248413 (1.3414434608423484) | Probs: 0.803798258304596 (0.8021322749695687)
Training Process is running: 250/250  | Batch: 265 | Loss: 1.3366367816925049 (1.3414253906199807) | Probs: 0.803780198097229 (0.8021384701692968)
Training Process is running: 250/250  | Batch: 266 | Loss: 1.336474061012268 (1.3414068463143338) | Probs: 0.8038013577461243 (0.8021446982126558)
Training Process is running: 250/250  | Batch: 267 | Loss: 1.336582064628601 (1.341388843397596) | Probs: 0.8037282824516296 (0.8021506071090698)
Training Process is running: 250/250  | Batch: 268 | Loss: 1.2421841621398926 (1.341066001571095) | Probs: 0.8039008975028992 (0.802156303079668)
==========================================!!!Evaluating!!!==========================================
Epoch: 250/250 | Accuracy: 0.7904778652129951 | Normal Acc: 0.9145156998403406 | Anormal Acc: 0.548801036941024 | Threshold: 0.5700000000000001
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time: 24135.391688346863

## Test:
### Command: 
```bash
python main.py --root_path /home/username/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name cence_0.8_nthreads4_na32
```

Mode: Top(D):      Best Acc: 82.85 | Threshold: 0.77 | AUC: 0.8809                                                                                                                                                    
View: Top(D)(post-processed):       Best Acc: 82.91 | Threshold: 0.77 | AUC: 0.882                                                                                                                                    
                                                                                                                                                                                                                      
Mode: Top(IR):      Best Acc: 81.56 | Threshold: 0.54 | AUC: 0.8574                                                                                                                                                   
View: Top(IR)(post-processed):       Best Acc: 81.61 | Threshold: 0.54 | AUC: 0.8598

Mode: Top(DIR):      Best Acc: 83.7 | Threshold: 0.68 | AUC: 0.8907
View: Top(DIR)(post-processed):       Best Acc: 83.78 | Threshold: 0.68 | AUC: 0.8921

Mode: Front(D):      Best Acc: 85.41 | Threshold: 0.49 | AUC: 0.8869
View: Front(D)(post-processed):       Best Acc: 85.49 | Threshold: 0.5 | AUC: 0.8885

Mode: Front(IR):      Best Acc: 82.87 | Threshold: 0.6 | AUC: 0.8647
View: Front(IR)(post-processed):       Best Acc: 82.93 | Threshold: 0.6 | AUC: 0.8671

Mode: Front(DIR):      Best Acc: 86.34 | Threshold: 0.6 | AUC: 0.8957
View: Front(DIR)(post-processed):       Best Acc: 86.46 | Threshold: 0.6 | AUC: 0.8975

Mode: Fusion(D):      Best Acc: 90.42 | Threshold: 0.69 | AUC: 0.9464
View: Fusion(D)(post-processed):       Best Acc: 90.52 | Threshold: 0.69 | AUC: 0.9478

Mode: Fusion(IR):      Best Acc: 88.2 | Threshold: 0.71 | AUC: 0.929
View: Fusion(IR)(post-processed):       Best Acc: 88.38 | Threshold: 0.71 | AUC: 0.9313

Mode: Fusion(DIR):      Best Acc: 91.28 | Threshold: 0.71 | AUC: 0.9556
View: Fusion(DIR)(post-processed):       Best Acc: 91.4 | Threshold: 0.71 | AUC: 0.9571

Total testing time: 4006.5820257663727

# Experiment 8:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.0) (wrong output CE)

## Train:
### Command:

```
python main.py --root_path /home/username/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32 --loss cence
python main.py --root_path /home/username/DAD/ --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32 --loss cence
python main.py --root_path /home/username/DAD/ --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32 --loss cence
python main.py --root_path /home/username/DAD/ --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32 --loss cence
```

*front depth*
Training Process is running: 250/250  | Batch: 264 | Loss: 3.6291306018829346 (3.6308324121079356) | Probs: 0.18508762121200562 (0.18492844093520686)
Training Process is running: 250/250  | Batch: 265 | Loss: 3.6310863494873047 (3.6308333667597377) | Probs: 0.1844446212053299 (0.18492662206404192)
Training Process is running: 250/250  | Batch: 266 | Loss: 3.628255605697632 (3.6308237122239246) | Probs: 0.18512874841690063 (0.18492737909158072)
Training Process is running: 250/250  | Batch: 267 | Loss: 3.63374924659729 (3.6308346283969595) | Probs: 0.18509167432785034 (0.18492799213350708)
Training Process is running: 250/250  | Batch: 268 | Loss: 3.404473304748535 (3.630097980667746) | Probs: 0.19139045476913452 (0.1849490229277653)
==========================================!!!Evaluating!!!==========================================
Epoch: 250/250 | Accuracy: 0.8019958675869345 | Normal Acc: 0.9251596593932943 | Anormal Acc: 0.5620220349967595 | Threshold: 0.8
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time: 23848.42882323265

*top depth*
Training Process is running: 250/250  | Batch: 264 | Loss: 3.629951000213623 (3.629771798511721) | Probs: 0.18509888648986816 (0.1850946845873347)
Training Process is running: 250/250  | Batch: 265 | Loss: 3.6293740272521973 (3.629770303131046) | Probs: 0.18511153757572174 (0.1850947479444339)
Training Process is running: 250/250  | Batch: 266 | Loss: 3.6295502185821533 (3.629769478844346) | Probs: 0.18510785698890686 (0.18509479704197873)
Training Process is running: 250/250  | Batch: 267 | Loss: 3.638030529022217 (3.6298003036584428) | Probs: 0.18511690199375153 (0.18509487952314205)
Training Process is running: 250/250  | Batch: 268 | Loss: 3.4033331871032715 (3.629063311647338) | Probs: 0.19286751747131348 (0.18512017402134626)
==========================================!!!Evaluating!!!==========================================
Epoch: 250/250 | Accuracy: 0.7707829603903812 | Normal Acc: 0.8920968600319319 | Anormal Acc: 0.5344134802333117 | Threshold: 0.9500000000000001
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time: 24005.303787708282

*top ir*
Training Process is running: 250/250  | Batch: 264 | Loss: 3.6341335773468018 (3.630328317858138) | Probs: 0.18502730131149292 (0.18509904067471342)
Training Process is running: 250/250  | Batch: 265 | Loss: 3.6294193267822266 (3.6303249005984544) | Probs: 0.1851039081811905 (0.18509905897360995)
Training Process is running: 250/250  | Batch: 266 | Loss: 3.6339242458343506 (3.630338381292222) | Probs: 0.18511229753494263 (0.18509910855623668)
Training Process is running: 250/250  | Batch: 267 | Loss: 3.628708600997925 (3.630332300022467) | Probs: 0.18512043356895447 (0.18509918812717965)
Training Process is running: 250/250  | Batch: 268 | Loss: 3.403804302215576 (3.629595109885485) | Probs: 0.1928521692752838 (0.18512441865625298)
==========================================!!!Evaluating!!!==========================================
Epoch: 250/250 | Accuracy: 0.7605838132500989 | Normal Acc: 0.864888238424694 | Anormal Acc: 0.5573558003888529 | Threshold: 0.9
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time: 24533.764451742172

*front ir*
Training Process is running: 250/250  | Batch: 264 | Loss: 3.6407716274261475 (3.630613044522843) | Probs: 0.18473120033740997 (0.1849340928050707)
Training Process is running: 250/250  | Batch: 265 | Loss: 3.632228374481201 (3.6306191171918596) | Probs: 0.18445584177970886 (0.18493229486888513)
Training Process is running: 250/250  | Batch: 266 | Loss: 3.6289494037628174 (3.630612863583511) | Probs: 0.18512673676013947 (0.18493302311566884)
Training Process is running: 250/250  | Batch: 267 | Loss: 3.6331918239593506 (3.630622486569988) | Probs: 0.18513035774230957 (0.18493375943890258)
Training Process is running: 250/250  | Batch: 268 | Loss: 3.403326988220215 (3.6298827987557396) | Probs: 0.19283327460289001 (0.18495946683367148)
==========================================!!!Evaluating!!!==========================================
Epoch: 250/250 | Accuracy: 0.7557040488855673 | Normal Acc: 0.9163783927621075 | Anormal Acc: 0.4426441996111471 | Threshold: 0.81
==========================================!!!Logging!!!==========================================
==========================================!!!Saving!!!==========================================
Total training time: 24217.14488005638


## Test
```bash
python main.py --root_path /home/username/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32
```
Mode: Top(D):      Best Acc: 85.11 | Threshold: 0.91 | AUC: 0.8881
View: Top(D)(post-processed):       Best Acc: 85.16 | Threshold: 0.91 | AUC: 0.89

Mode: Top(IR):      Best Acc: 78.71 | Threshold: 0.88 | AUC: 0.8313
View: Top(IR)(post-processed):       Best Acc: 78.78 | Threshold: 0.88 | AUC: 0.8331

Mode: Top(DIR):      Best Acc: 83.31 | Threshold: 0.87 | AUC: 0.8864
View: Top(DIR)(post-processed):       Best Acc: 83.36 | Threshold: 0.88 | AUC: 0.8878

Mode: Front(D):      Best Acc: 85.25 | Threshold: 0.9 | AUC: 0.8952
View: Front(D)(post-processed):       Best Acc: 85.36 | Threshold: 0.9 | AUC: 0.8968

Mode: Front(IR):      Best Acc: 81.66 | Threshold: 0.91 | AUC: 0.842
View: Front(IR)(post-processed):       Best Acc: 81.79 | Threshold: 0.91 | AUC: 0.8445

Mode: Front(DIR):      Best Acc: 86.98 | Threshold: 0.92 | AUC: 0.9117
View: Front(DIR)(post-processed):       Best Acc: 87.11 | Threshold: 0.92 | AUC: 0.9135

Mode: Fusion(D):      Best Acc: 89.44 | Threshold: 0.92 | AUC: 0.9455
View: Fusion(D)(post-processed):       Best Acc: 89.54 | Threshold: 0.92 | AUC: 0.9469

Mode: Fusion(IR):      Best Acc: 84.08 | Threshold: 0.9 | AUC: 0.91
View: Fusion(IR)(post-processed):       Best Acc: 84.2 | Threshold: 0.9 | AUC: 0.9119

Mode: Fusion(DIR):      Best Acc: 89.22 | Threshold: 0.91 | AUC: 0.9496
View: Fusion(DIR)(post-processed):       Best Acc: 89.3 | Threshold: 0.91 | AUC: 0.951

Total testing time: 4004.694367170334

# Eperiment 9:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.0), 2 separated projection heads

## Train:
### Command:

```
python main.py --root_path /home/username/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32 --loss cence --head two_heads_cence
python main.py --root_path /home/username/DAD/ --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32 --loss cence --head two_heads_cence
python main.py --root_path /home/username/DAD/ --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32 --loss cence --head two_heads_cence
python main.py --root_path /home/username/DAD/ --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32 --loss cence --head two_heads_cence
```

## Test:
```bash
python main.py --root_path /home/username/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name cence_beta0.8_eps0_nthreads4_na32
```
Mode: Top(D):      Best Acc: 84.02 | Threshold: 0.97 | AUC: 0.8695
View: Top(D)(post-processed):       Best Acc: 84.11 | Threshold: 0.97 | AUC: 0.8714

Mode: Top(IR):      Best Acc: 80.99 | Threshold: 0.9 | AUC: 0.8498
View: Top(IR)(post-processed):       Best Acc: 81.11 | Threshold: 0.9 | AUC: 0.8521

Mode: Top(DIR):      Best Acc: 83.15 | Threshold: 0.94 | AUC: 0.8779
View: Top(DIR)(post-processed):       Best Acc: 83.23 | Threshold: 0.94 | AUC: 0.8797

Mode: Front(D):      Best Acc: 85.61 | Threshold: 0.87 | AUC: 0.8642
View: Front(D)(post-processed):       Best Acc: 85.68 | Threshold: 0.87 | AUC: 0.8657

Mode: Front(IR):      Best Acc: 83.88 | Threshold: 0.97 | AUC: 0.8746
View: Front(IR)(post-processed):       Best Acc: 84.16 | Threshold: 0.97 | AUC: 0.8785

Mode: Front(DIR):      Best Acc: 87.4 | Threshold: 0.92 | AUC: 0.8933
View: Front(DIR)(post-processed):       Best Acc: 87.48 | Threshold: 0.92 | AUC: 0.8952

Mode: Fusion(D):      Best Acc: 87.57 | Threshold: 0.92 | AUC: 0.913
View: Fusion(D)(post-processed):       Best Acc: 87.66 | Threshold: 0.93 | AUC: 0.9145

Mode: Fusion(IR):      Best Acc: 84.94 | Threshold: 0.94 | AUC: 0.912
View: Fusion(IR)(post-processed):       Best Acc: 85.13 | Threshold: 0.94 | AUC: 0.9144

Mode: Fusion(DIR):      Best Acc: 89.47 | Threshold: 0.94 | AUC: 0.9457
View: Fusion(DIR)(post-processed):       Best Acc: 89.59 | Threshold: 0.94 | AUC: 0.9474

Total testing time: 4015.3029034137726

# Eperiment 10:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.1), 1 projection heads

## Train:
### Command:

```
python main.py --root_path /home/username/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32 --loss cence
python main.py --root_path /home/username/DAD/ --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32 --loss cence
python main.py --root_path /home/username/DAD/ --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32 --loss cence
python main.py --root_path /home/username/DAD/ --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32 --loss cence
```

## Test:
```bash
python main.py --root_path /home/username/DAD/ --mode test --model_type resnet --model_depth 18 --shortcut_type A --val_batch_size 70 --cal_vec_batch_size 100 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32
```
Mode: Top(D):      Best Acc: 80.92 | Threshold: 0.97 | AUC: 0.8398
View: Top(D)(post-processed):       Best Acc: 80.98 | Threshold: 0.97 | AUC: 0.8414

Mode: Top(IR):      Best Acc: 81.32 | Threshold: 0.93 | AUC: 0.8603
View: Top(IR)(post-processed):       Best Acc: 81.4 | Threshold: 0.93 | AUC: 0.8622

Mode: Top(DIR):      Best Acc: 82.73 | Threshold: 0.95 | AUC: 0.8786
View: Top(DIR)(post-processed):       Best Acc: 82.79 | Threshold: 0.95 | AUC: 0.88

Mode: Front(D):      Best Acc: 84.17 | Threshold: 0.9 | AUC: 0.8526
View: Front(D)(post-processed):       Best Acc: 84.24 | Threshold: 0.9 | AUC: 0.8541

Mode: Front(IR):      Best Acc: 78.5 | Threshold: 0.97 | AUC: 0.801
View: Front(IR)(post-processed):       Best Acc: 78.63 | Threshold: 0.97 | AUC: 0.8043

Mode: Front(DIR):      Best Acc: 85.14 | Threshold: 0.94 | AUC: 0.8745
View: Front(DIR)(post-processed):       Best Acc: 85.22 | Threshold: 0.94 | AUC: 0.8762

Mode: Fusion(D):      Best Acc: 84.85 | Threshold: 0.94 | AUC: 0.8911
View: Fusion(D)(post-processed):       Best Acc: 84.9 | Threshold: 0.94 | AUC: 0.8924

Mode: Fusion(IR):      Best Acc: 83.54 | Threshold: 0.96 | AUC: 0.8989
View: Fusion(IR)(post-processed):       Best Acc: 83.66 | Threshold: 0.96 | AUC: 0.901

Mode: Fusion(DIR):      Best Acc: 87.39 | Threshold: 0.95 | AUC: 0.933
View: Fusion(DIR)(post-processed):       Best Acc: 87.45 | Threshold: 0.95 | AUC: 0.9344

Total testing time: 4035.602260828018


# Eperiment 11:
SGD optimizer, n_threads 4, n/a_train_batch_size 32, CENCE loss (beta0.8, eps 0.0), 1 projection heads correct output

## Train:
### Command:

```
python main.py --root_path /home/username/DAD/ --mode train --view top_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32 --loss cence
python main.py --root_path /home/username/DAD/ --mode train --view top_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32 --loss cence
python main.py --root_path /home/username/DAD/ --mode train --view front_IR --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32 --loss cence
python main.py --root_path /home/username/DAD/ --mode train --view front_depth --model_type resnet --model_depth 18 --shortcut_type A --pre_train_model False --n_train_batch_size 32 --a_train_batch_size 32 --val_batch_size 70  --learning_rate 0.01 --epochs 250 --cal_vec_batch_size 100 --tau 0.1 --train_crop 'random' --n_scales 5 --downsample 2 --n_split_ratio 1.0 --a_split_ratio 1.0 --save_step 10 --val_step 10 --n_threads 4 --name cence_beta0.8_eps0.1_nthreads4_na32 --loss cence
```
- leaky relu
- csp network
- new project head for ce


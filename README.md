# How to use this code and do the speaker recognition

```bash
>> pip install speechbrain
```

Firstly, we have 

**custom_model.py**: a well-defined TDNN model by pytorch, 

**inference.py**: use to predict the new .flac audio file , 

**inferece_noise.py**: use to predict the new .flac audio file with noise, 

**mini_librispeech_prepare.py**: use the prepare the audio file, which will create train.json, valid.json, test.json after working. You can just run train.py and it will run mini_librispeech_prepare.py at first.

**train.py**: use to do the whole work, and we run it first of all.

**data** file folder: contain all the noise and audio datas we will use in our project. Then we show the files' tree.

```
|─content
│  └─best_model
├─data
│  ├─LibriSpeech_SI
│  │  ├─noise
│  │  ├─test
│  │  ├─test-noisy
│  │  └─train
│  │      ├─spk001
│  │      ├─spk002
│  │      ├─spk003
│  │      ├─spk004
│  │      ├─......
│  └─RIRS_NOISES
│      ├─pointsource_noises
│      ├─real_rirs_isotropic_noises
│      └─simulated_rirs
│          ├─largeroom
│          │  ├─Room001
│          │  ├─Room002
│          │  └─......
│          ├─mediumroom
│          │  ├─Room001
│          │  ├─Room002
│          │  ├─......
│          └─smallroom
│              ├─Room001
│              ├─Room002
│              ├─......
├─pretrained_models
│  ├─EncoderClassifier-c7c226823887b6cf7433ddb7e3319813
│  └─EncoderClassifier-fab6304d6f8a8e30333af1f33bbe745c
├─results
│  └─speaker_id
│      └─1986
│          └─save
│              └─CKPT+2022-12-29+04-15-58
```

**content/best\_model** file folder: save our well-trained model and related _.yaml_ file, which we can use to do the inference/ predict the new audio file.

- At beginning,
```bash
>> python train.py train.yaml
```
- we will get train.json, valid.json, test.json, which save all training audio files and split them into train, valid, test set automatically. And we will get the filefolder _results_, which save the pretrained TDNN model and other related files created by our audio files. 

- Then we write a _plot.py_ file to plot the train_loss and valid_loss according to the train_log.txt file, which records all the changes of the train_loss and valid_loss in our model.
  
```bash
>> python plot.py
```

- Next, according to the model in the file folder _results/speaker_id/1986/save/CKPT+2022-12-29+04-15-58+00_, which contains model-related configuration files, we change the _content/best_model/hparams_inference.yaml_, which we will use to do the predictions.

- Last, we run the _inference.py_ and _inference\_noise.py_, then we will get 2 _.txt_ flies, which saves our prediction results about the datas in _data/LibriSpeech_SI/test_ and _data/LibriSpeech_SI/test-noisy_

```bash
>> python inference.py
>> python inference_noise.py
```

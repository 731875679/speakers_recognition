import torchaudio
from speechbrain.pretrained import EncoderClassifier

classifier = EncoderClassifier.from_hparams(source="content/best_model/", hparams_file='hparams_inference.yaml', savedir="content/best_model/")
import os
audio_list=[]
audio_path="data\\LibriSpeech_SI\\test"
for root,dirs,files in os.walk(audio_path):
    for f in files:
        audio_list.append(root+'\\'+f)

File=open('answer.txt',mode='w')

#clean the answer.txt
with open('answer.txt', "r+") as f:
    read_data = f.read()
    f.seek(0)  #get the location
    f.truncate() 

# Perform classification
for path in audio_list:
    audio_file = path
    name=(audio_file.split('\\'))[-1]
    signal, fs = torchaudio.load(audio_file) 
    output_probs, score, index, text_lab = classifier.classify_batch(signal)
    File.write(name+'-'+text_lab[0]+'\n')

File.close()

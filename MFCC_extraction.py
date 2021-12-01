import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import librosa
import csv
import os
from glob import glob


## reading all filenames from test folder, which has 5 subfolders corresponding to 5 classes. 
root = 'D:/Sounds_file/test'
test_filenames= []
for path, subdirs, files in os.walk(root):
    for name in files:
        #print(os.path.join(path, name))
        test_filenames.append(os.path.join(path, name))
                     
def load_audio_file(file_path):
   input_length = 16000
   data = librosa.core.load(file_path)[0] #, sr=16000
   return data  
   
# Original directory name is 'D:/Sounds_file/test/class1_sound/1345.wav'
## this function returns: ['class1_sound', '1345.wav']
def get_sound_id_from_file_path(file_path):
    a = file_path.split('\\')[-2:]
    return a
    
    
    
    
 ## This function extracts  mean chroma_stft, rmse, spectral_centroid, spectral_bandwidth, rolloff, zero_crossing_rate, and 21 mfcc mean values. 
 def extractWavFeatures(soundFilesFolder, csvFileName):
    print("The features of the files in the folder "+soundFilesFolder+" will be saved to "+csvFileName)
    header = 'key correlation chroma_stft rmse spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
    for i in range(1, 21):
        header += f' mfcc{i}'
    #header += ' label'
    header = header.split()
    print('CSV Header: ', header)
    file = open(csvFileName, 'w', newline='')
    #with file:
    writer = csv.writer(file)
    writer.writerow(header)
    
    for i in test_filenames:
        correlation, key  = get_sound_id_from_file_path(i)
        y, sr = librosa.load(i, mono=True, duration=30)
        
        # remove leading and trailing silence
        
        y, index = librosa.effects.trim(y)
        
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        rmse = librosa.feature.rms(y=y)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        
        to_append = f' {key} {correlation} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
        for e in mfcc:
            to_append += f' {np.mean(e)}'
        writer.writerow(to_append.split())
    file.close()
    print("End of extractWavFeatures")
    
    
    
CREATE_CSV_FILES = True

TRAIN_CSV_FILE = "D:/Sound_files/test/MFCC.csv"
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import librosa
import csv
import os



if (CREATE_CSV_FILES == True):
    extractWavFeatures("D:/Sound_files/test", TRAIN_CSV_FILE)
 
    print("CSV files are created")
else:
    print("CSV files creation is skipped")


## Then we can read this csv file with pandas dataframe.
import pandas as pd
df  = pd.read_csv("D:/Sound_files/test/MFCC.csv")











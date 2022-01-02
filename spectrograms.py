import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob 
import librosa as lr


data_dir ='C:/Users/Asus/Documents/split_sound/'
audio_files =glob(data_dir + '/*.wav')
len(audio_files)

audio, sfreq =lr.load(audio_files[0])
time = np.arange(0, len(audio)) / sfreq


fig, ax=plt.subplots()
ax.plot(time, audio)
ax.set(xlabel= 'Time(s)',ylabel = 'Sound Amplitude')
#plt.savefig('C:/Users/Asus/Documents/COVID19/spectrograms/' +'1'+ ".png")

%%time
for file in range(0, len(audio_files), 1):
    count=0
    audio, sfreq =lr.load(audio_files[file])
    time =np.arange(0, len(audio))/ sfreq
    
    fig, ax= plt.subplots()
    ax.plot(time,audio)
    ax.set (xlabel ='Time(s)', ylabel= 'Sound Amplitude')
    plt.savefig('C:/Users/Asus/Documents/spectrograms/' +str(file) + ".png")
    plt.show()
    count+=1
print(count)

# There are two methods for chunking.
# first method splits an audio on silence. If there are 500 ms silence in audio, it will make them a chunk. 

from pydub import AudioSegment
from pydub.utils import make_chunks
def split(filepath):
    sound = AudioSegment.from_wav(filepath)
    dBFS = sound.dBFS
    chunks = split_on_silence(sound, 
        min_silence_len = 500,
        silence_thresh = dBFS-16)
    return chunks
  
# the second method splits the given audio for 1000 ms which is 1second   
from pydub import AudioSegment
from pydub.utils import make_chunks

#file_path = 'C:/Users/Asus/Documents/Foldername/newwav/1588311962576.wav'
def get_sound_id_from_file_path(file_path):
    a = file_path.split('/')[-1][:-4]
    
    return a
#get_sound_id_from_file_path('C:/Users/Asus/Documents/Foldername/testwav/1586793423518.wav')

for i in get_data_files(): 
    myaudio = AudioSegment.from_file(i , "wav") 
    chunk_length_ms = 1000 # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms)
    j = get_sound_id_from_file_path(i)#Make chunks of one sec
    for i, chunk in enumerate(chunks):
        chunk.export('C:/Users/Asus/Documents/split_sound/'+j+'_'+str(i)+ '.wav', format="wav")

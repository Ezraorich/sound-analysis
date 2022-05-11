## checking the file length. if the audio file length is less than 1 second, then we should delete this file from the directory before creating the custom dataset.

path_train = 'D:/COVID_COUGH_SOUNDS/1second_chunks_458/balanced_1s_not_aug/one_shot1sec/train'
path_test = 'D:/COVID_COUGH_SOUNDS/1second_chunks_458/balanced_1s_not_aug/one_shot1sec/train'

def one_sec_file_length_filter(path):
    #audio_names =[]
    count=0
    for subdir, dirs, files in os.walk(path):
        for file in files:
            filepath =subdir+os.sep+file
            print(filepath)
            data_waveform, rate_of_sample = torchaudio.load(filepath)
            if (data_waveform.shape[1]!=22050):
                print(data_waveform.shape)
                os.remove(filepath)
                count+=1
    print(count)
    
one_sec_file_length_filter(path_test)
one_sec_file_length_filter(path_train)

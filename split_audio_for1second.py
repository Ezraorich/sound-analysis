directory_in_str = 'D:/Sound'
new_dir  = 'D:/CHUNKS_WITH_OVERLAP50/'
pathlist = Path(directory_in_str).glob('**/*.wav')
for i in pathlist:
    path_in_str = str(i)
    #print(path_in_str)
    base=os.path.basename(i)
    a = os.path.splitext(base)[0]
    #print(a)
    data, sr = librosa.load(path_in_str)
    avg = int(sr/2)
    # split 1 sec with 50% overlap
    split = []
    noSections = int(np.ceil(len(data) / sr))*2-1

    for i in range(noSections):
    # get 1 second
    
        temp = data[i*avg:i*avg + sr] # this is for mono audio
    
        split.append(temp)

    for i in range(noSections):
        filename = new_dir+str(a)+'_covid_{0}.wav'.format(i)
    
        sf.write(filename, split[i], sr, format = 'wav')
        print(librosa.get_duration(y=split[i], sr=sr))

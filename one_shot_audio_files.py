## Doing one-shot learning on audio files.
## Audio files of the same length were converted to tensors. If you have audio files of the different length, then cut them to equal sized chunks or use padding method to
## make them equal sized tensors.
## So after that you need dataset which has the following structure:
# class_name1/
    # 12345.wav
    # 12346.wav
    # 12347.wav
# class_name2/
    # 1.wav
    # 2.wav
    # 3.wav and etc.

## path = 'your path here' 
## path = root_dir + class_name+ audio_filename
## root_dir in my case was 'D:/1second_chunks_458/balanced_1s_not_aug/one_shot1sec/test/'
## class_name in my case was 'allergies'
## path in my case was 'D:/1second_chunks_458/balanced_1s_not_aug/one_shot1sec/test/allergies\1594464974023_13.wav'
path_train = 'D:/1second_chunks_458/balanced_1s_not_aug/one_shot1sec/train/'
path_test = 'D:/1second_chunks_458/balanced_1s_not_aug/one_shot1sec/test/'
root_dir = path_train
categories = [[folder, os.listdir(root_dir +'/'+ folder)] for folder in os.listdir(root_dir)  if not folder.startswith('.') ]


# creating the pairs of images for inputs, same character label = 1, vice versa
class Audio_sound_Dataset(Dataset):
    def __init__(self, categories, root_dir, transform=None):
        self.categories = categories
        self.root_dir = root_dir
        self.transform = transform
        
        
        audio_names =[]
        for subdir, dirs, files in os.walk(self.root_dir):
            for file in files:
                filepath =subdir+os.sep+file
                audio_names.append(filepath)
        self.audio_names = audio_names
        
    def __len__(self):
        return len(self.audio_names)
    def __getitem__(self, idx):
        audio1 = None
        audio2 = None
        label = None
        
        audio_names =[]
        for subdir, dirs, files in os.walk(self.root_dir):
            for file in files:
                filepath =subdir+os.sep+file
                audio_names.append(filepath)
        self.audio_names = audio_names
        
        class_name = self.audio_names[idx].split('\\')[1]
        list_categories = ['asthma', 'allergies', 'pneumonia', 'covid','other']
        channel_dict = {'asthma': 0, 'allergies': 1, 'pneumonia': 2, 'covid':3,'other':4}
        label = channel_dict.get(class_name)
        
        
        if idx % 2 == 0: # select the same character for both images
            category = random.choice(categories)
            character = random.choice(category[1])
            #category = random.choice(list_categories)
            audioDir = str(root_dir) + str(category[0]) 
            audio1Name = random.choice(os.listdir(audioDir))
            audio2Name = random.choice(os.listdir(audioDir))
            audio1, _ = torchaudio.load(str(audioDir) + os.sep + str(audio1Name)) 
            audio2, _ = torchaudio.load(str(audioDir) + os.sep + str(audio2Name)) 
            
            #print(audioDir + os.sep + audio1Name)
            #print(audioDir + os.sep + audio2Name)
            label = 1.0
        else: # select a different character for both images
            category1, category2 = random.choice(categories), random.choice(categories)
            category1, category2 = random.choice(categories), random.choice(categories)
            character1, character2 = random.choice(category1[1]), random.choice(category2[1])
            audioDir1, audioDir2 = str(root_dir) + str(category1[0]), str(root_dir) + str(category2[0])
            audio1Name = random.choice(os.listdir(audioDir1))
            audio2Name = random.choice(os.listdir(audioDir2))
            while audio1Name == audio2Name:
                audio2Name = random.choice(os.listdir(audioDir2))
            label = 0.0
            audio1, _ = torchaudio.load(str(audioDir1) + os.sep + str(audio1Name)) 
            audio2, _ = torchaudio.load(str(audioDir2) + os.sep+ str(audio2Name)) 
#         plt.imshow(img1)
        if self.transform:
            audio1 = self.transform(audio1)
            audio2 = self.transform(audio2)
        
  
        return audio1, audio2, torch.from_numpy(np.array([label], dtype=np.float32)) 
  
  
  
  
# choose a training dataset size and further divide it into train and validation set 80:20



train_set = Audio_sound_Dataset(categories, root_dir, transform =None)

train_loader = torch.utils.data.DataLoader(train_set, batch_size=128, num_workers=0)

## To check whether your dataset loads everything correctly run this code:
for i_batch, sample_batched in enumerate(train_loader):
    print(i_batch, sample_batched)
#val_loader = torch.utils.data.DataLoader(val_set, batch_size=1, num_workers=16, shuffle=True)

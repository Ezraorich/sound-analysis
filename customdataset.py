import torch
from torch.utils.data import Dataset
from torchvision import datasets
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
from torch import nn
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt
import numpy as np
import tensorboard
import torchvision
from torch.utils.tensorboard import SummaryWriter
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Using {} device'.format(device))
from sklearn.model_selection import KFold


import os
test_classes = []
test_x = next(os.walk('D:/1second_chunks_458/stft_images_1sec_no_overlap/test/allergies/'))[2]
test_y = next(os.walk('D:/1second_chunks_458/stft_images_1sec_no_overlap/test/covid/'))[2]
for i in range(len(test_x)):
    test_classes.append(0)
for i in range(len(test_y)):
    test_classes.append(1)
    
test_image_path = []

root_dir = 'D:/1second_chunks_458/stft_images_1sec_no_overlap/test/'
classname1 = 'allergies/'
classname2 = 'covid/'

for index in range(len(test_x)):
    test_image_path.append(os.path.join(root_dir, classname1, test_x[index]))
for index in range(len(test_y)):
    test_image_path.append(os.path.join(root_dir, classname2, test_y[index]))
    
train_classes = []
train_x = next(os.walk('D:/1second_chunks_458/stft_images_1sec_no_overlap/train/allergies/'))[2]
train_y = next(os.walk('D:/1second_chunks_458/stft_images_1sec_no_overlap/train/covid/'))[2]
for i in range(len(train_x)):
    train_classes.append(0)
for i in range(len(train_y)):
    train_classes.append(1)
    
    
train_image_path = []

root_dir = 'D:/1second_chunks_458/stft_images_1sec_no_overlap/train/'
classname1 = 'allergies/'
classname2 = 'covid/'

for index in range(len(train_x)):
    train_image_path.append(os.path.join(root_dir, classname1, train_x[index]))
for index in range(len(train_y)):
    train_image_path.append(os.path.join(root_dir, classname2, train_y[index]))
 
from torch.utils.data import Dataset, DataLoader
from skimage import io
class LandmarkDataset(Dataset):
    def __init__(self, image_paths, classes, transform=None):
        self.image_paths = image_paths
        self.transform = transform
        self.classes = classes
        
    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_filepath = self.image_paths[idx]
        image = cv2.imread(image_filepath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        
        label = self.classes[idx]
        
        if self.transform:
            image = self.transform(image)
        
        return image, label
      
train_dataset = LandmarkDataset(train_image_path,train_classes, transform)
test_dataset = LandmarkDataset(test_image_path, test_classes, transform)

train_loader = DataLoader(
    train_dataset, batch_size=4, shuffle=True
)
test_loader = DataLoader(
    test_dataset, batch_size=4, shuffle=True
)

    
 

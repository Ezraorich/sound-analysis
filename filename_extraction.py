from pathlib import Path
import os


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import librosa
import csv
import os

import pandas as pd
from glob import glob
filepath = 'D:/folded_name/'
pathlist = Path(filepath).glob('**/*.wav')


DATA_DIR ='D:/folder_name_with_files/'
filenames = glob(DATA_DIR + '/*.wav')

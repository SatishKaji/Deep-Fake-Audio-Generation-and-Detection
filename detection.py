# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import os

"""# New Section"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

# Don't Show Warning Messages
import warnings
warnings.filterwarnings('ignore')



from pydub import AudioSegment
import IPython

# We will listen to this file:
# 213_1p5_Pr_mc_AKGC417L.wav

audio_file = '/content/drive/MyDrive/FakeAudios/Fake/sample10.wav'

path = audio_file

IPython.display.Audio(path)



import soundfile as sf

# Define helper functions

# Load a .wav file. 
# These are 24 bit files. The PySoundFile library is able to read 24 bit files.
# https://pysoundfile.readthedocs.io/en/0.9.0/

def get_wav_info(wav_file):
    data, rate = sf.read(wav_file)
    return data, rate

# source: Andrew Ng Deep Learning Specialization, Course 5
def graph_spectrogram(wav_file):
    data, rate = get_wav_info(wav_file)
    nfft = 200 # Length of each window segment
    fs = 8000 # Sampling frequencies
    noverlap = 120 # Overlap between windows
    nchannels = data.ndim
    if nchannels == 1:
        pxx, freqs, bins, im = plt.specgram(data, nfft, fs, noverlap = noverlap)
    elif nchannels == 2:
        pxx, freqs, bins, im = plt.specgram(data[:,0], nfft, fs, noverlap = noverlap)
    return pxx

path = 'D:/FakeAudios/Fake/sample10.wav'


x = graph_spectrogram(path)

audio_file = 'D:/FakeAudios/Fake/sample10.wav'

path = audio_file

# read the file
data, rate = sf.read(path)

# display the numpy array
data

from pydub import AudioSegment

# note: Time is given in seconds. Will be converted to milliseconds later.
start_time = 0
end_time = 7

t1 = start_time * 1000 # pydub works in milliseconds
t2 = end_time * 1000
newAudio = AudioSegment.from_wav(path) # path is defined above
newAudio = newAudio[t1:t2]
newAudio.export('new_slice.wav', format="wav")

# Lets listen to the new slice

IPython.display.Audio('new_slice.wav')

import os
import matplotlib.pyplot as plt

#for loading and visualizing audio files
import librosa
import librosa.display

#to play audio
import IPython.display as ipd

audio_fpath = "D:/FakeAudios/Fake/"
audio_clips = os.listdir(audio_fpath)
print("No. of .wav files in audio folder = ",len(audio_clips))

x, sr = librosa.load(audio_fpath+audio_clips[0], sr=44100)

print(type(x), type(sr))
print(x.shape, sr)

plt.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr=sr)

X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()

plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()

import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
import librosa
import numpy as np
import pathlib
from pathlib import Path
import librosa.display

def create_fold_spectrograms():
    spectrogram_path = Path('D:/FakeAudios/FakeA/')  
    audio_path = Path('D:/FakeAudios/Fake/')  
    print(f'Processing fold Files')
    for audio_file in list(Path(audio_path).glob('*.wav')):
        samples, sample_rate = librosa.load(audio_file)
        fig = plt.figure(figsize=[0.72,0.72])
        ax = fig.add_subplot(111)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.set_frame_on(False)
        filename  = spectrogram_path/Path(audio_file).name.replace('.wav','.png')
        S = librosa.feature.melspectrogram(y=samples, sr=sample_rate)
        librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
        plt.savefig(filename, dpi=400, bbox_inches='tight',pad_inches=0)
        plt.close('all')

create_fold_spectrograms()

data_path = Path('D:/FakeAudios/Data/')
spectrogram_path = Path('D:/FakeAudios/FakeA/')

IMG_SIZE = 50

DATADIR = 'D:/FakeAudios/'

CATEGORIES = ['FakeA', 'RealA']

for category in CATEGORIES :
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)

training_data = []

def create_training_data():
    for category in CATEGORIES :
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try :
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass

create_training_data()

random.shuffle(training_data)

X = [] #features
y = [] #labels

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
y = np.asarray(y)

import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt

scale_file = "D:/FakeAudios/Fake/sample10.wav"

ipd.Audio(scale_file)

scale, sr = librosa.load(scale_file)

filter_banks = librosa.filters.mel(n_fft=2048, sr=22050, n_mels=10)

filter_banks.shape

plt.figure(figsize=(25,10))
librosa.display.specshow(filter_banks,
                         sr =sr,
                         x_axis = 'linear')
plt.colorbar(format="%+2.f")
plt.show()

mel_spectrogram = librosa.feature.melspectrogram(scale, sr=sr, n_fft=2048, hop_length=512, n_mels=10)

mel_spectrogram.shape

log_mel_spec = librosa.power_to_db(mel_spectrogram)

plt.figure(figsize=(25,10))
librosa.display.specshow(log_mel_spec, x_axis='time', y_axis='mel', sr=sr)
plt.colorbar(format = "%+2.f")
plt.show()

def create_mel_spectrograms():
    spectrogram_path = Path('D:/FakeAudios/FakeA/')  
    audio_path = Path('D:/FakeAudios/Fake/')  
    print(f'Processing Files')
    for audio_file in list(Path(audio_path).glob('*.wav')):
        print(str(audio_file))
        print("jafi")
        scale, sr = librosa.load(str(audio_file))
        mel_spectrogram = librosa.feature.melspectrogram(scale, sr=sr, n_fft=1000, hop_length=256, n_mels=10)
        log_mel_spec = librosa.power_to_db(mel_spectrogram)
        fig = plt.figure(figsize=[20,10])
        ax = fig.add_subplot(111)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.set_frame_on(False)
        librosa.display.specshow(log_mel_spec, x_axis='time', y_axis='mel', sr=sr)
        plt.colorbar(format = "%+2.f")
        filename  = spectrogram_path/Path(audio_file).name.replace('.wav','.png')
        plt.show()
        plt.savefig(filename, dpi=400, bbox_inches='tight',pad_inches=0)
        plt.close('all')

sr, sample = librosa.load("D:/FakeAudios/Fake/sample7.wav")

create_mel_spectrograms()

import os
import cv2
import random
data_path = Path('D:/FakeAudios/Data/')
spectrogram_path = Path('D:/FakeAudios/FakeA/')

IMG_SIZE = 30

DATADIR = 'D:/FakeAudios/'

CATEGORIES = ['FakeA', 'RealA']

for category in CATEGORIES :
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)

training_data = []

def create_training_data():
    for category in CATEGORIES :
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try :
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass

create_training_data()

random.shuffle(training_data)

X = [] #features
y = [] #labels

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X)
y = np.asarray(y)

X.shape

X.shape

y.shape

import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D

model = tf.keras.models.Sequential([
    Conv2D(16, (3,3), activation='relu', input_shape = (30, 30, 4)),
    MaxPooling2D(2,2),
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    
   
    Flatten(),
    Dense(1024, activation = 'relu'),
    Dense(1, activation = 'sigmoid')
])

model.summary()

from tensorflow.keras.optimizers import RMSprop

model.compile(optimizer = RMSprop(learning_rate=0.001),
              loss = 'binary_crossentropy',
              metrics = ['acc'])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model.fit(X_train, y_train, epochs = 10)

score = model.evaluate(X_test, y_test, verbose=0)

print(score)

X_test.shape

y_test[1]

binary_ypred = model.predict(X_test[1])

from sklearn.metrics import fbeta_score

print('f1_score of prediction using scikit-learn f1_score  is {}'.format(fbeta_score(y_test, binary_ypred, beta=1)))
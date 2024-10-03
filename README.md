# Deep-Fake-Audio-Generation-and-Detection

## Introduction

Audio signals can be represented visually as spectrograms, which depict how the frequency content of the signal varies over time. This project processes WAV audio files, generates Mel spectrograms, and utilizes a CNN to classify them into predefined categories.

## Requirements

To run this project, you will need the following Python libraries:

- `numpy`
- `librosa`
- `opencv-python`
- `matplotlib`
- `tensorflow`
- `scikit-learn`
- `pathlib`

You can install these libraries using pip:

pip install numpy librosa opencv-python matplotlib tensorflow scikit-learn

Next, run the generation.py which will generate fake audios by taking any audio file (format .wav). After this, run the detection part to detect the fake audios.

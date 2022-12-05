import scipy
import streamlit as st
import os
import pandas as pd

import h5py

from extract_hdf5 import extract_data_from_hdf5
from spectrogram import plot_spectrograms

st.markdown("# Select your new recording")
uploaded_file = st.file_uploader("Pick a HDF5 file!", type='hdf5', key="recording1")

dataFile = h5py.File(uploaded_file, 'r')
df = list(dataFile.keys())[0]
st.markdown(df)
st.markdown(dataFile[df])

for key in dataFile[df].keys():
    st.markdown(key)


st.markdown(dataFile[df]['frequency_Hz'])

for key in dataFile[df]['L1'].keys():
    st.markdown(key)

st.markdown(dataFile[df]['H1']['SFTs'])
st.markdown(dataFile[df]['H1']['timestamps_GPS'])

st.table(data=dataFile[df]['frequency_Hz'])

if uploaded_file is not None:
    # We generate byte data from the uploaded sample 1 to store locally
    data = extract_data_from_hdf5(uploaded_file.name)

    plot_spectrograms(data)

    if os.path.exists('cache/sample1.wav'):
        pass
    else:
        with open('cache/sample1.wav', mode='bx') as f:
            f.write(bytes_data)

    # Read the .wav file
    sample_rate, data = wavfile.read('cache/sample1.wav')

    st.markdown('## Check out the sample!')
    audio_file = open("cache/sample1.wav", 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')

    # Spectrogram of First sample, First channel
    sample_freq_fs_fc, segment_time_fs_fc, spec_data_fs_fc = scipy.signal.spectrogram(data[:, 0], sample_rate)

    # Spectrogram of First sample, Second channel
    sample_freq_fs_sc, segment_time_fs_sc, spec_data_fs_sc = scipy.signal.spectrogram(data[:, 1], sample_rate)

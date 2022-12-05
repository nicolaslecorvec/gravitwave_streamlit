import scipy
import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import h5py

from extract_hdf5 import extract_data_from_hdf5
from spectrogram import plot_spectrograms
from wave import mywave

st.markdown("# Select your new recording")
uploaded_file = st.file_uploader("Pick a HDF5 file!", type='hdf5', key="recording1")

if uploaded_file is not None:
    # We generate byte data from the uploaded sample 1 to store locally
    data = extract_data_from_hdf5(uploaded_file)
    import time

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f"The AI analyzes your file... {i+1}")
        bar.progress(i + 1)
        time.sleep(0.07)

    st.markdown("## % chance that your data is true")
    st.markdown("67,8%")


    st.markdown("## Visual analysis of your data:")
    st.markdown("### Spectogram analysis")

    plot_spectrograms(data)

    st.markdown("### Wave analysis")
    mywave(data)

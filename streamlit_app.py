import requests
import streamlit as st

from extract_hdf5 import extract_data_from_hdf5
from utils.spectrogram import plot_spectrograms
from utils.wave import mywave

st.markdown("# Looking for Continuous Gravitational Waves?")

st.markdown("## Select your new recording")
uploaded_file = st.file_uploader("Pick a HDF5 file!", type='hdf5', key="recording1")
url = "https://gravitwave-53od7qupsq-ew.a.run.app/predict_image"
#url = 'http://localhost:8000/predict_image'

if uploaded_file is not None:
    # We generate byte data from the uploaded sample 1 to store locally
    files = {"hdf5_file":uploaded_file}

    try:
        r = requests.post(url, files=files)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    result = r.json()

    if result["prediction"] > 0.60:
        st.success(f'This is a pretty good news ! You have a score of {result["prediction"]}', icon="✅")
    else :
        st.error(f'Bad news ! Try an another file, your score is only {result["prediction"]}', icon="🚨")

    #st.write(result["prediction"])


    data = extract_data_from_hdf5(uploaded_file.name)

    st.markdown("## Visual analysis of your data:")
    st.markdown("### Spectrogram visualization")

    plot_spectrograms(data)

    st.markdown("### Frequency visualization")
    mywave(data)

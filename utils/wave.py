import matplotlib.pyplot as plt
import streamlit as st
from scipy.signal import istft
from scipy import signal


def mywave(data_s):

    amp1 = data_s['L1_SFTs_amplitudes']
    amp2 = data_s['H1_SFTs_amplitudes']
    f1 = data_s['freq']
    f_m1 = sum(f1)/len(f1)
    #st.write('Mean of label 1 signal frequency is {}'.format(f_m1))
    _, xrec1 = signal.istft(amp1, f_m1)
    xrec1_r = signal.resample(xrec1, 200)

    _, xrec2 = signal.istft(amp2, f_m1)
    xrec2_r = signal.resample(xrec2, 200)

    fig = plt.figure(figsize=(20,10))

    plt.subplot(1, 2, 1)
    plt.suptitle('Signals in Time Domain', fontsize=10)
    plt.ylabel('Signal', fontsize=16)
    plt.xlabel('Time', fontsize=16)

    plt.plot(xrec1_r, label='Label L1 signal')
    plt.plot(xrec2_r, label='Label H1 signal')
    plt.legend(loc='upper right')
    #face = misc.face(gray=True)
    #ax.imshow(face, cmap='gray')
    st.pyplot(fig)

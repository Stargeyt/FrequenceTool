import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft




def soundplot(data):
    Hn = fft.fft(data)
    Hn = abs(Hn.real) + abs(Hn.imag)
    freqs = fft.fftfreq(len(Hn), 1 / (22050))  # *2 for frequencies if stéreo i.e Hn has 2 data per sample
    volume = max(np.abs(Hn))

    if volume > 2000000:

        for i in range(len(Hn)):
            if Hn[i] > 0.1*volume:
                return abs(freqs[i])
            

    """idx = np.argmax(np.abs(Hn))  # find the peak
    if volume > 1000000:
        freq_in_hertz = abs(freqs[idx])
        #print(idx, freq_in_hertz, volume)
        return(freq_in_hertz)
    """





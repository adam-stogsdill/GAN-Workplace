import numpy as np
import librosa
import librosa.display
import os
import pandas
import matplotlib.pyplot
import midi2audio

def wav_to_spectogram(file_location):
    for i, file_name in enumerate(os.listdir(file_location)):
        file = os.path.join(file_location, file_name)
        y, sr = librosa.load(file)

        y = y[:10000]

        window_size = 1024
        window = np.hanning(window_size)
        stft  = librosa.core.spectrum.stft(y, n_fft=window_size, hop_length=512, window=window)
        out = 2 * np.abs(stft) / np.sum(window)

        from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

        fig = plt.Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        p = librosa.display.specshow(librosa.amplitude_to_db(out, ref=np.max), ax=ax, y_axis='log', x_axis='time')
        fig.savefig('spec'+str(i)+'.png')

def midi_to_wav(file_location):
    for i, file_name in enumerate(os.listdir(file_location)):
        file = os.path.join(file_location, file_name)
        FluidSynth().midi_to_audio(file, os.path.join(file_location, "wav", file_name[:-3] + '.wav'))

midi_to_wav("./data")
wav_to_spectogram("./data/wav")
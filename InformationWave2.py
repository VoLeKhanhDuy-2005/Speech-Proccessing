import soundfile as sf

data, samplerate = sf.read('trial.wav')

print(f'Sample rate: {samplerate} Hz')
print(f'Audio data shape: {data.shape}')
print(f'First 10 samples of audio data: {data[:10]}')
#-3.05175781e-05 -> 0xff

## so mẫu với file wav: 4 số 0 liên tiếp tính 1 số 0
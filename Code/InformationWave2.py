import wave

f = wave.open("Record/mix_violin_piano_01.wav")
metadata = f.getparams()
print(metadata)


# import soundfile as sf

# data, samplerate = sf.read('Record/mix_violin_piano_01.wav')

# print(f'Sample rate: {samplerate} Hz')
# print(f'Audio data shape: {data.shape}')
# print(f'First 10 samples of audio data: {data[:10]}')
# #-3.05175781e-05 -> 0xff
# ## so mẫu với file wav: 4 số 0 liên tiếp tính 1 số 0

# data_tmp = data[::2] # 2 mẫu lấy 1 mẫu

# Run cell
# # %%
# import numpy as np
# data = np.array([1,2,3,4,5,6,7,8,9,10])
# data_tmp = data[::2]
# print(data)
# print(data_tmp)
# # %%
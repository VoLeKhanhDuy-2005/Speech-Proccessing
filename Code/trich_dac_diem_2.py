import numpy as np
import librosa
import soundfile as sf

bat_dau = 95*16 # 1 ms -> 16 samples
ket_thuc = bat_dau + 400
data, fs = sf.read("Record/mix_03.wav", dtype="int16")
x = data[bat_dau: ket_thuc]
# Chuẩn hóa giữa -1 và 1
x = x.astype(np.float32)
x = x / 32768
# pre-emphasis
N = len(x)
y = np.zeros((N,), np.float32)
a = 0.9 # a = [0.9, ..., 1]
# a = 0.97
for n in range(0,N):
    if n == 0:
        y[n] = x[n] - a*x[n]
    else:
        y[n] = x[n] - a*x[n-1]
        
# Nhân với cửa sổ Hamming
w = np.zeros((N,), np.float32)        
for n in range(0, N):
    w[n] = 0.54 - 0.46*np.cos(2*np.pi*n/N)
x = y*w
    
pad_zeros = np.zeros((112,), np.float32)# padding 112 zeros
x = np.hstack((x, pad_zeros))
mel = librosa.feature.mfcc(y=y, sr=16000, n_mfcc=26)
L = len(mel)
print("L = ", L)
    
# sr = sample rate -> tần số lấy mẫu mặc định 22050Hz của librosa mfcc
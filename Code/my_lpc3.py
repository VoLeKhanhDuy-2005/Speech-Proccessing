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

# Nhân với cửa sổ Hamming
z = y*w

# Kiểm tra lại với lpc của librosa
# a_lib = librosa.lpc(y, order=12)
# print("lib a: ", a_lib)

# a1 = (R[1]*R[0] - R[1]*R[2])/(R[0]**2 - R[1]**2)
# print(a1)

# Tính hệ số tương quan tuyến tính
# Return [1, -a1, ..., -am]
a = librosa.lpc(z, order = 12)
a = -a
m = 18 # chạy for ngoài
p = 12 # chạy for trong
c =  np.zeros((19,), dtype=np.float32)

m = 1
while m <= p: # 1 <= m <= p
    c[m] = a[m]
    k = 1
    while k <= m - 1:
        c[m] = c[m] + (k/m)*c[k]*a[m-k]
        k += 1
    m += 1

m = p + 1
while m <= 18: # 18 >= m > p
    
    c[m] = 0.0
    k = 1
    while k <= m - 1:
        chi_so = m-k
        if m - k > p:
            temp = 0.0
        else:
            temp = a[m-k]
        c[m] = c[m] + (k/m)*c[k]*temp
        k += 1
    m += 1
print(c)
    
# https://librosa.org/doc/main/generated/librosa.lpc.html
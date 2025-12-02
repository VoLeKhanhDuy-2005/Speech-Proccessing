import soundfile as sf
import numpy as np
from sklearn.decomposition import PCA
from sklearn.decomposition import FastICA
import sounddevice as sd

x1, fs = sf.read("Record/mix_violin_piano_01.wav", dtype="int16")
L = len(x1)
x1 = x1.astype(np.float32)
x1 = x1/32768

x2, fs = sf.read("Record/mix_violin_piano_02.wav", dtype="int16")
#L2 = len(x2)
x2 = x2.astype(np.float32)
x2 = x2/32768

x = np.zeros((2, L), np.float32)
x[0, :] = x1
x[1, :] = x2

x = x.T
# m= np.mean(x, 0)
# x = x - m

# # Kiểm tra ma trận covariance
# C = np.matmul(x.T, x)
# C /= L
# print("C =")
# print(C)

# # Làm trắng
# pca = PCA(whiten=True)
# y = pca.fit_transform(x)

# # Kiểm tra ma trận covariance
# C = np.matmul(y.T, y)
# C /= L
# print("C sau khi làm trắng")
# print(C)

# Compute ICA
ica = FastICA(n_components=2, whiten="unit-variance")# variance: phương sai
s = ica.fit_transform(x)  # Reconstruct signals (tách thành tín hiệu ban đầu trước trộn)
s1 = s[:, 0]
s2 = s[:, 1]

# Chuẩn hóa [-1, 1]
min_s1 = min(s1)
s1 = s1/abs(min_s1)
sd.play(s1, 8000)
sd.wait()

max_s2 = max(s2)
s2 = s2/abs(max_s2)
# sd.play(s2, 8000)
# sd.wait()
pass 

# REF
# https://sound-source-separation-python.readthedocs.io/en/latest/_notebooks/Getting-Started.html
# https://speechbrain.readthedocs.io/en/latest/tutorials/tasks/source-separation.html
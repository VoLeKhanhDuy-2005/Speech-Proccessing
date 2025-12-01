import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA


np.random.seed(100)
n_samples = 2000
time = np.linspace(0, 8, n_samples) # time = Chu kỳ

s1 = np.sin(2 * time)  # Signal 1 : sinusoidal signal (sóng hình sin)
s2 = np.sign(np.sin(3 * time))  # Signal 2 : square signal
s3 = signal.sawtooth(2 * np.pi * time)  # Signal 3: saw tooth signal (sóng răng cưa)

S = np.zeros((3, n_samples), dtype= np.float64)
S[0, :] = s1
S[1, :] = s2
S[2, :] = s3

S = S.T # mat 2000 x 3
S = S + 0.2 * np.random.normal(size=S.shape) # Add noise (gây nhiễu)
# normal/Gauss/Student -> phân phối chuẩn
# 0.2 là độ lệch chuẩn
# 0.0 là trung bình (mặc định)

# Chuẩn hóa bằng cách chia cho độ lệch chuẩn (STD)
S = S / S.std(axis=0)

# m = np.mean(S, axis=0)
# print(m)

# Mix data
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # Mixing matrix (random)
X = np.matmul(S, A.T)

# Compute ICA
ica = FastICA(n_components=3, whiten="arbitrary-variance")
R = ica.fit_transform(X)  # Reconstruct signals (tách thành tín hiệu ban đầu trước trộn)

plt.plot(time, R[:, 0])
# plt.plot(time, R[:, 1])
# plt.plot(time, R[:, 2])
plt.show()


# REF
# Blind source separation using FastICA, https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html#sphx-glr-auto-examples-decomposition-plot-ica-blind-source-separation-py
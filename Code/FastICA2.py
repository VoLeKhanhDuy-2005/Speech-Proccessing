from sklearn.datasets import load_digits # mnist dataset
from sklearn.decomposition import FastICA
import numpy as np
import matplotlib.pyplot as plt
X, y = load_digits(return_X_y=True)
m = np.mean(X, 0)# axis=0
X = X - m
m = np.mean(X, 0)
# print(m)
# for i in range(0, 64):
#     print("%2d = %10.2f" % (i, m[i]))
plt.plot(X[0, :], 25)
plt.show()
# C = np.matmul(X.T, X)
# C = C/64 #64=8x8
# print(C[0:3, 0:3])

# librosa, torch, speechbrain

pass
# REF
# https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html
# https://speechbrain.readthedocs.io/en/latest/tutorials/tasks/source-separation.html
# BTVN: Chay thu code
# https://speechbrain.readthedocs.io/en/latest/tutorials/tasks/source-separation.html
# Mix source
# %%capture
# !wget https://www.dropbox.com/sh/07vwpwru6qo6yhf/AADx5I8oV0IdekCf80MSkxMia/mixture_0.wav
# !wget https://www.dropbox.com/sh/07vwpwru6qo6yhf/AAAZI7ZezKyHFGPdus6hn2v_a/mixture_1.wav
# !wget https://www.dropbox.com/sh/07vwpwru6qo6yhf/AACh4Yy4H-Ii2I0mr_b1lQdXa/mixture_2.wav
# !wget https://www.dropbox.com/sh/07vwpwru6qo6yhf/AAAenTlEsoj1-AGbCxeJfMHoa/mixture_3.wav
# !wget https://www.dropbox.com/sh/07vwpwru6qo6yhf/AAC-awQo-9NFVVULuVwaHKKWa/source1_0.wav
# !wget https://www.dropbox.com/sh/07vwpwru6qo6yhf/AABVKWtdVhXZE6Voq1I_c6g5a/source1_1.wav
# !wget https://www.dropbox.com/sh/07vwpwru6qo6yhf/AAC9EfjTTwL0dscH16waP9s-a/source1_2.wav
# !wget https://www.dropbox.com/sh/07vwpwru6qo6yhf/AAC5Ozb4rS9qby268JSIy5Uwa/source1_3.wav
# !wget https://www.dropbox.com/sh/07vwpwru6qo6yhf/AABlonG910Ms2l-rTN5ct3Oka/source2_0.wav
# !wget https://www.dropbox.com/sh/07vwpwru6qo6yhf/AACDOqEgyXIeA2r1Rkf7VgQTa/source2_1.wav
# !wget https://www.dropbox.com/sh/07vwpwru6qo6yhf/AACTYGAG0LOh6HvxpVYoqO_Da/source2_2.wav
# !wget https://www.dropbox.com/sh/07vwpwru6qo6yhf/AACPmq-ZJNzfh4bnO34_8mfAa/source2_3.wav
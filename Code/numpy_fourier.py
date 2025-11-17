import numpy as np
x = np.array([i for i in range(1,17)], dtype = np.float32)
N = len(x)

# Biến đổi DFT
X = np.fft.fft(x, N)
#print(X)
print(X.real)
print(X.imag)

print("Spectrum:")
S = np.sqrt(X.real**2 + X.imag**2)
for k in range(0, len(S)):
    print('%2d --> %10.2f' % (k, S[k]))
    
# Biến đổi IDFT
x_original = np.fft.ifft(X, N) # i: inverse
print(x_original.real)
print(x_original.imag)
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(100)
n = 7200
x = rng.normal(size=(n, 2)) #rng.normal là phân phối chuẩn (gaussian distribution)

#m = np.mean(x, axis=0)
# x1 = x[:, 0]
# x2 = x[:, 1]
_, _, Vh = np.linalg.svd(x, full_matrices=True) #U, S, Vh
Vt = Vh.T
y = np.matmul(x, Vt)
print("y = ", y)

# plt.hist(x1, 51)
# plt.show()

# Kiểm tra ma trận covariance
# C = np.zeros((2, 2), np.float32)
# for i in range(0, n):
#     C[0, 0] = C[0, 0] + x[i, 0] * x[i, 0]
#     C[0, 1] = C[0, 1] + x[i, 0] * x[i, 1]
#     C[1, 0] = C[1, 0] + x[i, 1] * x[i, 0]
#     C[1, 1] = C[1, 1] + x[i, 1] * x[i, 1]
# print("C = ")
# print(C)
Cx = np.matmul(x.T, x)
Cx /= n
print("Cx =")
print(Cx)

Cy = np.matmul(y.T, y)
Cy /= n
print("Cy =")
print(Cy)



# Có thể coi thêm
# A = np.sqrt(Vh[0, 0]**2 + Vh[0,1]**2) # độ dài các vecto = 1 + vecto trực giao (đôi một vuông góc) -> vecto trực chuẩn
# print(A)
# X_white = np.dot(U, Vh) # np.dot là phép tích vô hướng hai vecto: doc(a, b) = a . b = a1*b1 + a2*b2 + ... + an*bn
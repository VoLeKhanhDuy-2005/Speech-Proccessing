import numpy as np
from sklearn.decomposition import PCA
rng = np.random.default_rng(100)
n = 72000
x = rng.normal(size=(n, 2))
pca = PCA(whiten=True)
y = pca.fit_transform(x)

# Kiểm tra ma trận covariance
C = np.matmul(y.T, y)
C /= n
print("Cx =")
print(C)

# Làm trắng
pca = PCA(whiten=True)
y = pca.fit_transform(x)

# Kiểm tra ma trận covariance
C = np.matmul(y.T, y)
C /= n
print("Cy =")
print(C)

# Báo cáo: tại sao gỡ ra dữ liệu trộn lẫn được
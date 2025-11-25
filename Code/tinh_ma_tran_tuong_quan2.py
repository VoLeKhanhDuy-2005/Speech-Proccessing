import numpy as np

x = np.array([[1, 3], [5, 7], [9, 11]]) # là matrix, ko phải row -> xét (1, 3) là cột
print(x)

m = np.mean(x, axis=0) # tính trung bình theo hàng trong trường hợp này
print(m)

x = x - m
print(x)

# Tính mean -> xét trung bình cộng theo từng hàng lấy trừ theo hàng với giá trị vừa tính ra
# numpy và line algebra có hàng và cột ngược nhau
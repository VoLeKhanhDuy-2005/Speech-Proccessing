import numpy as np
f = 8000 # Tần số cao nhất -> Tần số lấy mẫu 8kHz (Ban đầu khoảng cách các bộ lọc không đều do tai người nghe)
m = 1127 * np.log(1 + f/700) # Độ dài của mel
print(m) # Vị trí của mel (ở đoạn cuối)
# n_filter = 6 # đỉnh của tam giác
n_filter = 28
d = m/(n_filter - 1)
print(d)
F = []
for i in range(n_filter):
    m = i * d# d - delta
    f  = 700 * (np.exp(m/1127)-1)
    F.append(f)
print(F)
L = len(F)
print(L)
# mục đích đổi về thang đo mel cho khoảng cách bằng nhau

# 0 -> 8000Hz
# 0 1 ... 256

# 256   8000Hz  -> i = f * 256 / 8000
# i     f
# print(256/8000*68.47927398669893)# = 2.1913367675743656 -> vị trí i = 2
# print(256/8000*143.65770649589132)# vị trí 4
# print(256/8000*7999.999999999999)# vị trí 8000

print(256/8000*6518.567380003728)
print(256/8000*7224.742027727618)
print(256/8000*7999.999999999999)# vị trí 8000
print(1/22)
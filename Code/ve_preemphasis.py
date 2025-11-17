import matplotlib.pyplot as plt
import numpy as np

Fmax = 5000 # Tần số tối đa trên trục x khi vẽ. Ở đây chọn 5000 Hz
n = 500 # 500 điểm mẫu dữ liệu tần số  muốn vẽ
f = np.linspace(0, Fmax, 500) # mảng tần số rời rạc từ 0 đến Fmax gồm 500 điểm
Fs = 10000 # tần số lấy mẫu (10000 mẫu)
Ts = 1/Fs # chu kỳ lấy mẫu (giây) — khoảng thời gian giữa hai mẫu liên tiếp
a = 0.98 # hệ số pre-emphasis (thường chọn khoảng 0.9–0.99)
H = np.sqrt(1 + a**2 - 2*a*np.cos(2*np.pi*f*Ts)) 
H = 20*np.log10(H) # đưa về db (chuyển biên độ tuyến tính sang decibel)

plt.plot(f, H)
plt.plot([0, 5000], [0, 0], 'r')
plt.xlabel('Hz')
plt.ylabel('|H(f)|\n(dB)')
plt.title('Frequency Response of Pre-emphasis Filter')
plt.show()

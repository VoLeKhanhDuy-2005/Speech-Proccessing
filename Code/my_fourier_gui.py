import tkinter as tk
import tkinter.filedialog as fd
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

class App(tk.Tk):
    def	__init__(self):
        super().__init__()
        self.title("Fourier GUI")
        self.data = None
        
        self.cvs_figure = tk.Canvas(self, width=600, height=300, relief=tk.SUNKEN, border=1)  
            
        lblf_upper = tk.LabelFrame(self)
        btn_open = tk.Button(lblf_upper, text ="Open", width = 8, command=self.btn_open_click)
        btn_cut = tk.Button(lblf_upper, text="Cut", width=8, command=self.btn_cut_click)
        btn_spectrum = tk.Button(lblf_upper, text="Spectrum", width=8, command=self.btn_spectrum_click)
        btn_open.grid(row=0, padx =5, pady=5)
        btn_cut.grid(row=1, padx=5, pady=5)
        btn_spectrum.grid(row=2, padx=5, pady=5)

        self.cvs_figure.grid(row=0, column=0, rowspan=2, padx=5, pady=5)# rowspan=2: cvs_figure sẽ được đặt bắt đầu ở hàng 0, cột 0 và chiếm luôn 2 hàng liền kề (hàng 0 và hàng 1).
        lblf_upper.grid(row=0, column=1, padx=5, pady=6, sticky=tk.N)# sticky N: dán lên phía bắc 
            
    def btn_open_click(self):
        filetypes = (("Wave files", "*.wav"),)
        filename = fd.askopenfilename(title="Open wave file", filetypes=filetypes)
        if filename:
            print(filename)      
        self.data, fs = sf.read(filename, dtype='int16')
        L = len(self.data) # số lượng mẫu
        N = L // 600 # 600 là chiều dài canvas -> N: số mẫu trên 1 px trong canvas (600px đầu tiên)
        lst_values = []
        for i in range(1, N+1):
            s = "%10d" % i
            lst_values.append(s)
        self.cvs_figure.delete(tk.ALL)
        
        yc = 150 # Điểm gốc tung độ ở giữa canvas
        for x in range(0, 599):
            a1 = int(self.data[x*N])            
            y1 = int((a1 + 32768)*300/65535) - 150 #y = (x + 32768)*300//65535 - 150         
            a2 = int(self.data[(x+1)*N])# i+1 mẫu kế bên        
            y2 = int((a2 + 32768)*300/65535) - 150            
            self.cvs_figure.create_line(x, yc - y1, x+1, yc - y2, fill="green")  
            
    def btn_cut_click(self):
        index = 23
        #index = 30 #chọn đoạn cắt thứ 30 -> đoạn đột biến (biên độ thay đổi rõ rệt)
        batDau = index * 600  # 600Hz
        ketThuc = (index + 1) * 600
        data_temp = self.data[batDau:ketThuc]
        self.cvs_figure.delete(tk.ALL)
        yc = 150 # Điểm gốc tung độ ở giữa canvas
        for x in range(0, 599):
            a1 = int(data_temp[x])            
            y1 = int((a1 + 32768)*300/65535) - 150 #y = (x + 32768)*300//65535 - 150         
            a2 = int(data_temp[(x+1)])# i+1 mẫu kế bên        
            y2 = int((a2 + 32768)*300/65535) - 150            
            self.cvs_figure.create_line(x, yc - y1, x+1, yc - y2, fill="green")  
            
    def btn_spectrum_click(self):
        # voice
        index = 23
        # index = 30 #chọn đoạn cắt thứ 30 -> đoạn đột biến (biên độ thay đổi rõ rệt)
        batDau = index * 600  # 600Hz
        ketThuc = (index + 1) * 600
        x = self.data[batDau:ketThuc]
        N = 16000 # N = len(x)
        x = x / 32768  # Chuẩn hóa biên độ về [-1, 1] -> 32768 là giá trị biên độ lớn nhất của tín hiệu 16-bit
        x = x.astype(np.float32)    
        
        X = np.fft.fft(x, N)  # Phép biến đổi Fourier nhanh (FFT)
        S = np.sqrt(X.real**2 + X.imag**2)  # Biên độ phổ
        S = 20*np.log10(S)#S = 20*np.log10(S + 1)  # Chuyển đổi sang thang dB: db = 20 * log10(K), K = amplitude, + 1 lấy số liệu dương; 20: độ khuyech đại - optional
        S = S[:N//2+1] # lấy phần đối xứng của S
        print('S =', S)
        plt.plot(S)
        plt.show()
            
    def btn_spectrum_pre_emphasis_click(self):
        # no voice
        index = 23
        # index = 30 #chọn đoạn cắt thứ 30 -> đoạn đột biến (biên độ thay đổi rõ rệt)
        batDau = index * 600  # 600Hz
        ketThuc = (index + 1) * 600 # bat dau + 600
        x = self.data[batDau:ketThuc]
        N = 16000 # N = len(x)
        x = x / 32768  # Chuẩn hóa biên độ về [-1, 1] -> 32768 là giá trị biên độ lớn nhất của tín hiệu 16-bit
        x = x.astype(np.float32)
        L = len(x)
        y = np.zeros((L,), dtype=np.float32)
        a = 0.98
        for i in range(1, L):
            if i == 0:
                y[i] = x[i] - a*x[i]
            else:
                y[i] = x[i] - a*x[i-1]
            
        
        Y = np.fft.fft(y, N)  # Phép biến đổi Fourier nhanh (FFT)
        S = np.sqrt(Y.real**2 + Y.imag**2)  # Biên độ phổ
        S = 20*np.log10(S)  # Chuyển đổi sang thang dB: db = 20 * log10(K), K = amplitude, + 1 lấy số liệu dương; 20: độ khuyech đại - optional
        S = S[:N//2+1] # lấy phần đối xứng của S
        print('S =', S)
        plt.plot(S)
        plt.show()
        
    

if __name__	==	"__main__":
    app	= App()
    app.mainloop()
    
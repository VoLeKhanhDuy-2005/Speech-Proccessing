import tkinter as tk
import tkinter.filedialog as fd
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

class App(tk.Tk):
    def	__init__(self):
        super().__init__()
        self.title("Spectrogram")
        self.data = None
        
        self.cvs_figure = tk.Canvas(self, width=600, height=600, relief=tk.SUNKEN, border=1)  
            
        lblf_upper = tk.LabelFrame(self)
        btn_open = tk.Button(lblf_upper, text ="Open", width=10, command=self.btn_open_click)
        btn_cut = tk.Button(lblf_upper, text="Cut", width=10, command=self.btn_cut_click)
        btn_spectrogram = tk.Button(lblf_upper, text="Spectrogram", width=10, command=self.btn_spectrogram_click)
        btn_open.grid(row=0, padx =5, pady=5)
        btn_cut.grid(row=1, padx=5, pady=5)
        btn_spectrogram.grid(row=2, padx=5, pady=5)

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
        
        yc = 450 # Điểm gốc tung độ ở giữa canvas
        for x in range(0, 599):
            a1 = int(self.data[x*N])            
            y1 = int((a1 + 32768)*300/65535) - 150 #y = (x + 32768)*300//65535 - 150         
            a2 = int(self.data[(x+1)*N])# i+1 mẫu kế bên        
            y2 = int((a2 + 32768)*300/65535) - 150            
            self.cvs_figure.create_line(x, yc - y1, x+1, yc - y2, fill="green")  
            
    def btn_cut_click(self):
        index_bat_dau = 23#chọn đoạn cắt thứ 23 -> đoạn đột biến (biên độ thay đổi rõ rệt)
        bat_dau = index_bat_dau * 600  # 600Hz
        index_ket_thuc = 29 #31
        ket_thuc = index_ket_thuc * 600
        data_temp = self.data[bat_dau:ket_thuc]
        L = len(data_temp) # số lượng mẫu
        N = L // 600 # 600 là chiều dài canvas -> N: số mẫu trên 1 px trong canvas (600px đầu tiên)
        print('L =', L)
        print('N =', N)
        self.cvs_figure.delete(tk.ALL)
        
        yc = 450 # Điểm gốc tung độ ở giữa canvas
        for x in range(0, 599):
            a1 = int(data_temp[x*N])            
            y1 = int((a1 + 32768)*300/65535) - 150 #y = (x + 32768)*300//65535 - 150         
            a2 = int(data_temp[(x+1)*N])# i+1 mẫu kế bên        
            y2 = int((a2 + 32768)*300/65535) - 150            
            self.cvs_figure.create_line(x, yc - y1, x+1, yc - y2, fill="green")  
            
    def btn_spectrogram_click(self):
        index_bat_dau = 23#chọn đoạn cắt thứ 23 -> đoạn đột biến (biên độ thay đổi rõ rệt)
        bat_dau = index_bat_dau * 600  # 600Hz
        index_ket_thuc = 29
        ket_thuc = index_ket_thuc * 600
        data_temp = self.data[bat_dau:ket_thuc]
        data_temp = data_temp.astype(np.float32)
        data_temp = data_temp / 32768  # Chuẩn hóa biên độ về [-1, 1]
        L = len(data_temp) # số lượng mẫu
        N = L // 600 # 600 là chiều dài canvas -> N: số mẫu trên 1 px trong canvas (600px đầu tiên)
        pad_zeros = np.zeros((112,), dtype=np.float32) # trượt 400 mẫu + thêm 112 số 0 để đủ 512 mẫu = 2^n
        yc = 300 # Điểm gốc tung độ ở giữa canvas
        for x in range(0, 600):
            a = x*N
            b = x*N+400
            frame = data_temp[a:b]
            y = np.hstack((frame, pad_zeros))
            Y = np.fft.fft(y, 512)
            scale = 1.0
            S = scale * np.sqrt(Y.real**2 + Y.imag**2)
            S = np.clip(S, 0.001, 400)# np.clip > 400 -> 400, < 0.001 -> 0.001; 
            S = 20*np.log10(S)# 20*log0.001 = -60, log400 = 52.04
            dark = -(S-52)/112*255
            dark = dark[:257]
            dark = dark.astype(np.int32)
            for k in range(0, 257):
                mau = "#%02X%02X%02X" % (dark[k], dark[k], dark[k])
                self.cvs_figure.create_line(x, yc - k, x, yc - (k+1), fill=mau)
            pass
        

if __name__	==	"__main__":
    app	= App()
    app.mainloop()
    
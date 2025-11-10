import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msb

import sounddevice as sd
import queue
import soundfile as sf
import threading

class App(tk.Tk):
    def	__init__(self):
        super().__init__()
        self.title("Speech Signal Processing")
        
        #Create a queue to contain the audio data
        self.q = queue.Queue()
        #Declare variables and initialise them
        self.recording = False
        self.file_exists = False
        self.data = None
        self.index = tk.IntVar()
        
        self.cvs_figure = tk.Canvas(self, width=600, height=300, relief=tk.SUNKEN, border=1)  
            
        lblf_upper = tk.LabelFrame(self)
        btn_record = tk.Button(lblf_upper, text="Record", width=8, command=lambda m=1:self.threading_rec(m))
        btn_stop = tk.Button(lblf_upper, text="Stop", width=8, command=lambda m=2:self.threading_rec(m))
        btn_play = tk.Button(lblf_upper, text="Play", width=8, command=lambda m=3:self.threading_rec(m))
        btn_record.grid(row=0, padx=5, pady=5)
        btn_stop.grid(row=1, padx=5, pady=5)
        btn_play.grid(row=2, padx=5, pady=5)
        
        lblf_lower = tk.LabelFrame(self)
        self.factor_zoom = tk.StringVar()
        self.cbo_zoom = ttk.Combobox(lblf_lower, width = 7, textvariable = self.factor_zoom, state='disabled')
        self.cbo_zoom["values"] = None
        self.cbo_zoom.bind("<<ComboboxSelected>>", self.factor_zoom_changed)
        self.cbo_zoom["state"] = "readonly"
        btn_next = tk.Button(lblf_lower, text="Next", width=8, command=self.btn_next_click)  
        btn_prev = tk.Button(lblf_lower, text="Prev", width=8)

        self.cbo_zoom.grid(row=0, padx=5, pady=5)
        btn_next.grid(row=1, padx=5, pady=5)
        btn_prev.grid(row=2, padx=5, pady=5)
        
        self.cvs_figure.grid(row=0, column=0, rowspan=2, padx=5, pady=5)# rowspan=2: cvs_figure sẽ được đặt bắt đầu ở hàng 0, cột 0 và chiếm luôn 2 hàng liền kề (hàng 0 và hàng 1).
        lblf_upper.grid(row=0, column=1, padx=5, pady=6, sticky=tk.N)# sticky N: dán lên phía bắc 
        lblf_lower.grid(row=1, column=1, padx=5, pady=6, sticky=tk.S)
        self.index.set(0)
    
    def factor_zoom_changed(self, event):
        factor_zoom = self.factor_zoom.get()
        print('factor_zoom ', factor_zoom)
    
    #Fit data into queue
    def callback(self, indata, frames, time, status):
        self.q.put(indata.copy())
        
    #Recording function
    def record_audio(self):
        #Set to True to record
        self.recording= True   
        #Create a file to save the audio
        msb.showinfo(title="Recording Speech", message="Speak into the mic")
        with sf.SoundFile("trial.wav", mode='w', samplerate=16000,
                            channels=1) as file:#samplerate=44100 <-> 44.1kHz
        #Create an input stream to record audio without a preset time
                with sd.InputStream(samplerate=16000, channels=1, callback=self.callback):
                    while self.recording == True:
                        #Set the variable to True to allow playing the audio later
                        self.file_exists =True
                        #write into file
                        file.write(self.q.get())
        
    #Functions to play, stop and record audio
    #The recording is done as a thread to prevent it being the main process
    def threading_rec(self, x):
        if x == 1:
            #If recording is selected, then the thread is activated
            t1=threading.Thread(target= self.record_audio)
            t1.start()
        elif x == 2:
            #To stop, set the flag to false
            self.recording = False
            msb.showinfo(title="Recording", message="Recording finished")
            self.data, fs = sf.read('trial.wav', dtype='int16')
            L = len(self.data) # số lượng mẫu
            N = L // 600 # 600 là chiều dài canvas -> N: số mẫu trên 1 px trong canvas (600px đầu tiên)
            lst_values = []
            for i in range(1, N+1):
                s = "%10d" % i
                lst_values.append(s)
            self.cbo_zoom["values"] = lst_values
            self.cvs_figure.delete(tk.ALL)
            for i in range(0, 599):
                x1 = int(self.data[i*N])            
                y1 = int((x1 + 32768)*300/65535) - 150 #y = (x + 32768)*300//65535 - 150         
                x2 = int(self.data[(i+1)*N])# i+1 mẫu kế bên        
                y2 = int((x2 + 32768)*300/65535) - 150            
                self.cvs_figure.create_line(i, 150 - y1, i+1, 150 - y2, fill="green")         
            
        elif x == 3:
            #To play a recording, it must exist.
            if self.file_exists:
                #Read the recording if it exists and play it
                data, fs = sf.read("trial.wav", dtype='int16') 
                sd.play(data,fs)
                sd.wait()
            else:
                #Display and error if none is found
                msb.showerror(title="Error", message="Record something to play")
                
    def btn_zoom_click(self):
        L = len(self.data) # số lượng mẫu
        N = L // 600 # 600 là chiều dài canvas -> N: số mẫu trên 1 px trong canvas # next -> đi qua đoạn 600px tiếp theo
        self.cvs_figure.delete(tk.ALL)
        i = self.index.get()
        for x in range(0, 599):
            a1 = int(self.data[i*600 + x])     # a là biên độ       
            y1 = int((a1 + 32768)*300/65535) - 150 #y = (x + 32768)*300//65535 - 150
            a2 = int(self.data[i*600 + (x+1)])     # a là biên độ       
            y2 = int((a2 + 32768)*300/65535) - 150
            self.cvs_figure.create_line(x, 150-y1, x+1, 150-y2, fill="green")
            
    def btn_next_click(self):
        L = len(self.data) # số lượng mẫu
        N = L // 600 # 600 là chiều dài canvas -> N: số mẫu trên 1 px trong canvas # next -> đi qua đoạn 600px tiếp theo
        self.cvs_figure.delete(tk.ALL)
        i = self.index.get()
        i += 1
        self.index.set(i)
        print('i', i, 'self.index', self.index.get())
        
        for x in range(0, 599):
            a1 = int(self.data[i*600 + x])     # a là biên độ       
            y1 = int((a1 + 32768)*300/65535) - 150 #y = (x + 32768)*300//65535 - 150
            a2 = int(self.data[i*600 + x+1])     # a là biên độ       
            y2 = int((a2 + 32768)*300/65535) - 150
            self.cvs_figure.create_line(x, 150-y1, x+1, 150-y2, fill="green")

if __name__	==	"__main__":
    app	=	App()
    app.mainloop()
    
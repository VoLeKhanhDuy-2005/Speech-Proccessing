import tkinter as tk
from tkinter import messagebox as msb
import sounddevice as sd
import queue
import soundfile as sf
import threading

class App(tk.Tk):
    def	__init__(self):
        super().__init__()
        self.title("Speech Recording")
        
        #Create a queue to contain the audio data
        self.q = queue.Queue()
        #Declare variables and initialise them
        self.recording = False
        self.file_exists = False    
        
        cvs_figure = tk.Canvas(self, width=600, height=300, relief=tk.SUNKEN, border=1)  
        
        lblf_upper = tk.LabelFrame(self)
        btn_record = tk.Button(lblf_upper, text="Record", width=8, command=lambda m=1:self.threading_rec(m))
        btn_stop = tk.Button(lblf_upper, text="Stop", width=8, command=lambda m=2:self.threading_rec(m))
        btn_play = tk.Button(lblf_upper, text="Play", width=8, command=lambda m=3:self.threading_rec(m))
        btn_record.grid(row=0, padx=5, pady=5)
        btn_stop.grid(row=1, padx=5, pady=5)
        btn_play.grid(row=2, padx=5, pady=5)
        
        lblf_lower = tk.LabelFrame(self)
        btn_view = tk.Button(lblf_lower, text="View", width=8)
        btn_next = tk.Button(lblf_lower, text="Next", width=8)
        btn_prev = tk.Button(lblf_lower, text="Prev", width=8)
        btn_view.grid(row=0, padx=5, pady=5)
        btn_next.grid(row=1, padx=5, pady=5)
        btn_prev.grid(row=2, padx=5, pady=5)
        
        cvs_figure.grid(row=0, column=0, rowspan=2, padx=5, pady=5) 
        # rowspan=2: cvs_figure sẽ được đặt bắt đầu ở hàng 0, cột 0 và chiếm luôn 2 hàng liền kề (hàng 0 và hàng 1).
        lblf_upper.grid(row=0, column=1, padx=5, pady=6, sticky=tk.N) # sticky N: dán lên phía bắc 
        lblf_lower.grid(row=1, column=1, padx=5, pady=6, sticky=tk.S)
    
    #Fit data into queue
    def callback(self, indata, frames, time, status):
        self.q.put(indata.copy())
        
    #Recording function
    def record_audio(self):
        #Set to True to record
        self.recording= True   
        global file_exists 
        #Create a file to save the audio
        msb.showinfo(title="Recording Speech", message="Speak into the mic")
        with sf.SoundFile("trial.wav", mode='w', samplerate=44100,
                            channels=2) as file:#samplerate=44100 <-> 44.1kHz
        #Create an input stream to record audio without a preset time
                with sd.InputStream(samplerate=44100, channels=2, callback=self.callback):
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
        elif x == 3:
            #To play a recording, it must exist.
            if self.file_exists:
                #Read the recording if it exists and play it
                data, fs = sf.read("trial.wav", dtype='float32') 
                sd.play(data,fs)
                sd.wait()
            else:
                #Display and error if none is found
                msb.showerror(title="Error", message="Record something to play")

if __name__	==	"__main__":
    app	=	App()
    app.mainloop()
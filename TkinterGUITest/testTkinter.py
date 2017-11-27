import Tkinter as tk
import time

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(background = 'black')
        self.clk = tk.Label(self.root, text = "", font = ('Courier', 50), background = 'black', foreground = 'white')
        self.clk.pack(side = 'right')
        self.updateClk()
        self.root.mainloop()

    def updateClk(self):
        self.timeString = time.strftime('%H:%M:%S')
        self.clk.configure(text=self.timeString)
        self.root.after(1000, lambda: self.updateClk())

    def updateWeather():
        

gui = GUI()

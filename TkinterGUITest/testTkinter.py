import Tkinter as tk
import time, weatherClient

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(background = 'black')
        wc = weatherClient.Client('localhost', 22, 'localhost', 23)
        weatherString = wc.sendReceive('summary')
        self.clockLabel = tk.Label(self.root, text = "", font = ('Courier', 50), background = 'black', foreground = 'white')
        self.weatherLabel = tk.Label(self.root, text = weatherString, font = ('Courier', 40), background = 'black', foreground = 'white')
        self.clockLabel.pack(side = 'right')
        self.weatherLabel.pack(side = 'left')
        self.weatherLabel
        self.updateclockLabel()
        self.root.mainloop()

    def updateclockLabel(self):
        timeString = time.strftime('%H:%M:%S')
        self.clockLabel.configure(text=timeString)
        self.root.after(1000, lambda: self.updateclockLabel())

    def updateWeather(self):
        pass;



gui = GUI()

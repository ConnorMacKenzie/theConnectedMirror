import Tkinter as tk

font = "Nidus Sans"
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background = 'black')
W = tk.StringVar()
N = tk.StringVar()
clockLabel = tk.Label(root, text = "", font = (font, 50), background = 'black', foreground = 'white')
weatherLabel = tk.Label(root, textvariable = W, font = (font, 40), background = 'black', foreground = 'white')
newsLabel = tk.Label(root, textvariable = N, font = (font, 10), background = 'black', foreground = 'white')
clockLabel.pack(side = 'top')
weatherLabel.pack(side = 'left')
newsLabel.pack(side = 'right')
root.mainloop()

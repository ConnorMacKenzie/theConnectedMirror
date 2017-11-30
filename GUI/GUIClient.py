import Tkinter as tk
import time, socket, sys, time, json, GUIServer

class Client():

    def __init__(self, local = 'localhost', localport = 22, remote = 'localhost', remoteport = 23):

        #initializes socket addresses and ports
        self.localName = local
        self.localPort = localport
        self.remoteName = remote
        self.remotePort = remoteport

        #initializes sockets
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.localAddress = (self.localName, self.localPort)
        self.remoteAddress = (self.remoteName, self.remotePort)
        self.s.bind(self.localAddress)

    def recieveData(self, field):

        #print ("Enter non-null weather pull request: ")
        #sets the string to be sent as the next line in the terminal

        if not len(field):
            break
        #sends the next line in the terminal to the server socket
        self.s.sendto(field.encode('utf-8'), self.remoteAddress)

        #receives data from server and stores in buf
        buf, address = self.s.recvfrom(2048)
        if not len(buf):
            break
        #decodes utf-8 data to store json string
        jsonData = buf.decode('utf-8')

        #decodes json string into python dictionary to enable manipulation and access
        data = json.loads(jsonData)

        return data


class GUI():

    def __init__(self):

        server = GUIServer.serv()
        server.start()
        font = "Courier"
        #font = "Nidus Sans"
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(background = 'black')
        self.client = Client()
        self.clockLabel = tk.Label(self.root, text = "", font = (font, 50), background = 'black', foreground = 'white')
        self.weatherLabel = tk.Label(self.root, text = "", font = (font, 40), background = 'black', foreground = 'white')
        self.newsLabel = tk.Label(self.root, text = "", font = (font, 40), background = 'black', foreground = 'white')
        self.clockLabel.pack(side = 'right')
        self.weatherLabel.pack(side = 'left')
        self.newsLabel.pack(side = "top")
        self.updateAll()
        self.root.mainloop()

    def updateClock(self):
        timeString = time.strftime('%H:%M:%S')
        self.clockLabel.configure(text=timeString)
        self.root.after(1000, lambda: self.updateclockLabel())

    def updateWeather(self):
        weatherData = self.client.recieveData('weather')
        weatherString = weatherData.get('summary')
        self.weatherLabel.configure(text = weatherString)

    def updateNews(self):
        newsData = self.client.recieveData('news')
        newsString = weatherData.get('title')
        self.newsLabel.configure(text = newsString)

    def updateAll(self):
        self.updateWeather()
        self.updateNews()
        self.root.after(1800000, lambda: self.updateAll())

gui = GUI()

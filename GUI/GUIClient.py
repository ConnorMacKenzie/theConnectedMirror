import Tkinter as tk
import time, socket, sys, time, json



class Client():

    def __init__(self, local = '10.0.0.52', localport = 51, remote = '10.0.0.52', remoteport = 50):

        #initializes socket addresses and ports
        self.localName = local
        self.localPort = localport
        self.remoteName = remote
        self.remotePort = remoteport

        #initializes sockets
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	self.localAddress = (self.localName, self.localPort)
        self.remoteAddress = (self.remoteName, self.remotePort)
        self.s.bind(self.localAddress)

    def recieveData(self, field):

        #print ("Enter non-null weather pull request: ")
        #sets the string to be sent as the next line in the terminal

        #sends the next line in the terminal to the server socket
        self.s.sendto(field.encode('utf-8'), self.remoteAddress)

        #receives data from server and stores in buf
        buf, address = self.s.recvfrom(100000)
        #decodes utf-8 data to store json string
        jsonData = buf.decode('utf-8')

        #decodes json string into python dictionary to enable manipulation and access
        data = json.loads(jsonData)

        return data

    def recieveStr(self):

        #print ("Enter non-null weather pull request: ")
        #sets the string to be sent as tself.server.start('localhost', 53, '10.0.0.51', 52)he next line in the terminal

        #sends the next line in the terminal to the server socket
        #self.s.sendto(field.encode('utf-8'), self.remoteAddress)

        #receives data from server and stores in buf
        buf, address = self.s.recvfrom(2048)
        #decodes utf-8 data to store json string
        data = buf.decode('utf-8')

        #decodes json string into python dictionary to enable manipulation and access
        #data = json.loads(jsonData)

        return data


class GUI():

    
    def startGUI(self):
	time.sleep(1)
        #font = "Courier"
        font = "Nidus Sans"
        self.isWeather = 1
        self.isNews = 1
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(background = 'black')
	self.client = Client()
	self.W = '.'
	self.N = '.'
	self.clockLabel = tk.Label(self.root, text = "", font = (font, 50), background = 'black', foreground = 'white')
	self.weatherLabel = tk.Label(self.root, text = self.W, font = (font, 40), background = 'black', foreground = 'white')
	self.newsLabel = tk.Label(self.root, text = self.N, font = (font, 10), background = 'black', foreground = 'white')
	self.clockLabel.pack(side = 'top')
	self.weatherLabel.pack(side = 'left')
	self.newsLabel.pack(side = 'right')
	self.updateAll()
	self.updateClock()
	self.modules()
	self.root.mainloop()

    def modules(self):
        modules = self.client.recieveData('modules')
        if modules.get('news') == 'off':
		self.newsOff()
	if modules.get('weather') == 'off':
		self.weatherOff()
	if modules.get('news') == 'on':
		self.updateNews()
	if modules.get('weather') == 'on':
		self.updateWeather()
	self.root.after(2000, lambda: self.modules())

    def newsOff(self):
	self.newsLabel.configure(text = ' ')

    def weatherOff(self):
	self.weatherLabel.configure(text = ' ')

    def updateClock(self):
        timeString = time.strftime('%H:%M')
        self.clockLabel.configure(text=timeString)
        self.root.after(60000, lambda: self.updateClock())

    def updateWeather(self):
        weatherData = self.client.recieveData('weather')
	weatherString = weatherData.get('summary')
        self.weatherLabel.configure(text = weatherString)

    def updateNews(self):
        newsData = self.client.recieveData('news')
	articles = newsData.get('articles')
        newsString = ' '
        for item in articles:
        	newsString += item['title']
                newsString += "\n"
        self.newsLabel.configure(text = newsString)
        

    def updateAll(self):
        self.updateWeather()
        self.updateNews()

g = GUI()
g.startGUI()

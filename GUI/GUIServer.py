import json, StringIO, socket, sys, time, weather, news, database, serial

#passed to the json encoder to check and use the serializing method if found, else returns an error
class EncoderClass(json.JSONEncoder):
    def default(self,o):
        if hasattr(o, 'serializable'):
            return o.serializable()
        else:
            raise TypeError


class Modules:
	def __init__(self):
		self.news = 'on'
		self.weather = 'on'
	def setNews(self, onOff):
		self.news = onOff
	def setWeather(self, onOff):
		self.weather = onOff
	def serializable(self):
		return self.__dict__

class serv:


    def start(self, local = '10.0.0.52', lPort = 50, remote = '10.0.0.52', rPort = 51):
        
	print("Starting UDP Server")
	ser = serial.Serial('/dev/ttyACM0', 9600)
       
        #initialize socket addresses and ports
        localName = local
        localPort = lPort
        remoteName = remote
        remotePort = rPort

        #Initialize the UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	localAddress = (localName, localPort)
        remoteAddress = (remoteName, remotePort)
        s.bind(localAddress)

        db = database.Databade()
	modules = Modules()
  
	while True:
	   
            notRec = True
		
            #while nothing is recieved, loop
            while notRec:
                print("Waiting for Request on port %d : press Ctrl-C to stop" % localPort)

                #recieves data from client and stores it in buf
                buf, address = s.recvfrom(2048)
                if not len(buf):
                    break
                #displays data received for validation
                print("Recieved %s bytes from %s '%s': " % (len(buf), address, buf))
                if 'news' in buf or 'weather' in buf or 'modules' in buf or 'led' in buf:
                    notRec = False

            if 'news off' in buf:
                modules.setNews('off')
	    elif 'weather off' in buf:
		modules.setWeather('off')
	    elif 'news on' in buf:
		modules.setNews('on')
	    elif 'weather on' in buf:
		modules.setWeather('on')

	    elif 'led on' in buf:
                led = buf.split()
                values = db.getLed(led[1])
                ser.write(values.get('red'))
                ser.write(values.get('green'))
                ser.write(values.get('blue'))
                
                
            elif 'modules' in buf:
		jsonModules = json.dumps(modules, cls = encoderClass)
                s.sendto(jsonModules.encode('utf-8'), remoteAddress)
            
            elif 'weather' in buf:

                weatherData = weather.getCurrentData()
                jsonWeather = json.dumps(weatherData, cls = encoderClass)

                #sends JSON data on different free port encoded in utf-8
                s.sendto(jsonWeather.encode('utf-8'), remoteAddress)
            elif 'news' in buf:
                newsData = news.newsData()
                jsonNews = json.dumps(newsData, cls = encoderClass)

                s.sendto(jsonNews.encode('utf-8'), remoteAddress)


        #closes the socket
        s.close()

server = serv()
server.start()


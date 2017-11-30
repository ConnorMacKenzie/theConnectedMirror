import json, StringIO, socket, sys, time, weather, news

#passed to the json encoder to check and use the serializing method if found, else returns an error
class encoderClass(json.JSONEncoder):
    def default(self,o):
        if hasattr(o, 'serializable'):
            return o.serializable()
        else:
            raise TypeError

class serv:

    def start(self, local = 'localhost', lPort = 23, remote = 'localhost', rPort = 22):
        print("Starting UDP Server")

        #initialize socket addresses and ports
        localName = local
        localPort = lPort
        remoteName = remote
        remotePort = rPort

        #Initialize the UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        localAddress = (localName, localPort)
        remoteAddress = (remoteName, remotePort)
        s.bind(localAddress)
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
                if 'news' in buf or 'weather' in buf:
                    notRec = False

            if 'weather' in buf:

                weatherData = weather.getCurrentData()
                jsonWeather = json.dumps(weatherData, cls = encoderClass)

                #sends JSON data on different free port encoded in utf-8
                s.sendto(jsonWeather.encode('utf-8'), remoteAddress)
            if 'news' in buf:
                newsData = news.newsData()
                jsonNews = json.dumps(newsData, cls = encoderClass)

                s.sendto(jsonNews.encode('utf-8'), remoteAddress)
                
        #closes the socket
        s.close()

server = serv()
server.start()

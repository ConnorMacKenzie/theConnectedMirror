'''
weatherServer.py
GIT URL: https://github.com/ConnorMacKenzie/theConnectedMirror/WeatherModule/weatherServer.py
Version 3.0
Added UDP communication along with specific requests
November 26th, 2017
'''

import forecastio, json, StringIO, socket, sys, time


class getCurrentData:
    apikey = "566169fcb4282ff1c9d716df2ccdfd90"
    lat = 45.411572
    lng = -75.698194
    forecast = forecastio.load_forecast(apikey, lat, lng, units = "ca")
    curr = forecast.currently()
    def __init__(self):
        self.summary = self.curr.summary
        self.icon = self.curr.icon
        self.temp = self.curr.temperature
        self.visibility = self.curr.visibility
        self.windSpeed = self.curr.windSpeed
        self.cloudPercent = self.curr.cloudCover*100
        self.humidity = self.curr.humidity
        self.precipPercent = self.curr.precipProbability*100
        if self.precipPercent > 0:
            self.precipType = self.curr.precipType
        self.pressure = self.curr.pressure

    def serializable(self):
        return self.__dict__

class encoderClass(json.JSONEncoder):
    def default(self,o):
        if hasattr(o, 'serializable'):
            return o.serializable()
        else:
            raise TypeError


data = getCurrentData()
jsonData = json.dumps(data, cls = encoderClass)

print("Starting UDP Server")

localName = raw_input("Input Local Address: ")
localPort = int(input("Input Local Port: "))
remoteName = raw_input("Input Remote Address: ")
remotePort = int(input("Input Remote Port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
localAddress = (localName, localPort)
remoteAddress = (remoteName, remotePort)
s.bind(localAddress)
notRec = True
while notRec:
    print("Waiting for Request on port %d : press Ctrl-C to stop" % localPort)
    buf, address = s.recvfrom(2048)
    if not len(buf):
        break
    print("Recieved %s bytes from %s '%s': " % (len(buf), address, buf))
    notRec = False



s.sendto(jsonData.encode('utf-8'), remoteAddress)
s.close()

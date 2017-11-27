'''
weatherServer.py
GIT URL: https://github.com/ConnorMacKenzie/theConnectedMirror/WeatherModule/weatherServer.py
Version 3.0
Added UDP communication along with specific requests
November 26th, 2017
'''

import forecastio, json, StringIO, socket, sys, time

#when initialized, this class gets information on curent weather
class getCurrentData:

    #API key given by Forecast.io to access data
    apikey = "566169fcb4282ff1c9d716df2ccdfd90"
    #Latitude and longitude of the SYSC3010 lab
    lat = 45.411572
    lng = -75.698194
    #forcast data object
    forecast = forecastio.load_forecast(apikey, lat, lng, units = "ca")
    #requests forecast of current time
    curr = forecast.currently()

    #Constructor which takes only self as an argument
    def __init__(self):

        #sets variables to the values recieved from Forecast.io
        self.summary = self.curr.summary
        self.icon = self.curr.icon
        self.temp = self.curr.temperature
        self.visibility = self.curr.visibility
        self.windSpeed = self.curr.windSpeed
        self.cloudPercent = self.curr.cloudCover*100
        self.humidity = self.curr.humidity
        self.precipPercent = self.curr.precipProbability*100
        #precipType returns an error if called when percentage of precipitation is 0
        if self.precipPercent > 0:
            self.precipType = self.curr.precipType
        self.pressure = self.curr.pressure

        #serializing method for the class to be converted into a JSON string
    def serializable(self):
        return self.__dict__

#passed to the json encoder to check and use the serializing method if found, else returns an error
class encoderClass(json.JSONEncoder):
    def default(self,o):
        if hasattr(o, 'serializable'):
            return o.serializable()
        else:
            raise TypeError

#initializes the class
data = getCurrentData()
#encodes the forecast data as a JSON string
jsonData = json.dumps(data, cls = encoderClass)

print("Starting UDP Server")

#initialize socket addresses and ports
localName = raw_input("Input Local Address: ")
localPort = int(input("Input Local Port: "))
remoteName = raw_input("Input Remote Address: ")
remotePort = int(input("Input Remote Port: "))

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
        notRec = False

    #sends JSON data on different free port encoded in utf-8
    s.sendto(jsonData.encode('utf-8'), remoteAddress)
    #closes the socket
s.close()

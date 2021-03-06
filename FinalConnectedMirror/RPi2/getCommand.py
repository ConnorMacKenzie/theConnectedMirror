import speech
import socket

class SpeechCommand():

    def __init__(self, local = '10.0.0.51', localport = 51, remote = '10.0.0.52', remoteport = 50):

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

        while 1:
            self.getCommand(self)

    def sendData(self, field):
            self.s.sendto(field.encode('utf-8'), self.remoteAddress)

    @staticmethod
    def getCommand(self):
        
        s = speech.Speech()
        words = s.record().split()

        isLED = False
        isNews = False
        isWeather = False

        print words
        
        if words[0] != 'client':
            return

        for word in words:
            if word == 'news':
                isNews = True
            if word == 'weather':
                isWeather = True
            if word == 'led':
                isLED = True

        if isNews:
            for word in words:
                if word == 'on':
                    self.sendData('news on')
                elif word == 'off':
                    self.sendData('news off')
               
        if isWeather:
            for word in words:
                if word == 'on':
                    self.sendData('weather on')
                elif word == 'off':
                    self.sendData('weather off')
                
        if isLED == True:
            for word in words:
                if word == 'on':
                    for word in words:
                        if word == '1' or word == 'one':
                            self.sendData('LED 1 on')
                        elif word == '2' or word == 'two' or word == 'to' or word == 'too':
                            self.sendData('LED 2 on')
                        elif word == '3' or word == 'three':
                            self.sendData('LED 3 on')
                        elif word == '4' or word == 'four' or word == 'for' or word == 'fore':
                            self.sendData('LED 4 on')
                        elif word == '5' or word == 'five':
                            self.sendData('LED 5 on')
                elif word == 'off':
                    self.sendData('LED off')
            
        else:
            return

        

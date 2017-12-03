import speech
import socket

class SpeechCommand():

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

        while 1:
            print self.getCommand(self)

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
        
        if words[0] != 'connected':
            return

        for word in words:
            if word == 'news':
                isNews = True
            if word == 'weather':
                isWeather = True
            if word == 'LED':
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
                        if word == '1' or 'one':
                            self.sendData('LED 1 on')
                        if word == '2' or 'two':
                            self.sendData('LED 2 on')
                        if word == '3' or 'three':
                            self.sendData('LED 3 on')
                        if word == '4' or 'four':
                            self.sendData('LED 4 on')
                        if word == '5' or 'five':
                            self.sendData('LED 5 on')
                elif word == 'off':
                    self.sendData('LED off')
            
        else:
            return

        

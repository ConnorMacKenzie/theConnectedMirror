'''
weatherClient.py
GIT URL: https://github.com/ConnorMacKenzie/theConnectedMirror/WeatherModule/weatherClient.py
Version 3.0
Added UDP communication along with specific requests
November 26th, 2017
'''

import socket, sys, time, json

class client:

    #initializes socket addresses and ports
    #localName = raw_input("Input Local Address: ")
    #localPort = int(input("Input Local Port: "))
    #remoteName = raw_input("Input Remote Address: ")
    #remotePort = int(input("Input Remote Port: "))

    #initializes sockets
    def initialize(self, localName, localPort, remoteName, remotePort):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.localAddress = (localName, localPort)
        self.remoteAddress = (remoteName, remotePort)
        self.s.bind(self.localAddress)
        return self.s.getsockname()


    def closeConnection(self):
        self.s.close()


    def pullRequest(self, inputString):

        notSent = True
        bites = 0
        #while nothing is sent, loop
        while notSent:
            #print ("Enter non-null weather pull request: ")
            #sets the string to be sent as the next line in the terminal
            request = inputString
            if not len(request):
                break
            #sends the next line in the terminal to the server socket
            bites = self.s.sendto(request.encode('utf-8'), self.remoteAddress)
            notSent = False

        return bites



    def startListening(self):
        notRec = True
        #while nothing is received, loop
        while notRec:
            #receives data from server and stores in buf
            buf, address = self.s.recvfrom(2048)
            if not len(buf):
                break
            notRec = False

        #decodes utf-8 data to store json string
        jsonData = buf.decode('utf-8')

        #decodes json string into python dictionary to enable manipulation and access
        data = json.loads(jsonData)

        return data

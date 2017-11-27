'''
weatherClient.py
GIT URL: https://github.com/ConnorMacKenzie/theConnectedMirror/WeatherModule/weatherClient.py
Version 3.0
Added UDP communication along with specific requests
November 26th, 2017
'''

import socket, sys, time, json

class Client():

    def __init__(self, local, localport, remote, remoteport):

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

    def sendReceive(self, field):

        notSent = True

        #while nothing is sent, loop
        while notSent:
            #print ("Enter non-null weather pull request: ")
            #sets the string to be sent as the next line in the terminal
            request = field
            if not len(request):
                break
            #sends the next line in the terminal to the server socket
            self.s.sendto(request.encode('utf-8'), self.remoteAddress)
            notSent = False



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

        return data.get(field)

import socket, time

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

        field = 'news off'

        self.s.sendto(field.encode('utf-8'), self.remoteAddress)

        time.sleep(8)
        
        field = 'weather off'

        self.s.sendto(field.encode('utf-8'), self.remoteAddress)

        time.sleep(8)

        field = 'news on'

        self.s.sendto(field.encode('utf-8'), self.remoteAddress)

        time.sleep(8)

        field = 'weather on'

        self.s.sendto(field.encode('utf-8'), self.remoteAddress)

SpeechCommand()

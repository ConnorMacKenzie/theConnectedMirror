

class SpeechClient():

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

       def recieveData(self, field):
                #print ("Enter non-null weather pull request: ")
                #sets the string to be sent as the next line in the terminal

                #sends the next line in the terminal to the server socket
                self.s.sendto(field.encode('utf-8'), self.remoteAddress)

                #receives data from server and stores in buf
                buf, address = self.s.recvfrom(100000)
                #decodes utf-8 data to store json string
                data = buf.decode('utf-8')

                

                return data

            
                

        

'''
weatherClient.py
GIT URL: https://github.com/ConnorMacKenzie/theConnectedMirror/WeatherModule/weatherClient.py
Version 3.0
Added UDP communication along with specific requests
November 26th, 2017
'''

import socket, sys, time, json

#initializes socket addresses and ports
localName = raw_input("Input Local Address: ")
localPort = int(input("Input Local Port: "))
remoteName = raw_input("Input Remote Address: ")
remotePort = int(input("Input Remote Port: "))

#initializes sockets
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
localAddress = (localName, localPort)
remoteAddress = (remoteName, remotePort)
s.bind(localAddress)

notSent = True

#while nothing is sent, loop
while notSent:
    print ("Enter non-null weather pull request: ")
    #sets the string to be sent as the next line in the terminal
    request = sys.stdin.readline().strip()
    if not len(request):
        break
    #sends the next line in the terminal to the server socket
    s.sendto(request.encode('utf-8'), remoteAddress)
    notSent = False



notRec = True
#while nothing is received, loop
while notRec:
    #receives data from server and stores in buf
    buf, address = s.recvfrom(2048)
    if not len(buf):
        break
    notRec = False

#decodes utf-8 data to store json string
jsonData = buf.decode('utf-8')

#decodes json string into python dictionary to enable manipulation and access
data = json.loads(jsonData)

#to access a specific element
print("What would you like to display?")
print("(summary/icon/temp/visibility/windSpeed/cloudPercent/humidity/precipPercent/pressure)")
specs = raw_input()

print(data.get(specs))

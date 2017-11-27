'''
weatherClient.py
GIT URL: https://github.com/ConnorMacKenzie/theConnectedMirror/WeatherModule/weatherClient.py
Version 3.0
Added UDP communication along with specific requests
November 26th, 2017
'''

import socket, sys, time, json

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
    print ("Enter non-null weather pull request: ")
    request = sys.stdin.readline().strip()
    if not len(request):
        break
    #s.sendall(data.encode('utf-8'))
    s.sendto(request.encode('utf-8'), remoteAddress)
    notRec = False



notRec = True

while notRec:
    buf, address = s.recvfrom(2048)
    if not len(buf):
        break
    notRec = False

jsonData = buf.decode('utf-8')

data = json.loads(jsonData)

print("What would you like to display?")
print("(summary/icon/temp/visibility/windSpeed/cloudPercent/humidity/precipPercent/pressure)")
specs = raw_input()

print(data.get(specs))

import json
import database

#Connor MacKenzie

#expected data to be returned from database class
data1 = [['led_id', 100], ['red', 10], ['green', 10], ['blue', 10], ['white', 0], ['brightness', 10]]
data2 = [['setting_id', 1], ['location', 'Ottawa'], ['modules', 2]]
data3 = ['Bad', 'Data']

#pass database class a user id and led id to get JSON info on both back
db = database.database()
test1 = db.getLed(100)
test2 = db.getUser(1)

#test with bad data to recieve null json back
test3 = db.getLed(0)
test4 = db.getUser(0)

#decode JSON
json1 = json.loads(test1)
json2 = json.loads(test2)
json3 = json.loads(test3)
json4 = json.loads(test4)

#Check if data recieved matched expected results
if data1 == json1:
    print "Pass test 1"
else:
    print "Fail test 1"

#Check if data recieved matched expected results
if data2 == json2:
    print "Pass test 2"
else:
    print "Fail test 2"

#Check if data recieved matched expected results
if json3 == data3:
    print "Pass test 3"
else:
    print "Fail test 3"

#Check if data recieved matched expected results
if json4 == data3:
    print "Pass test 4"
else:
    print "Fail test 4"


    

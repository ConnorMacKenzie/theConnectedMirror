import json
import database

#expected data to be returned from database class
data1 = [['led_id', 100], ['red', 10], ['green', 10], ['blue', 10], ['white', 0], ['brightness', 10]]
data2 = [['setting_id', 1], ['location', 'Ottawa'], ['modules', 2]]

#pass database class a user id and led id to get JSON info on both back
db = database.database()
test1 = db.getLed(100)
test2 = db.getUser(1)

#decode JSON
json1 = json.loads(test1)
json2 = json.loads(test2)

#Check if data recieved matched expecred results
if data1 == json1:
    print "Pass test 1"
else:
    print "Fail test 1"

#Check if data recieved matched expecred results
if data2 == json2:
    print "Pass test 2"
else:
    print "Fail test 2"
    

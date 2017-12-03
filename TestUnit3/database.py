import MySQLdb
import json

#Connor Mackenzie

#Class of fucntions for database interactions
class database:

    #get row for led_settings table given led_id, return in JSON format
    @staticmethod
    def getLed(led_id):
        db = MySQLdb.connect("localhost", "root", "mysql", "connected_mirror")
        cur = db.cursor()
        cur.execute("SELECT * FROM led_settings WHERE led_id = " + str(led_id))
        result = cur.fetchone()
        db.commit()
        db.close()

        if result == None:
            data = ['Bad','Data']
        else:
            data = [['led_id', result[0]], ['red', result[1]], ['green', result[2]], ['blue', result[3]]]
        jsonData = json.dumps(data)
        return jsonData

    #Insert new row into led_settings table given data for all columns
    @staticmethod
    def setLed(led_id, r, g, b, w, bri):
        db = MySQLdb.connect("localhost", "root", "mysql", "connected_mirror")
        cur = db.cursor()
        cur.execute("INSERT INTO led_settings (led_id, red, green, blue) VALUES(" + str(led_id) + "," + str(r) + "," + str(g) + "," + str(b) + ")")
        db.commit()
        db.close()

    #Update row in led_settings table given led_id and data for columns
    @staticmethod
    def updateLed(led_id, r, g, b, w, bri):
        db = MySQLdb.connect("localhost", "root", "mysql", "connected_mirror")
        cur = db.cursor()
        cur.execute("UPDATE led_settings SET red = " + str(r) + ", green = " + str(g) + ", blue = " + str(b) + " WHERE led_id = " + str(led_id))        
        db.commit()
        db.close()

    #get row for user_settings table given setting_id, return in JSON format
    @staticmethod
    def getUser(setting_id):
        db = MySQLdb.connect("localhost", "root", "mysql", "connected_mirror")
        cur = db.cursor()
        cur.execute("SELECT * FROM user_settings WHERE setting_id = " + str(setting_id))
        result = cur.fetchone()
        db.commit()
        db.close()

        if result == None:
            data = ['Bad','Data']
        else:
            data = [['setting_id', result[0]], ['location', result[1]], ['modules', result[2]]]
        jsonData = json.dumps(data)
        return jsonData

    #Insert new row into user_settings table given data for all columns
    @staticmethod
    def setUser(setting_id, location, modules):
        db = MySQLdb.connect("localhost", "root", "mysql", "connected_mirror")
        cur = db.cursor()
        cur.execute("INSERT INTO user_settings (setting_id, location, modules) VALUES(" + str(setting_id) + ", '" +str(location) + "', " + str(modules) + ")")
        db.commit()
        db.close()

    #Update row in user_settings table given setting_id and data for columns
    @staticmethod
    def updateUser(setting_id, location, modules):
        db = MySQLdb.connect("localhost", "root", "mysql", "connected_mirror")
        cur = db.cursor()
        cur.execute("UPDATE user_settings SET location = '" + str(location) + "', modules = " + str(modules) + " WHERE setting_id = " + str(setting_id))
        db.commit()
        db.close()

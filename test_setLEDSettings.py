import MySQLdb

db = MySQLdb.connect("localhost", "root", "mysql", "connected_mirror")

cur = db.cursor()

cur.execute("INSERT INTO led_settings (led_id, red, green, blue, white, brightness) VALUES(100, 0, 0, 0, 0, 0)")

cur.execute("SELECT * FROM led_settings WHERE led_id = 100")

result = cur.fetchone()

for row in result:
    print row

cur.execute("DELETE FROM led_settings WHERE led_id = 100")

db.commit()

db.close()


import MySQLdb

db = MySQLdb.connect("localhost", "root", "mysql", "connected_mirror")

cur = db.cursor()

cur.execute("INSERT INTO led_settings (setting_id, location, modules) VALUES(100, 'Ottawa', 2)")

cur.execute("UPDATE led_settings")

db.commit()

result = cur.fetchall()

db.commit()

for row in result:
    print row

cur.execute("DELETE FROM led_settings WHERE setting_id = 100")

import MySQLdb

db = MySQLdb.connect("localhost", "root", "mysql", "connected_mirror")

cur = db.cursor()

cur.execute("INSERT INTO user_settings (setting_id, location, modules) VALUES(100, 'Ottawa', 2)")

cur.execute("SELECT * FROM user_settings WHERE setting_id = 100")

result = cur.fetchone()

for row in result:
    print row

cur.execute("DELETE FROM user_settings WHERE setting_id = 100")

db.commit()

db.close()

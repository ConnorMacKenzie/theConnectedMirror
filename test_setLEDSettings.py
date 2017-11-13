import MySQLdb

db = MySQLdb.connect("localhost", "root", "mysql", "connected_mirror")

cur = db.cursor()

cur.execute("INSERT INTO led_settings () VALUES()")

db.commit()

result = cur.fetchall()

db.commit()

for row in result:
    print row

cur.execute("DELETE FROM led_settings WHERE")

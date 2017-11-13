import MySQLdb

db = MySQLdb.connect("localhost", "root", "mysql", "connected_mirror")

cur = db.cursor()

cur.execute("INSERT INTO user_settings (location, modules) VALUES('Ottawa', 2)")

for row in cur.fetchall():
    print row

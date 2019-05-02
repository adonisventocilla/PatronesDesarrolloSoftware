import pymysql as DB

db = DB.connect("localhost","root","adonis","bdprueba")
cursor = db.cursor()
cursor.execute("SELECT * FROM persona")
for row in cursor:
   print(row)
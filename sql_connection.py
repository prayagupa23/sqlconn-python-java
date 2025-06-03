# to connect MySQL database using mysql-connector-python
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "Prayag@2308",
    database = "demo",
)

cursor= conn.cursor()

cursor.execute("INSERT INTO student(sid,name,address,stream) VALUES(%s,%s,%s,%s)",(101,"Pramod","Mumbai","computer"))
conn.commit()
cursor.execute("SELECT * FROM student")
for i in cursor.fetchall():
    print(i)
cursor.close()
conn.close()
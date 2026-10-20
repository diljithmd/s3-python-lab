import sqlite3

conn = sqlite3.connect('student.db')

if(conn):
    print("Connected Successfully")
else:
    print("Not Connected")

cursor=conn.cursor()
cursor.execute("create table if not exists football(ida integer primary key,name text,goal integer)")
conn.commit()
cursor.execute("insert into football(ida,name,goal)values(10,'messi',745)")
cursor.execute("insert into football(ida,name,goal)values(7,'ronaldo',658)")
cursor.execute("insert into football(ida,name,goal)values(28,'yamil',356)")
cursor.execute("insert into football(ida,name,goal)values(24,'yamil',24)")
conn.commit()

print("exicuted")
cursor.execute("select * from football")
rows=cursor.fetchall()
for row in rows:
    print(row)
cursor.execute("delete from football where ida=24")
conn.commit()
print("deleted")
cursor.execute("select * from football")
rows=cursor.fetchall()
for row in rows:
    print(row)
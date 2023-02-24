import sqlite3

db=sqlite3.connect('students.db')

c = db.cursor()

c.execute(''' CREATE TABLE IF NOT EXISTS student (
id integer AVTOINCREMENT,
hobbi text, 
name text,
surname text,
years integer, 
point integer
 ) ''')

c.execute("INSERT INTO student VALUES ('MUSIC', 'SERGY', 'BEIAEV', 1695, 1)")
c.execute("INSERT INTO student VALUES ('MUSI', 'SERGY', 'BELAEV', 1495, 2)")
c.execute("INSERT INTO student VALUES ('MUSC', 'SEREY', 'BELIEV', 1995, 3)")
c.execute("INSERT INTO student VALUES ('MSIC', 'SRGEY', 'BLIAEV', 1395, 4)")
c.execute("INSERT INTO student VALUES ('MSIC', 'SEREY', 'BELIEV', 1295, 5)")
c.execute("INSERT INTO student VALUES ('MSIC', 'SERGEY', 'DFDFSFSDFDFSF', 1995, 6)")
c.execute("INSERT INTO student VALUES ('MUIC', 'SEGEY', 'BELIAE', 1995, 7)")
c.execute("INSERT INTO student VALUES ('MUSC', 'SERGY', 'ELIAEV', 1395, 12)")
c.execute("INSERT INTO student VALUES ('MUSC', 'SEREY', 'BEIAEVDF', 1995, 13)")
c.execute("INSERT INTO student VALUES ('MUSIC', 'SEGEY', 'DFDFFDFDFDF', 1995, 140)")

c.execute("SELECT * FROM student WHERE LENGTH(surname) > 10")

c.execute("UPDATE student SET name = 'genius' WHERE point > 10")

c.execute("SELECT * FROM student WHERE name = 'genius'")

c.execute("DELETE FROM student WHERE rowid % 2 = 0")
# c.execute("SELECT name FROM student WHERE name = 'genius'")

print(c.fetchall())
db.commit()
db.close()
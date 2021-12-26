import sqlite3
conn=sqlite3.connect("sqlite.db")     # sqlite.db file will be created at the same location of sqlitedb.py file.
conn.execute('''
      CREATE TABLE student(
        st_id INT AUTO_INCREMENT PRIMARY KEY,
        st_name VARCHAR(50),
        st_class VARCHAR(10),
        st_email VARCHAR(30)
       )
    ''')
conn.close()

################ INSERT ###############################
import sqlite3
conn=sqlite3.connect("sqlite.db")

ins='''
    INSERT INTO student (st_name, st_class, st_email) VALUES
    ('Rahul','12th',"rahul10@gmail.com")
'''
conn.execute(ins)
conn.commit()
conn.close()

################ SELECT ###############################
import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM student LIMIT 0,2")
print("STUDENT ID", "STUDENT NAME", "STUDENT CLASS", "STUDENT EMAIL")
for i in data:
  print(i[0],i[1],i[2],i[3])

st_name=input("Enter the Student Name: ")
# SELECT * FROM student WHERE st_name='"+st_name+"'
# SELECT * FROM student WHERE st_name='"+st_name+"'
data=conn.execute("SELECT * FROM student WHERE st_name LIKE '%"+st_name+"%'")

################ DELETE ###############################
import sqlite3
conn=sqlite3.connect("sqlite.db")
st_id=input("Enter the Student ID: ")
conn.execute("DELETE FROM student WHERE st_id="+st_id)
conn.commit()
conn.close()

################ UPDATE ###############################
import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''UPDATE student SET st_name='Ronak' WHERE st_id=1''')
conn.commit()
conn.close()

########### Connection and Database create ###############
import pymysql as pm
dbConnect=pm.connect("localhost","root","")
dbcursor=dbConnect.cursor()
try:
  db="create database school"
  dbcursor.execute(db)
  print("database created")
  
except:
  print("database error")
  
################## CRATE TABLE #########################
import pymysql as pm
dbconn=pm.connect(
  host:"localhost",
  user:"root",
  password:"",
  database:"school")

dbcursor=dbconn.cursor()
tbl="CREATE TABLE student(st_id INT PRIMARY KEY AUTO_INCREMENT, st_name VARCHAR(50), st_class VARCHAR(10), st_email VARCHAR(50))"
dbcursor.execute(tbl)

################## INSERT #########################
import pymysql as pm
dbconn=pm.connect(host:"localhost",user:"root",password:"",database:"school")
dbcursor=dbconn.cursor()
try:
   query="INSERT INTO student(st_name,st_class,st_email) VALUES (%s,%s,%s)"
   value=("Ram","12th","ram@gmail.com")
   dbcursor.execute(query,value)
    
   #### Inserting multiple values together ####
   # value=[("Ram","12th","ram@gmail.com"),("Ronak","10th","ronak@gmail.com")]
   # dbcursor.executemany(query,value)
  
   dbConnect.commit();
   print("Data Inserted")
except:
  print("Error...")
  
################## SELECT #########################
import pymysql as pm
dbconn=pm.connect(host:"localhost",user:"root",password:"",database:"school")
dbcursor=dbconn.cursor()
dbcursor.execute("SELECT * FROM student")
print("{:<20} {:<30} {:<15} {:<30}".format("Student ID","Student Name", "Student Email", "Student Class"))
try:
  # myresult=dbcursor.fetchone()                    To get the one raw data only.
  myresult=dbcursor.fetchall()
  for x in myresult:
    print("{:^20} {:<30} {:<15} {:<30}".format(x[0],x[1],x[2],x[3]))
except:
  print("Error")
  

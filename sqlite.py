import sqlite3
MySchool=sqlite3.connect('user.db')

curschool=MySchool.cursor()
curschool.execute("CREATE TABLE teacher(Teacherid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT (20),username TEXT (15) NOT NULL,password TEXT (15) NOT NULL,gender TEXT (10) NOT NULL,book TEXT (30),fruit TEXT (10),friend TEXT (20));")
MySchool.close()

import sqlite3  
  
con = sqlite3.connect("Account.db")  
print("Database opened successfully")  
  
con.execute("create table Account (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL,Age INTEGER  NOT NULL,dob TEXT NOT NULL,Email TEXT NOT NULL,Password TEXT UNIQUE NOT NULL)")  
  
print("Table created successfully")  
  
con.close()
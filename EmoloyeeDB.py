import sqlite3  
  
con = sqlite3.connect("login.db")  
print("Database opened successfully")  
  
con.execute("create table login (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE NOT NULL,pwd TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()
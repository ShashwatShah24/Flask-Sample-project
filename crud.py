from flask import *  
import sqlite3  
  
app = Flask(__name__)  
app.secret_key = "abc"  

@app.route("/")  
def index():  
    return render_template("index.html");

@app.route("/savedetails1",methods = ["POST","GET"])  
def saveDetails1():  
    msg = "msg"  
    if request.method == "POST":  
        try:   
            Email = request.form["email"]
            pwd = request.form["pwd"] 
            print(Email,pwd)    
            with sqlite3.connect("Account.db") as con:  
                cur = con.cursor()
                print("Connection test")   
                cur.execute("SELECT * FROM Account WHERE Email= ? and Password= ?",(Email, pwd))
                row = cur.fetchone()
                print("query test")  
                while row is not None:
                	msg = row[1] +" Welcome to airtel"
                	session['email']=request.form['email']  
                	print(row[1])
                	return render_template("success.html",msg = msg)
                else:
                	msg = "sorry wrong id"
                	return render_template("failure.html",msg = msg)
        except:  
            con.rollback()  
            msg = "problem"  

@app.route('/logout')  
def logout():  
    if 'email' in session:  
        session.pop('email',None)
        msg = "Thank you,Please login again!"
        return render_template("failure.html",msg = msg)  
    else:
    	msg = "sorry aldready log out"
    	return render_template("failure.html",msg = msg)   

@app.route("/register")  
def register():  
    return render_template("register.html")  

@app.route('/about')
def about():
    return render_template('about.html')
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["Name"]  
            Age = request.form["Age"] 
            dob = request.form["dob"]  
            Email = request.form["Email"]
            pwd = request.form["pwd"]  
            rpwd = request.form["rpwd"]   
            with sqlite3.connect("Account.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Account (Name,Age,dob,Email,Password) values (?,?,?,?,?)",(name,Age,dob,Email,pwd))  
                con.commit()  
                msg = "Employee successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()  
 
@app.route("/view")  
def view():  
    con = sqlite3.connect("Account.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Account ")  
    rows = cur.fetchall()
    if 'email' in session:
    	email = session['email']   
    	return render_template("view.html",rows = rows) 
    else:
    	return '<p>Please login first</p>'  
 
 
@app.route("/delete")  
def delete():  
    return render_template("delete.html")  
 
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    name1 = request.form["name1"]
    print(name1) 
    with sqlite3.connect("Account.db") as con:  
        try:  
            cur = con.cursor() 
            print("yoyo") 
            cur.execute("delete from Account where id = ?",name1)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record.html",msg = msg)  
  
if __name__ == "__main__":  
    app.run(debug = True)  
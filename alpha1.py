from flask import *  
import pandas as pd
import sqlite3  
  
app = Flask(__name__)  

@app.route("/")  
def add():  
    return render_template("index02.html")  
 
@app.route("/savedetails",methods = ["POST"])  
def saveDetails():  
        try:  
            a3 = request.form["sn"] 
            data = pd.read_excel('Book1.xlsx', sheet_name='Sheet1')
            rslt_df = data[data['a3'] == a3]
            stocklist = list(rslt_df.values)
            return render_template('simple.html', stocklist=stocklist)
        except:  
            return "error"     

 
if __name__ == "__main__":  
    app.run(debug = True)    


#rslt_df = df[df['a3'] == 'q37']
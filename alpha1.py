from flask import *  
import pandas as pd
import sqlite3  
  
app = Flask(__name__)  
 
@app.route("/")  
def Stocks():
    data = pd.read_excel('Book1.xlsx', sheet_name='Sheet1')

    stocklist = list(data.values)
    return render_template('simple.html', stocklist=stocklist)  
  
if __name__ == "__main__":  
    app.run(debug = True)    
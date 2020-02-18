from flask import *  

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("dropdown.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        car_brand = request.form.get("cars", None)
        if car_brand!=None:
            return render_template("dropdown.html", car_brand = car_brand)
    return render_template("dropdown.html")

if __name__ == '__main__':
    app.run(debug=True)
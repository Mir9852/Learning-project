from flask import Flask
from markupsafe import escape
#from flask import escape
from flask import request
from flask import render_template
app=Flask(__name__)

@app.route('/')
def index():
#    mydata = {"Nama" : "Muhamad Amir", "Alamat" : "Bogor", "Usia" : "26"}
#    mylist = ["apel", "mangga", "jeruk"]
#    thidic = {"nama":"Amir", "alamat":"Bogor", "Usia":"26"}
    return render_template('index.html')
  

@app.route('/about')
def about():
    return '<h1>About Us</h1>'

@app.route('/contact')
def contact():
    return '<h1>Contact Us</h1>'

@app.route('/profile')
def profile():
    return '<h1>Profile</h1>'

#@app.route('/profile/<string:username>')
#def profile_name(username):
#    return '<h1>Hello %s!</h1>' % username

@app.route("/htmlescape/<code>")
def htmlescape(code):
    return escape(code)

#@app.route('/routetanpaslah')
#def ruotetanpaslah():
#    return '<h1>Route Tanpa Slah</h1>'

#@app.route("/routedenganslah/")
#def routedenganslah():
#    return '<h1>Route Dengan Slah</h1>'

@app.route("/cobarequest", methods=['GET', 'POST'])
def cobarequest():
    if request.method=="GET":
        return request.args.get("nama") + request.args.get("alamat")
    elif request.method=="POST":
        return request.form["nama"]

app.run(debug=True)
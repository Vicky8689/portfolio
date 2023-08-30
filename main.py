from distutils import debug
from flask import Flask,render_template
# app define
app = Flask(__name__,template_folder='Templats')

@app.route("/")
def home():
    return render_template('index.html')
# @app.route("/about")
# def hello1():
#     name = "vicky"
#     return render_template('about.html',name2=name)
@app.route("/about")
def about():
    return render_template('index.html')

@app.route("/resume")
def resume():
    return render_template('index.html')
@app.route("/portfolio")
def portfolio():
    return render_template('index.html')
@app.route("/services")
def services():
    return render_template('index.html')
@app.route("/contact")
def contact():
    return render_template('index.html')

 
app.run(debug=True)
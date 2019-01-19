from flask import Flask,render_template
from daya import faculties
app = Flask(__name__)
myfaculty =  faculties()
# @app.route('/')
# def index():
    # return "<h1>hello</h1>"
@app.route('/about')
def about():
    return render_template('About.html')
@app.route('/Login')
def login():
    return render_template('index.html')
@app.route('/register')
def reg():
    return render_template('Register.html')
@app.route('/faculty')
def fac():
    return render_template('faculty.html',facultylist = myfaculty)
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == "__main__":
   app.run(debug = True)
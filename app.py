from flask import Flask, render_template 
app = Flask(__name__)

COURSE = [
  {
    'id':1,
     'name':'Data Analysis'
  },
  {
    'id':2,
     'name':'Data Science'
  }
]


@app.route("/")
def hello_techyian():
  return render_template('home.html',course=COURSE)

if __name__ =="__main__":
  app.run(host='0.0.0.0',debug=True)
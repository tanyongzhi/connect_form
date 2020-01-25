from flask import Flask, render_template, request, url_for, redirect
from constants import *
import json

app = Flask(__name__)


@app.route("/")  # we are using get method here
def index():
    return render_template("index.html")

@app.route("/student")  # we are using get method here
def student():
    return render_template("student.html")

@app.route('/redirect_home',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("redirect_home.html",result = result)


@app.route("/slacker")  # we are using get method here
def slacker_list():
    test = Slacker(4, "HL Lee", "6 to 9", (6, 9), (7, 10))
    test2 = Slacker(5, "HY Lee", "1 to 9", (1, 9), (6, 10))
    test_arr = [test, test2]
    json_string = json.dumps([ob.__dict__ for ob in test_arr])
    print(json_string)
    return render_template("slacker_list.html", user=json_string)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

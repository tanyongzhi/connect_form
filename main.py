from flask import Flask, render_template 
from constants import *

app = Flask(__name__)

@app.route("/") # we are using get method here
def index():
    test = Slacker(4, "aspen tng liang gen", "6 to 9", (6, 9), (7, 10))
    test2 = 2
    return render_template("index.html", test=test)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
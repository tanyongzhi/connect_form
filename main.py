from flask import Flask, render_template 
from constants import *
import json

app = Flask(__name__)

@app.route("/") # we are using get method here
def index():
    test = Slacker(4, "aspen tng liang gen", "6 to 9", (6, 9), (7, 10))
    # new_test = []
    # for i in test.__dict__:
    #     new_test.extend([test.__dict__[i]])

    # hello = ["asd", "asds"]
    user = json.dumps(test.__dict__)
    print(user)
    # user = {"firstname": "Mr.", 'lastname': "My Father's Son"}

    return render_template("index.html", user=user)
                                      
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


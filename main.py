from flask import Flask, render_template 
from constants import *
import json

app = Flask(__name__)

@app.route("/") # we are using get method here
def index():
    test = Slacker(4, "HL Lee", "6 to 9", (6, 9), (7, 10))
    test2 = Slacker(5, "HY Lee", "1 to 9", (1, 9), (6, 10))
    test_arr = [test, test2]
    json_string = json.dumps([ob.__dict__ for ob in test_arr])
    print(json_string)
    # user = json.dumps(test.__dict__)
    # user2 = json.dumps(test2.__dict__)
    # test_arr = [user, user2]
    # print(test_arr)

    return render_template("index.html", user=json_string)
                                      
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


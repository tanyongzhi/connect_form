from flask import Flask, render_template, request, url_for, redirect
from constants import *
import json

from helper_functions import *

app = Flask(__name__)


@app.route("/")  # we are using get method here
def index():
    return render_template("index.html")

@app.route("/slacker_info")  # we are using get method here
def slacker_info():
    return render_template("slacker_info.html")

@app.route('/redirect_home',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      restaurant_latlon = get_latlon(result['restaurant'])
      address_latlon = get_latlon(result['destination'])
      dabaoer = DaBaoer(1, result['Name'], address_latlon, restaurant_latlon)

      slacker_list = get_optimized_slacker_list(all_slackers, dabaoer)

      return render_template("redirect_home.html", result = result)

@app.route("/slacker")  # we are using get method here
def slacker_list():
    test = Slacker(4, "HL Lee", "6 to 9", (6, 9), (7, 10))
    test2 = Slacker(5, "HY Lee", "1 to 9", (1, 9), (6, 10))
    test_arr = [test, test2]
    json_string = json.dumps([ob.__dict__ for ob in test_arr])
    print(json_string)
    return render_template("slacker_list.html", user=json_string)


@app.route("/slacker_add")  # we are using get method here
def add_slacker():
    return render_template("slacker_add.html")

@app.route("/redirect_home_add_slacker", methods = ['POST', 'GET'])  # we are using get method here
def redirect_home_add_slacker():
    if request.method == 'POST':
        result = request.form

        # convert addresses to latlon
        address_latlon = get_latlon(result['address'])
        restaurant_latlon = get_latlon(result['restaurant'])

        # create slacker
        slacker = Slacker(1, result['name'], result['time_period'],
                          result['address'], result['restaurant'],
                          address_latlon, restaurant_latlon, result['food_order'] )

        # append slacker to json (note: does not clear file upon app close)
        with open('data1.json', 'a') as f:
            json.dump(slacker.__dict__, f, indent=2)
            # f.write('{}\n'.format(json.dump(slacker.__dict__)))
        #
        # with open('sample.json', 'a') as sample:
        #     for dict in [d1, d2]:
        #         sample.write('{}\n'.format(json.dumps(dict)))
        #
        # print(file_to_json('data.json'))

        return render_template("redirect_home.html", result = result)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

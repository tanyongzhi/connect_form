from flask import Flask, render_template, request, url_for, redirect
from googlemaps import Client as GoogleMaps
from constants import *
import json

from helper_functions import *

app = Flask(__name__)


@app.route("/")  # we are using get method here
def index():
    return render_template("index.html")

@app.route("/dabaoer_add")  # we are using get method here
def slacker_info():
    return render_template("dabaoer_add.html")

@app.route('/redirect_home',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      restaurant_latlon = get_latlon(result['restaurant'])
      address_latlon = get_latlon(result['address'])
      dabaoer = DaBaoer(1, result['name'], result['address'], result['restaurant'],
                        address_latlon, restaurant_latlon)

      all_slackers = json_to_object_list("data.json")
      slacker_list = get_optimized_slacker_list(all_slackers, dabaoer)
      print(slacker_list)
      return render_template("slacker_list.html", user=beautify_json(slacker_list))

@app.route("/slacker")  # we are using get method here
def slacker_list():
    # test = Slacker(4, "Sean Shi Zhe Lee",  "6 to 9","Geylang Lor 6", "Cravings Pte Ltd", (1, 9), (1,4), "LZJD")
    # test2 = Slacker(4, "SH Sng", "6 to 9", "Geylang Lor 6", "Cravings Pte Ltd", (1, 9), (1,4), "DGRMDJJ")
    # test_arr = [test, test2]
    obj_list = json_to_object_list('data.json')
    return render_template("slacker_list.html", user=beautify_json(obj_list))


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
        with open('data.json', 'a') as f:
            json.dump(slacker.__dict__, f, indent=2)

        return render_template("index.html", result = result)

@app.route("/confirmation", methods = ['POST', 'GET'])  # we are using get method here
def confirmation():
    if request.method == 'POST':
        result = request.form
        return render_template("dabaoer_confirmation.html", name=result["name"], address=result["address"], order = result["order"])


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

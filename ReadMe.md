# Makan Tompang
| A community app that saves our energy in ordering take-out.

**Makan: To eat**

**Tompang: To hitch a ride**

Ever asked your roommate to buy you dinner on their way home? What if you could ask anyone in the community? Makan Tompang is an app that connects users who want a food delivery (buyers) with users who are already at restaurants (couriers). The app considers the route that the courier would take from the restaurant to their homes/destinations, and suggests buyers whose locations are on their route, in order of how much of a detour they would have to make to get to those buyers. 

We used Google Maps Geocoding API to convert location/street into geographic coordinates for the optimization function to be carried out. The UI design was made with Sketch

## Installation and Usage
Make sure your machine has Python 3 as well as pip installed.

Create a virtual environment:

`virtualenv venv`

Go into the venv folder:

`cd venv`

Activate the virtual environment:

`sourcebin/activate`

Make a copy of all Makan Tompang files in the venv folder. 

Then install the required packages:

`pip install -r requirements.txt`

Run our program (while in the venv). Control+click the link that shows up or copy into your browser:

`python main.py`

<!-- Install Flask:

`pip install Flask`

Install Jinja:

`pip install Jinja2`

Install Google Maps API:

```
pgit clone https://github.com/rochacbruno/Flask-GoogleMaps

cd Flask-GoogleMaps

python setup.py install
```--!>


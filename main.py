from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/") # we are using get method here
def index():
    name = "aspen"
    location = "cravings"
    return render_template("index.html", name=name, location=location)

if __name__ == "__main__":
    app.run()
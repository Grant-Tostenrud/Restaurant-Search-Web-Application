from flask import Flask, redirect, url_for, render_template, request

from src.searchfunction import search
from src.searchinfo import searchinfo

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        location = request.form["location"]
        term = request.form["term"]
        price = request.form["price"]
        open = request.form["open"]
        if (location == '') | (price == '') | (open == ''):
            return render_template("index.html")
        place = search(location, term, price, open)
        info = searchinfo(location, term, price, open)
        return redirect(url_for('restaurant', name=place, info=info))

    else:
        return render_template("index.html")


@app.route("/restaurant", methods=["POST", "GET"])
def restaurant():
    name = request.args['name']
    info = request.args['info']
    if request.method == "POST":
        return render_template("rmap.html")
    else:
        return render_template("restaurant.html", name=name, info=info)


@app.route("/map")
def map():
    return render_template("rmap.html")


if __name__ == "__main__":
    app.run(debug=True)
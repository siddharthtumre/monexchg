import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    countries = requests.get(
        "http://data.fixer.io/api/symbols?access_key=b9f63d6e3b33da599f7ed467ecfb8cac")
    countries = countries.json()
    return render_template("index.html", countries=countries)


@app.route("/convert", methods=["POST"])
def convert():

    # Query for currency exchange rate
    fromcurrency = request.form.get("from")
    tocurrency = request.form.get("to")
    con = f"{fromcurrency}_{tocurrency}"
    url = f"https://free.currconv.com/api/v7/convert?q={con}&compact=ultra&apiKey=d5677ce99f5782cc6088"
    res = requests.get(url)

    # Make sure currency is in response
    data = res.json()

    return jsonify({"rate": data[con]})


if __name__ == "__main__":
    app.run(debug=True)

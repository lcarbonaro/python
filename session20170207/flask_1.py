from flask import Flask, request, render_template
import requests, os

# create flask application object
app = Flask(__name__)

BASE_URL = "http://api.openweathermap.org/data/2.5/"
API_KEY = "your-openweathermap-api-key" # sign up for the openweathermap api key
URL_SLUG = "weather"

@app.route("/")
def home():
    return "We're up and running!" # use to test your flask app is up and running


@app.route("/weather", methods=["GET", "POST"])
def weather():
    results = None

    if request.method == "POST":
        city_name = request.form["city"]
        country_name = request.form["country"]
        location = "{0},{1}".format(city_name, country_name)
        payload = {
            "q":location,
            "APPID":API_KEY,
            "units":"metric"
        }

        req = requests.get(BASE_URL + URL_SLUG, params=payload)
        print("Test ", req.text)
        results = req.json()
        print(results)

    return render_template('index.html', data=results)



if __name__ == "__main__":
    ## should work for both for c9 and local
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

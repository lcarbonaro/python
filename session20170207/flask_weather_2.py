from flask import Flask
import requests, os

# create flask application object
app = Flask(__name__)

BASE_URL = "http://api.openweathermap.org/data/2.5/"
API_KEY = "your_openweathermap_api_key" # sign up for the openweathermap api key

@app.route("/")
def home():
    return "We're up and running!" # use to test your flask app is up and running


@app.route("/weather")
def weather():
    pass # will complete this section at meetup

if __name__ == "__main__":
    ## for local
    ##app.run()
    
    ## for c9
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))



from flask import Flask, request, render_template
import requests, os
from bs4 import BeautifulSoup

# create flask application object
app = Flask(__name__)

@app.route("/")
def home():
    return "Flask server up & running!" # use to test your flask app is up and running

@app.route("/scrape", methods=["GET"])
def scrapeData():
    
    # scrape current top movies
    results = []
    
    
    # scrape freebies from CL site
    results2 = []
    
    
    # scrape Python job listings
    results3 = []
    
    
    # scrape Toronto headlines
    results4 = []
    
    
    return render_template('index.html', moviedata=results, freebiedata=results2, jobsdata=results3, tweetsdata=results4)


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

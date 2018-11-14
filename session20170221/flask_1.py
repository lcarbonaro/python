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
    url = 'http://www.imdb.com/chart/boxoffice'
    cont = requests.get(url).content
    soup = BeautifulSoup(cont, 'html.parser')
    rows = soup.find('table', {"class":"chart"}).find('tbody').findAll('tr')
    for row in rows:
       movie_title = row.find('td',{"class":"titleColumn"}).text.strip()
       rec= {}
       rec['movie_title'] = movie_title
       results.append(rec)
    
    # scrape freebies from CL site
    results2 = []
    url = 'https://toronto.craigslist.ca/search/mss/zip'
    cont = requests.get(url).content
    soup = BeautifulSoup(cont, 'html.parser')
    rows = soup.findAll('li', {'class':'result-row'})
    for row in rows:
        a_tag = row.find('a', {'class':'result-title'})
        title = a_tag.text.strip()
        link = a_tag['href']   # 'https://toronto.craigslist.ca' + a_tag['href']
        rec = {}
        rec['title'] = title
        rec['link'] = link
        results2.append(rec)

    # scrape Python job listings
    results3 = []
    url = 'https://www.indeed.ca/jobs?q=python&l=Mississauga&radius=0'
    cont = requests.get(url).content
    soup = BeautifulSoup(cont, 'html.parser')
    divs = soup.find('td', {"id":"resultsCol"}).findAll("div", {"class":"result"})
    for div in divs:
        job_title = div.a.text.strip()
        job_link = 'https://www.indeed.ca' + div.a['href']
        rec = {}
        rec['job_title'] = job_title
        rec['job_link'] = job_link
        results3.append(rec)

    # scrape Toronto headlines
    results4 = []
    url = 'http://twitter.com/CityNews'
    cont = requests.get(url).content
    soup = BeautifulSoup(cont, 'html.parser')
    tweets = soup.find('div', {"class":"stream"}).findAll('p', {"class":"tweet-text"})
    for tweet in tweets:
        rec = {}
        rec['tweet'] = tweet.text.strip()
        try:
            a_tag = tweet.find('a', {"class":"twitter-timeline-link"})
            rec['link'] = a_tag['href']
        except:
            pass
        results4.append(rec)

    return render_template('index.html', moviedata=results, freebiedata=results2, jobsdata=results3, tweetsdata=results4)


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)

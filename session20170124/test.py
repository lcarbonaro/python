import os
from flask import Flask   ## sudo pip install Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Python Flask!"

if __name__ == "__main__":
    ## for local
    ##app.run()
    
    ## for c9
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))


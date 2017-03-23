from flask import Flask, request, render_template, url_for, redirect, session, \
                  flash, g
import sqlite3                  
import os

# for c9 users
host = os.getenv("IP", "0.0.0.0")
port = int(os.getenv("PORT", "8081"))

# configuration details
DATABASE = "books.db"

app = Flask(__name__)
app.config.from_object(__name__)

# create function to connect to database
def connect_db():
    return sqlite3.connect(app.config["DATABASE"])
    
    
# create views/routes
@app.route("/")
def login():
    return render_template("login.html")
    
    
@app.route("/main")
def main():
    return render_template("main.html")
    
    
if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
    
    


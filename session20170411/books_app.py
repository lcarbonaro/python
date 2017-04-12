from flask import Flask, request, render_template, url_for, redirect, session, \
                  flash, g
import sqlite3                  
import os

# for c9 users
host = os.getenv("IP", "0.0.0.0")
port = int(os.getenv("PORT", "8080"))

# configuration details
DATABASE = "books.db"
SECRET_KEY = "my_secret"

app = Flask(__name__)
app.config.from_object(__name__) # pulls in app configuration by looking for uppercase variables

# create function to connect to database
def connect_db():
    return sqlite3.connect(app.config["DATABASE"])
    
    
# create views/routes
@app.route("/")
def login():
    return render_template("login.html")
    
    
@app.route("/main")
def main():
    # create connection to db
    g.db = connect_db()
    # create a cursor to db
    conn = g.db.cursor()
    # execute a query against db
    conn.execute("SELECT * FROM books")
    books_data = conn.fetchall()
    
    # how do we want to display the data? In a list
    books = []
    # books data is a list of records that have same column items
    # i.e author, title, genre, price, best represented in a dictionary
    # iterate over books data and populate books list with data
    for book in books_data:
        books.append({"author":book[0], "title":book[1], "genre":book[2], "price":book[3]})
        
    # close db connection
    g.db.close()
    
    # pass books data to our template for use
    return render_template("main.html", books=books)


@app.route("/add", methods=["POST","GET"])
def add_book():

    msg = ""

    if request.method == "POST":

        # fetch form vars	
        author = request.form['author']
        title = request.form['title']
        genre = request.form['genre']
        price = request.form['price']

        # connect to db
        g.conn = connect_db()

        # create cursor
        cursor = g.conn.cursor()

        # execute SQL command
        cursor.execute("INSERT INTO books VALUES(?,?,?,?)",(author,title,genre,price) )

        # commit data changes
        g.conn.commit()

        # close db connection
        g.conn.close()

        msg = "Your new book record has been saved."

    return render_template("add.html",message=msg)

    

    
    
if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
    
    


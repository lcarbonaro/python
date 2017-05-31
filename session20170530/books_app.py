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
    
    
# create routes using @app.route decorator

# log in route
@app.route("/", methods=["GET","POST"])
def login():
    message = ''
    if request.method == 'POST':
        session.pop('username',None)   # clear session variable
        username = request.form["username"]
        password = request.form["password"]
        
        # temporarily set as vars
        # later read from database
        user_from_db = 'jsmith'
        pass_from_db = 'password'

        if username == user_from_db and password == pass_from_db:
            session['username'] = username # set session variable
            return redirect( url_for('main') )
        else:
            message = 'Invalid log-in credentials!'
            
    return render_template("login.html", msg=message)
    
# log out route
@app.route("/logout")
def logout():
    session.pop('username',None)   # clear session variable
    return redirect( url_for('login') )

@app.before_request
def before_request():
    # check if logged in (unless request is to log in) 
    # request.path gives url, e.g. '/'
    # request.endpoint gives function, e.g. 'login'
    print(request.endpoint)
    if 'username' not in session and request.endpoint != 'login':
        return redirect( url_for('login') )

# main route (list books)
@app.route("/main")
def main():
           
    # create connection to db
    g.conn = connect_db()
    # create a cursor to db
    cursor = g.conn.cursor()
    # execute a query against db
    cursor.execute("SELECT * FROM books")
    books_data = cursor.fetchall()
    
    # how do we want to display the data? In a list
    books = []
    # books data is a list of records that have same column items
    # i.e author, title, genre, price, best represented in a dictionary
    # iterate over books data and populate books list with data
    for book in books_data:
        books.append({"id":book[0], "author":book[1], "title":book[2], "genre":book[3], "price":book[4]})
        
    # close db connection
    g.conn.close()
    
    # pass books data to our template for use
    return render_template("main.html", books=books)
    
    
# add route to add book
@app.route("/add", methods=["GET","POST"])
def add_book():
    
    msg = ""
    if request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        genre = request.form["genre"]
        price = request.form["price"]
        
        g.conn = connect_db()
        cursor = g.conn.cursor()
        cursor.execute("INSERT INTO books (author, title, genre, price) VALUES(?, ?, ?, ?)", (author, title, genre, price))
        
        g.conn.commit()
        g.conn.close()
        msg = "Record successfully added!"
    
    return render_template('add.html', message=msg)
    
# edit route
@app.route("/edit", methods=["GET", "POST"])
def edit():
    
    msg = ""
    
    # get query string arguments
    book_id = request.args.get("book_id")
    author = request.args.get("author")
    title = request.args.get("title")
    genre = request.args.get("genre")
    price = request.args.get("price")
    
    book = {
        "book_id": book_id,
        "author":author,
        "title":title,
        "genre":genre,
        "price":price
    }
    
    if request.method == "POST":
        # get the data from form
        book_id = request.form["book_id"]
        author = request.form["author"]
        title = request.form["title"]
        genre = request.form["genre"]
        price = request.form["price"]
        
        # connect db and update record
        g.conn = connect_db()
        cursor = g.conn.cursor()
        cursor.execute("UPDATE books SET author=?, title=?, genre=?, price=? WHERE id=?", (author, title, genre, price,book_id))
        
        g.conn.commit()
        g.conn.close()
        
        book = {
            "book_id": book_id,
            "author":author,
            "title":title,
            "genre":genre,
            "price":price
        }
        
        msg = "Record successfully updated!"
    
    return render_template('edit.html', book_record=book, message=msg)
        
# delete route
@app.route("/delete", methods=["GET", "POST"])
def delete():
    
    # get query string arguments
    book_id = request.args.get("book_id")
    author = request.args.get("author")
    title = request.args.get("title")
    genre = request.args.get("genre")
    price = request.args.get("price")
    
    book = {
        "book_id": book_id,
        "author":author,
        "title":title,
        "genre":genre,
        "price":price
    }
    
    if request.method == "POST":
        
        # get the data from form
        book_id = request.form["book_id"]
        
        # connect db and delete record
        g.conn = connect_db()
        cursor = g.conn.cursor()
        cursor.execute("DELETE FROM books WHERE id=?", (book_id))
        
        g.conn.commit()
        g.conn.close()
        
        return redirect( url_for('main') )
    
    return render_template('delete.html', book_record=book)



# start the Flask application    
if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
    
    

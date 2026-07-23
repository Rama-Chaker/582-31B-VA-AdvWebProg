import os
from dotenv import load_dotenv

from flask import (Flask, flash, redirect, render_template, request, url_for)
from flask_login import (LoginManager, current_user, login_required, login_user, logout_user)

from models import db, User, Book

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shelf.db"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# db
db.init_app(app)

# login
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

with app.app_context():
    # create the tables
    db.create_all()


#### Loading User
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


#### Registration Validation
def validate_password(password):
    if len(password) < 8:
        return "Password must contain at least 8 characters."
    
    if len(password) > 20:
        return "Password must contain at most 20 characters."
    
    if not any(character.isupper() for character in password):
        return "Password must contain at least an uppercase letter."
    
    if not any(character.isdigit() for character in password):
        return "Password must contain a digit."
    
    return None


#### Base route
@app.route("/")
def base():
    return render_template("base.html")


#### Registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("books"))
    
    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        errors = []

        if not username:
            errors.append("Username is required")

        if len(username) > 100:
            errors.append("Username may contain at most 100 characters.")
        
        if any(character.isspace() for character in username):
            errors.append("Username may not contain whitespace")

        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            errors.append("That username is already in use!")

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            errors.append("That email is already registered.")

        password_error = validate_password(password)
        if password_error:
            errors.append(password_error)

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template("register.html", username=username, email=email)
        
        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Your account has been created!!!", "success")

        return redirect(url_for("login"))
    
    return render_template("register.html")


#### Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("books"))
    
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            flash("Invalid username or password", "error")
            return render_template("login.html", username=username)
        
        login_user(user)

        flash("Your now logged in.", "success")

        return redirect(url_for("books"))
    
    return render_template("login.html")


#### Logout route
@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("base"))


#### View Reading List / Books
@app.route("/books")
@login_required
def books():
    user_books = Book.query.filter_by(user_id=current_user.id).all()
    return render_template("books.html", books=user_books)


#### Add a New Book
@app.route("/books/new", methods=["GET", "POST"])
@login_required
def new_book():
    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        note = request.form.get("note", "").strip()
        status = request.form.get("status", "Want to read")

        errors = []

        if not title:
            errors.append("Title is required.")
        elif len(title) > 100:
            errors.append("Title must be 100 characters or less.")

        if not author:
            errors.append("Author is required.")
        elif len(author) > 100:
            errors.append("Author must be 100 characters or less.")

        if note and len(note) > 1000:
            errors.append("Note must be 1,000 characters or less.")

        valid_statuses = ["Want to read", "Reading", "Finished"]
        if status not in valid_statuses:
            errors.append("Invalid reading status.")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template("book_form.html", title=title, author=author, note=note, status=status)

        book = Book(
            title=title,
            author=author,
            note=note if note else None,
            status=status,
            user_id=current_user.id
        )

        db.session.add(book)
        db.session.commit()

        flash("Book added to your reading list!", "success")
        return redirect(url_for("books"))

    return render_template("book_form.html")


#### Edit a Book
@app.route("/books/<int:book_id>/edit", methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    book = db.session.get(Book, book_id)

    if book is None or book.user_id != current_user.id:
        flash("Book not found or unauthorized.", "error")
        return redirect(url_for("books"))

    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        note = request.form.get("note", "").strip()
        status = request.form.get("status", "Want to read")

        errors = []

        if not title:
            errors.append("Title is required.")
        elif len(title) > 100:
            errors.append("Title must be 100 characters or less.")

        if not author:
            errors.append("Author is required.")
        elif len(author) > 100:
            errors.append("Author must be 100 characters or less.")

        if note and len(note) > 1000:
            errors.append("Note must be 1,000 characters or less.")

        valid_statuses = ["Want to read", "Reading", "Finished"]
        if status not in valid_statuses:
            errors.append("Invalid reading status.")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template("book_edit.html", book=book)

        book.title = title
        book.author = author
        book.note = note if note else None
        book.status = status

        db.session.commit()

        flash("Book updated successfully!", "success")
        return redirect(url_for("books"))

    return render_template("book_edit.html", book=book)


#### Delete a Book
@app.route("/books/<int:book_id>/delete", methods=["POST"])
@login_required
def delete_book(book_id):
    book = db.session.get(Book, book_id)

    if book is None or book.user_id != current_user.id:
        flash("Book not found or unauthorized.", "error")
        return redirect(url_for("books"))

    db.session.delete(book)
    db.session.commit()

    flash("Book deleted from your reading list.", "success")
    return redirect(url_for("books"))
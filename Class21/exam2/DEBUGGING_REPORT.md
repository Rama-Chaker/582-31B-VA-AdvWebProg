## SQLALCHEMY_DATABASE_URL
**File: app.py**
**Problem:**
app.config was using: "SQLALCHEMY_DATABASE_URL" **Fix:**
"SQLALCHEMY_DATABASE_URI"
**Test:**
Before changing to URI it was giving me this:
 File "C:\Users\Rama\AppData\Local\Programs\Python\Python314\Lib\site-packages\flask_sqlalchemy\extension.py", line 355, in init_app
    raise RuntimeError(
        "Either 'SQLALCHEMY_DATABASE_URI' or 'SQLALCHEMY_BINDS' must be set."
    )
RuntimeError: Either 'SQLALCHEMY_DATABASE_URI' or 'SQLALCHEMY_BINDS' must be set.

After changing it to URI, the error didn't show again.

## SQLALCHEMY Initialization
**File: app.py**
**Problem:**
db = SQLAlchemy
**Fix:**
"db = SQLAlchemy(app)"
**Test:**
the app crashed with AttributeError: type object 'SQLAlchemy' has no attribute 'Model'. After adding (app), the Album class successfully inherits from db.Model, allowing the app to read the database structure.

## DB Issue (Part 1)
**File: app.py**
**Problem:**
year = db.Column(
        db.String(4),
        nullable=False
    )
**Fix:**
year = db.Column(
        db.Integer,
        nullable=False
    )
**Test:**
Logically, year value is an integer not a string

## DB Issue (Part 2)
**File: app.py**
**Problem:**
stock = db.Column(
        db.Integer,
        nullable=False,
        default="0"
    )
**Fix:**
stock = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )
**Test:**
Logically, Integer can't accpet strings values.

## Conditional Issue for in stock function
**File: app.py**
**Problem:**
def in_stock(self):
        return self.stock < 0
**Fix:**
def in_stock(self):
        return self.stock > 0
**Test:**
Logically, an item is in stock when teh stock is > 0

## Application Context
**File: app.py**
**Problem:**
with app.app_context:
**Fix:**
with app.app_context():
**Test:**
 File "C:\Users\Rama\Desktop\AEC Web Design Specialist\Block 3\Advanced Web Prog\GitHub\582-31B-VA-AdvWebProg\Class21\exam2\code\app.py", line 59, in <module>
    with app.app_context:

When fixed, app started (ran)

## Incorrect Query Parameter & Filter Column
**File: app.py**
**Problem:**
genre = request.args.get("category", "")
 albums = Album.query.filter_by(
            artist=genre
        ).all()
**Fix:**
genre = request.args.get("genre", "")
albums = Album.query.filter_by(
            genre=genre
        ).all()
**Test:**

## Missing Execution Parentheses on Query
**File: app.py**
**Problem:**
albums = Album.query.all
**Fix:**
albums = Album.query.all()
**Test:**
Logically, query.all() is a function so it needs a "()"

## HTTP Methods
**File: app.py**
**Problem:**
@app.route(
    "/albums/add",
    methods=["GET"]
)
**Fix:**
@app.route(
    "/albums/add",
    methods=["GET", "POST"]
)
**Test:**
Inside the function add album, we are using method POST so that's why I added  "POST" in app.route.

## Session.add() missing
**File: app.py**
**Problem:**
Was missing the add(album) session before the commit
**Fix:**
db.session.add(album)
**Test:**

## Redirecting issue
**File: app.py**
**Problem:**
return redirect(
            url_for("albums")
        )
**Fix:**
return redirect(
            url_for("index")
        )
**Test:**
"albums" route doesnn't exist

## Form value
**File: app.py**
**Problem:**
album.stock = request.form["amount"]
**Fix:**
album.stock = request.form["stock"]
**Test:**
The form has "stock" attribute not amount

## Rendering template issue for editing an album
**File: app.py**
**Problem:**
return render_template(
        "add_album.html",
        album=album
    )
**Fix:**
return render_template(
        "edit_album.html",
        album=album
    )
**Test:**
Used the edit template since it exists.

## Delete route issue
**File: app.py**
**Problem:**
@app.route(
    "/albums/<int:album_id>/delete",
    methods=["GET"]
)
**Fix:**
@app.route(
    "/albums/<int:album_id>/delete",
    methods=["POST"]
)
**Test:**
A delete should be done via POST method

## Conditional Issue for in stock function
**File: app.py**
**Problem:**
Missing commit session after the delete
**Fix:**
db.session.commit()
**Test:**
A commit is like a save method, so the chnages done cna be saved to the db
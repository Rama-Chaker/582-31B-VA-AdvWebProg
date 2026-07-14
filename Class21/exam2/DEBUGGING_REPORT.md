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

## Conditional Issue for in stock function

**File: app.py**
**Problem:**
def **repr**(self):
return self.id
**Fix:**
return f"<Album {self.title}>"
**Test:**
repr returns string rather than int

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
Inside the function add album, we are using method POST so that's why I added "POST" in app.route.

## Form Value Error

**File: app.py**
**Problem:**
album = Album(
title=request.form["album_name"],
artist=request.form["artist"],
genre=request.form["genre"],
year=request.form["year"],
stock=request.form["stock"]
)
**Fix:**
album = Album(
title=request.form["title"],
artist=request.form["artist"],
genre=request.form["genre"],
year=int(request.form["year"]),
stock=int(request.form["stock"])
)
**Test:**
In add album template : <input type="text" id="title" name="title" required>

so in order to meet the requirements of the form for the title we need to change from album name to title.
And also we are using int for both stiock and yer in the db , so we have to cast it to int.

## Session.add() missing

**File: app.py**
**Problem:**
Was missing the add(album) session before the commit
**Fix:**
db.session.add(album)
**Test:**
it is like a create function so it needs to be ther ein order to be able to add the album

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
"albums" route doesn't exist

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

## Session.commit() missing in edit

**File: app.py**
**Problem:**
Was missing the commit session
**Fix:**
db.session.commit()
**Test:**
we need to save changes, otherwise the changes weren't saved.

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
A delete should be done via POST method.

## Conditional Issue for in stock function

**File: app.py**
**Problem:**
Missing commit session after the delete
**Fix:**
db.session.commit()
**Test:**
A commit is like a save method, so the chnages done cna be saved to the db

## Template issue (Base Template)

**File: base.html**
**Problem:**
<a href="{{ url_for('albums') }}"> All Albums </a>
<a href="{{ url_for('add') }}"> Add Album </a>

**Fix:**
<a href="{{ url_for('index') }}"> All Albums </a>
<a href="{{ url_for('add_album') }}"> Add Album </a>

**Test:**
url_for() function in Flask doesn't look at URLs; it looks at the name of Python functions inside app.py.

## Issue with the conditional block

**File: index.html**
**Problem:**
{% if album %}

<article class="album-card">
    <h3>{{ item.name }}</h3>

    <p>
      <strong>Artist:</strong>
      {{ item.band }}
    </p>

  </article>

**Fix:**
{% if albums %}

<article class="album-card">
   <h3>{{ item.title }}</h3>

    <p>
      <strong>Artist:</strong>
      {{ item.artist }}
    </p>

  </article>

**Test:**
because in app.py we are looping through albums not album and also in app.py we are using albums=albums.
Also we have title and artist , not band and name

## Wrong Method for form was used

**File: add_album.html**
**Problem:**

<form method="GET" action="{{ url_for('add_album') }}">
**Fix:**
<form method="POST" action="{{ url_for('add_album') }}">
**Test:**
Each time I was adding an album it vanishes and also in app.py we are using this:
@app.route(
    "/albums/add",
    methods=["GET", "POST"]
)
def add_album():
    if request.method == "POST":

## Parentheses removed in index.html for the in stock property

**File: index.html**
**Problem:**
{% if item.in_stock() %} In stock {% else %} Sold out {% endif %}
**Fix:**
{% if item.in_stock %} In stock {% else %} Sold out {% endif %}
**Test:**
@property
def in_stock(self):
return self.stock > 0.
Properties acts like regular variables.

## Filtering Issues for the genre

**File: index.html**
**Problem:**
<select id="genre" name="category">

**Fix:**
<select id="genre" name="genre">

**Test:**
whne filtering we should hit /?genre=Electronic , that's why we need to chnage to genre rather than keeping it as category.

## Redirecting Issue after editing an album

**File: app.py**
**Problem:**
db.session.commit()
return redirect(
url_for(
"edit_album",
id=album.id
)
)

**Fix:**
db.session.commit()
return redirect(
url_for(
"index"
)
)

**Test:**
Because in the exam requirements , you told us to redirect to the homepage(album list) after the editing.

## Keeping Title and Artist names' issue

**File: edit_album.html**
**Problem:**

  <p>
    <label for="title">Title</label>

    <input
      id="title"
      name="title"
      type="text"
      value="{{ album.name }}"
      required
    />

  </p>

  <p>
    <label for="artist">Artist</label>

    <input
      id="artist"
      name="artist"
      type="text"
      value="{{ album.band }}"
      required
    />

  </p>

**Fix:**

  <p>
    <label for="title">Title</label>

    <input
      id="title"
      name="title"
      type="text"
      value="{{ album.title }}"
      required
    />

  </p>

  <p>
    <label for="artist">Artist</label>

    <input
      id="artist"
      name="artist"
      type="text"
      value="{{ album.artist }}"
      required
    />

  </p>

**Test:**
whenever i wanted to edit the album, the title and artist values are vanished. Now it works.

## Editing Stock Issues

**File: edit_album.html**
**Problem:**
name="quantity"
werkzeug.exceptions.BadRequestKeyError: 400 Bad Request: The browser (or proxy) sent a request that this server could not understand.
KeyError: 'stock'

**Fix:**
<input
      id="stock"
      name="stock"
      type="number"
      min="0"
      value="{{ album.stock }}"
      required
    />

**Test:**
In app.py we are using request.form["stock"], so Flask expects to pass a "stock" name value. So now it works.

from flask import Flask 

app = Flask(__name__)  

# we want an app with 3 routes
#   /  
#   /games
#       make it to return an HTML unordered list with 3 game names.
#   /students
# each route should return different HTML content.

@app.route("/")
def hello():
    return ""

@app.route("/games")
def games():
    return """
    <ul>
        <li>Chess</li>
        <li>Monopoly</li>
        <li>Clue</li>
    </ul>
    """

@app.route("/students")
def students():
    return """
    <ul>
        <li>Alice</li>
        <li>Bob</li>
        <li>Charlie</li>
    </ul>
    """
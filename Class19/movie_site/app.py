from flask import Flask
from main_routes import main
from movie_routes import movies

app = Flask(__name__)

# Registering both blueprints
app.register_blueprint(main)
app.register_blueprint(movies)

if __name__ == "__main__":
    app.run(debug=True)

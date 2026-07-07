from flask import Blueprint, render_template, request

movies = Blueprint("movies", __name__)

MOVIES = [
    {"title": "Inception", "genre": "Sci-Fi", "year": 2010},
    {"title": "Interstellar", "genre": "Sci-Fi", "year": 2014},
    {"title": "Spirited Away", "genre": "Animation", "year": 2001},
    {"title": "Whiplash", "genre": "Drama", "year": 2014},
    {"title": "Parasite", "genre": "Thriller", "year": 2019}
]

@movies.route("/movies")
def movie_list():
    genre = request.args.get("genre", "")
    
    # Simple loop matching the lecture search logic
    if genre:
        filtered = []
        for movie in MOVIES:
            if movie["genre"].lower() == genre.lower():
                filtered.append(movie)
    else:
        filtered = MOVIES

    return render_template("movies.html", title="Movies", movies=filtered, genre=genre)

@movies.route("/movie")
def movie_detail():
    title_query = request.args.get("title", "")
    
    # Find the specific movie matching the title query parameter
    selected_movie = None
    for movie in MOVIES:
        if movie["title"].lower() == title_query.lower():
            selected_movie = movie

    return render_template("movie_detail.html", title="Movie Detail", movie=selected_movie, search_title=title_query)

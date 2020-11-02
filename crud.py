
""" CRUD operation """
from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime

def create_user(email, password):
    """ Create and return a new user"""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """ Create and return a new movie """
    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)
    #no leading zeros when inputting release_date ex: datetime(2020, 11, 10)
    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    """returns all the movies"""

    return Movie.query.all()

def create_rating(user, movie, score):
    """Create and return a new score."""
    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_movie_by_id(movie_id):
    """returns movie by ID"""

    return Movie.query.get(movie_id)

def get_users():
    """returns all the movies"""

    return User.query.all()

def get_user_by_id(user_id):
    """ returns user by ID"""
    
    return User.query.get(user_id)

def get_user_by_email(email):
    """ returns users by email """
    return User.query.filter(User.email == email).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
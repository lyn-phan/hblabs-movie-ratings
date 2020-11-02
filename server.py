"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db 
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """ View Homepage """
    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    """ View all movies """
    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def display_movie(movie_id):
    """ Show details on a particular movie """
    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def all_users():
    """ Show users """
    users = crud.get_users()
    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def display_users(user_id):
    """ Shows user details """
    user = crud.get_user_by_id(user_id)
    return render_template('user_details.html', user=user) 

@app.route('/users', methods=['POST'])
def create_account():
    email = request.form.get('email')
    password = request.form.get('password')

    potential_user = crud.get_user_by_email(email)
    if potential_user:
        flash("Can't create account with that email")
    else:
        flash("Account successfully created. Please log in.")
        crud.create_user(email, password)
    
    return redirect('/')
    

    
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

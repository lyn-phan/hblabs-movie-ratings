""" script to seed database """
import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())
#create_movie(title, overview, release_date, poster_path)
    list_movies = []
    for movie in movie_data:
        format = '%Y-%m-%d'
        date = datetime.strptime(movie['release_date'],format)
        new_movie = crud.create_movie(movie['title'], movie['overview'], date, movie['poster_path'])
        list_movies.append(new_movie) #just movie or key into each aspect of the movie

for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'
    
    user = crud.create_user(email, password) #OR create_user(email,password) because we can't changed saved variable
    #randint a movie from list_movies
    #randint a score from range(1,5)
    #create_rating(user, rand_movie, rand_score)
    for i in range (10):
        rand_movie = choice(list_movies)
        rand_score = randint(1,5)
        crud.create_rating(user, rand_movie, rand_score)

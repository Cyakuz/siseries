from secrets import choice
from types import NoneType
from imdb import Cinemagoer # For IMDB API

from bs4 import BeautifulSoup  #For XML Datas
from tkinter import *
import random,sqlite3
from logs import Paths

## Class ##
ia = Cinemagoer()
ia.get_movie_infoset()
##Class ##

##Search Module##
def search(imdb_movie):
    try:
        movies = ia.search_movie(imdb_movie)
        ID = movies[0].movieID
        return ID
    except:
        print("index error")
    

def searchepisode(imdb_series,seasons,episode):
    series = ia.get_movie(search(imdb_series))
    ia.update(series, 'episodes')
    seasons = int(seasons)
    found_episode = series['episodes'][seasons][episode]
    title = found_episode.get('title')
    rating = found_episode.get('rating')
    return title, rating
    #Kullanılmadı...
## Search Module ##

## Data Module ##
def getmyimdb(imdb_movie):
    movie = ia.get_movie(search(imdb_movie))

    title = movie.get('title')

    director = movie.getAsXML('director')
    Bs_data = BeautifulSoup(director, "xml")
    name = Bs_data.find_all('name')
    rng = len(name)
    names = []
    for child in range(rng):
        names.append(name[child].getText())
    directors = names

    writer = movie.getAsXML('writer')
    Bs_data = BeautifulSoup(writer, "xml")
    name = Bs_data.find_all('name')
    rng = len(name)
    names = []
    for child in range(rng):
        names.append(name[child].getText())
    writers = names

    rating = movie.get('rating')

    genres = movie.get('genres')
    
    return title, directors,writers,rating,genres

def getmyseries(imdb_series):
    series = ia.get_movie(search(imdb_series))
    
    title = series.get('title')

    rating = series.get('rating')

    genres = series.get('genres')

    ia.update(series, 'episodes')

    seasons = len(series['episodes'])

    return title,rating,genres,seasons

def getkeyforrandomsearch(imdb_movie):
    movie = ia.get_movie(search(imdb_movie))
    genres = movie.get('genres')
    chosenGenres = choice(genres)
    return chosenGenres
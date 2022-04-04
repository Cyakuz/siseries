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

### Data Module ####

### Random Katagori Search ML BETA Kullanılmadı...###

# def itarateTable():
#     connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
#     cursor = connection.execute("select MovieName from movies")
#     records = cursor.fetchall()
#     global count
#     count = 0
#     movielist = []
#     for record in records:
#         movielist.append(record[0])
#     connection.commit()
#     connection.close()
#     return movielist

# def chosenGenre():
#     movies = itarateTable()
#     genres = []
#     for i in movies:
#         try:
#             x = getkeyforrandomsearch(i)
#             genres.append(x)
#         except:
#             pass
#     x = choice(genres)
#     return x

# def keysearch():
#     keywords = ia.search_keyword("drama")
#     movieKey= [keywords[0],keywords[1],keywords[2]]
#     movieKey= choice(keywords)
#     movies =ia.get_keyword(movieKey)
#     chosenMovie = choice(movies)
#     chosenMovie = str(chosenMovie)
#     movie = ia.get_movie(search(chosenMovie))
#     rating = int(movie.get('rating'))
#     # try:
#     #     vote = movie.data['votes']
#     # except:
#     #     vote = "none"
#     # while rating < 7:
#     #     movie = ia.get_movie(search(chosenMovie))
#     #     if rating >= 7:
#     #         print (chosenMovie)
#     #         break
#     #     else:
#     #         movie = ia.get_movie(search(chosenMovie))
#     #         rating = int(movie.get('rating'))
# ### Random Katagori Search ML BETA Kullanılmadı...###

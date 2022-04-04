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

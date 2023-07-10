from igdb.wrapper import IGDBWrapper
import json
############ ID ve Token 2 Aylık Kullanım #######################
client_id = ""
token = ""
########### ID ve Token 2 Aylık Kullanım ########################
########### IGDB Wrapper #######################
wrapper = IGDBWrapper(client_id, token)

class RequestIGDB:
    def getgameid(game):
        byte_array = wrapper.api_request(
                'games',
                'fields name, involved_companies; search "{tag}"; where version_parent = null;'.format(tag=game)
                )

        my_json = byte_array.decode('utf8').replace("'", '"') ######### Converting Bytes to String Array

        data = json.loads(my_json)   ############## Json Loads

        search = data[0] # Python Dict
        return search["id"]
    
    def rating(gameid):
        byte_array = wrapper.api_request(
        'games',
        'fields *; where id= {tag};'.format(tag=gameid)
        )
        my_json = byte_array.decode('utf8').replace("'", '"') ######### Converting Bytes to String Array
        data = json.loads(my_json)   ############## Json Loads
        search = data[0] # Python Dict
        return search["name"], search["rating"]
########## Genre
    def genreid(gameid):
        byte_array = wrapper.api_request(
        'games',
        'fields *; where id= {tag};'.format(tag=gameid)
        )
        my_json = byte_array.decode('utf8').replace("'", '"') ######### Converting Bytes to String Array
        data = json.loads(my_json)   ############## Json Loads
        search = data[0] # Python Dict
        return search["genres"]

    def genre(genreid):
        byte_array = wrapper.api_request(
        'genres',
        'fields *; where id= {tag};'.format(tag=genreid)
        )
        my_json = byte_array.decode('utf8').replace("'", '"') ######### Converting Bytes to String Array
        data = json.loads(my_json)   ############## Json Loads
        search = data[0] # Python Dict
        return search["name"]  
       
    def getgenre(gameid):
        ids = RequestIGDB.genreid(gameid)
        sites = []
        for i in ids:
            sites.append(RequestIGDB.genre(i))
        return sites 
########## Website   
    def websites(urlid):
        byte_array = wrapper.api_request(
            'websites',
            'fields *; where id= {tag};'.format(tag=urlid)
            )
        my_json = byte_array.decode('utf8').replace("'", '"') ######### Converting Bytes to String Array
        data = json.loads(my_json)   ############## Json Loads
        search = data[0] # Python Dict
        return search["url"]
    
    def webids(id):
        byte_array = wrapper.api_request(
            'games',
            'fields *; where id= {tag};'.format(tag=id)
        )
        my_json = byte_array.decode('utf8').replace("'", '"') ######### Converting Bytes to String Array
        data = json.loads(my_json)   ############## Json Loads
        search = data[0] # Python Dict
        return search["websites"]
    
    def getwebsites(gameid):
        ids = RequestIGDB.webids(gameid)
        sites = []
        for i in ids:
            sites.append(RequestIGDB.websites(i))
        return sites

def Igdb(id):    
    a = RequestIGDB.rating(id)
    b = RequestIGDB.getgenre(id)
    c = RequestIGDB.getwebsites(id)
    return a,b,c

def gameid(game_name):
    a = RequestIGDB.getgameid(game_name)
    return a

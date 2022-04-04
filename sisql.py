import sqlite3
from logs import Paths,Logs
class Sql:

    def SelectOps(esitmi):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select movieName from movies where movieName = '{mi}'".format(mi = esitmi))
        a = []
        for row in cursor:
            a.append(row)
        if len(a) != 0:
            Logs.errorlog("Aynı Filmi Eklediniz.")

    def SelectOps_Dizi(esitmi):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select diziadi from series where diziadi = '{mi}'".format(mi = esitmi))
        a = []
        for row in cursor:
            a.append(row)
        if len(a) != 0:
            Logs.errorlog("Aynı Diziyi Eklediniz.")
            
    def SelectOps_Anime(esitmi):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select taitoru from anime where taitoru = '{mi}'".format(mi = esitmi))
        a = []
        for row in cursor:
            a.append(row)
        if len(a) != 0:
            Logs.errorlog("Aynı Animeyi Eklediniz.")
    
    def SelectOpsWl(esitmi):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select movieName from watchlist where movieName = '{mi}'".format(mi = esitmi))
        a = []
        for row in cursor:
            a.append(row)
        if len(a) != 0:
            Logs.errorlog("Aynı Filmi Eklediniz.")

    def SelectOpsWl_Anime(esitmi):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select taitoru from watchlist_anime where taitoru = '{mi}'".format(mi = esitmi))
        a = []
        for row in cursor:
            a.append(row)
        if len(a) != 0:
            Logs.errorlog()
            
 #### TABLO OUŞTURMA ^^^######   
    def SelectTable(my_tree,tag,col):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select {col} from {tags}".format(tags=tag,col=col))
        records = cursor.fetchall()
        global count
        count = 0
        for record in records:
            if tag == "{tags}".format(tags=tag):
                if count % 2 == 0:
                  my_tree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
            count += 1
        connection.commit()
        connection.close()

    def SelectTableAnime(my_tree,tag,col):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select {col} from {tags}".format(tags=tag,col=col))
        records = cursor.fetchall()
        global count
        count = 0
        for record in records:
            if tag == "{tags}".format(tags=tag):
                if count % 2 == 0:
                  my_tree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3],record[4]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3],record[4]), tags=('oddrow',))
            count += 1
        connection.commit()
        connection.close()

    def SelectTableSeries(my_tree,tag,col):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select {col} from {tags}".format(tags=tag,col=col))
        records = cursor.fetchall()
        global count
        count = 0
        for record in records:
            if tag == "{tags}".format(tags=tag):
                if count % 2 == 0:
                  my_tree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2]), tags=('oddrow',))
            count += 1
        connection.commit()
        connection.close()

    def SelectTableW(my_tree):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select MovieName from Watchlist")
        records = cursor.fetchall()
        global count
        count = 0
        for record in records:
            if count % 2 == 0:
             my_tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
            else: 
             my_tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
            count += 1
        connection.commit()
        connection.close()

    def SelectTableSeriesWL(my_tree):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select SeriesName from watchlist_series")
        records = cursor.fetchall()
        global count
        count = 0
        for record in records:
            if count % 2 == 0:
             my_tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
            else: 
             my_tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
            count += 1
        connection.commit()
        connection.close()

    def SelectTableAnimeWL(my_tree):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select taitoru from Watchlist_anime")
        records = cursor.fetchall()
        global count
        count = 0
        for record in records:
            if count % 2 == 0:
             my_tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
            else: 
             my_tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
            count += 1
        connection.commit()
        connection.close()
 #### TABLO OUŞTURMA ^^^######   
    ################### Series Modeli İçin SQL Fonksiyonları #########################
    def ins_series_db(n,s,co):
        try:
            connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
            connection.execute("insert into series (diziadi, score, en_son_bolum) values ('{n}','{s}','{co}')".format(n=n,s=s,co=co))
            connection.commit()
            connection.close()
        except:
            pass

    def ins_serieswl_db(m):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        connection.execute("insert into watchlist_series (SeriesName) values ('{m}')".format(m=m))
        connection.commit()
        connection.close()
        
    ################### Anime Modeli İçin SQL Fonksiyonları #########################
    def ins_anime_db(n,s,ca,co):
        try:
            connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
            connection.execute("insert into anime (taitoru, reitingu, kategorii , waifu) values ('{n}','{s}','{ca}','{co}')".format(n=n,s=s,ca=ca,co=co))
            connection.commit()
            connection.close()
        except:
            pass

    def ins_animewl_db(m):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        connection.execute("insert into watchlist_anime (taitoru) values ('{m}')".format(m=m))
        connection.commit()
        connection.close()
        
    ################### Movie Modeli İçin SQL Fonksiyonları #########################
    def ins_movies_db(n,s,ca,co):
        try:
            connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
            connection.execute("insert into movies (movieName, score, catagory , comment) values ('{n}','{s}','{ca}','{co}')".format(n=n,s=s,ca=ca,co=co))
            connection.commit()
            connection.close()
        except:
            pass

    def ins_wl_db(m):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        connection.execute("insert into watchlist (movieName) values ('{m}')".format(m=m))
        connection.commit()
        connection.close()
    

import sqlite3
from logs import Paths,Logs

class SiSql:
    def __init__(self) -> None:
        pass
    
    def SelectOps(esitmi,cname,tname):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select {colname} from {tablename} where {colname} = '{mi}'".format(mi = esitmi, colname=cname,tablename=tname))
        a = []
        for row in cursor:
            a.append(row)
        if len(a) != 0:
            Logs.errorlog("Aynı Filmi Eklediniz.")

#s1-s2-s3-s4 tabloda gözükmesini istediğimiz columların sıralı sayısı durmak istediğimiz columdan sonraki her s değeri aynı olmalı.
#örnek 4 sütunlu bir tablo için SiSql.SelectTable(self.my_tree,tag,col,1,2,3,3)

    def SelectTable(my_tree,tag,col,s1,s2,s3,s4): 
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        cursor = connection.execute("select {col} from {tags}".format(tags=tag,col=col))
        records = cursor.fetchall()
        global count
        count = 0
        x = 0
        for i in records:
            if tag == "{tags}".format(tags=tag):
                if count % 2 == 0:
                  my_tree.insert(parent='', index='end', text='', values=(i[x],i[x+s1],i[x+s2],i[x+s3],i[x+s4]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', text='', values=(i[x],i[x+s1],i[x+s2],i[x+s3],i[x+s4]), tags=('oddrow',))
            count += 1
        connection.commit()
        connection.close()
        
class Sql:
################### Watchlist Tabloları İçin SQL Fonksiyonları #########################
    def ins_wl_db(m,tname,cname):
        connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        connection.execute("insert into {tablename} ({colname}) values ('{m}')".format(m=m,tablename=tname,colname=cname))
        connection.commit()
        connection.close()
################### Series Modeli İçin SQL Fonksiyonları #########################
    def ins_series_db(n,s,co):
        try:
            connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
            connection.execute("insert into series (diziadi, score, en_son_bolum) values ('{n}','{s}','{co}')".format(n=n,s=s,co=co))
            connection.commit()
            connection.close()
        except:
            pass
################### Anime Modeli İçin SQL Fonksiyonları #########################
    def ins_anime_db(n,s,ca,co):
        try:
            connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
            connection.execute("insert into anime (taitoru, reitingu, kategorii , waifu) values ('{n}','{s}','{ca}','{co}')".format(n=n,s=s,ca=ca,co=co))
            connection.commit()
            connection.close()
        except:
            pass  
################### Movie Modeli İçin SQL Fonksiyonları #########################
    def ins_movies_db(n,s,ca,co):
        try:
            connection = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
            connection.execute("insert into movies (movieName, score, catagory , comment) values ('{n}','{s}','{ca}','{co}')".format(n=n,s=s,ca=ca,co=co))
            connection.commit()
            connection.close()
        except:
            pass
from tkinter import *
from tkinter import ttk, Image
from PIL import Image, ImageTk
import sqlite3
from imdb1 import getmyimdb,getmyseries
from anilist1 import myanimelist,Waifu
from logs import Paths
from logs import Paths,Tbfs,Logs
from sisql import Sql
from request import Igdb, gameid

class App():

    def construct(self,geo,rh):
        self.root = Tk()
        self.tree = ttk.Treeview(self.root)
        self.root.title('SiSeries- TreeBase')
        self.root.geometry(geo)
        self.root.configure(bg = "#003D4D")
        # Add Some Style
        style = ttk.Style()
        style.theme_use('classic')
        style.configure("Treeview",
        background="#F8D559",
        foreground="black",
        rowheight= int(rh),
        fieldbackground="#F8D559"),
        style.map('Treeview',
        background=[('selected', "#347083")]),
        style.configure('Treeview.Heading', background="#F5CC3A")
    
    def table(self):
        tree_frame = Frame(self.root)
        tree_frame.pack(pady=10)
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)
        self.my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        self.my_tree.pack()
        tree_scroll.config(command=self.my_tree.yview)

    def foundItem(self,x):
        curItem = self.my_tree.focus()
        mydict = dict(self.my_tree.item(curItem))
        sons = mydict['values']
        x = sons[x]
        return x
    
    def tableDetails(self,a,b,c,d,e,aw,bw,cw,dw,ew):
        self.my_tree['columns'] = Tbfs.table("{a}".format(a=a), "{b}".format(b=b), "{c}".format(c=c), "{d}".format(d=d),"{e}".format(e=e))

        self.my_tree.column("#0", width=0, stretch=NO)
        if a != "":
            self.my_tree.column("{a}".format(a=a), anchor=W, width=aw)
            if b !="":
                self.my_tree.column("{b}".format(b=b), anchor=W, width=bw)
                if c !="":
                    self.my_tree.column("{c}".format(c=c), anchor=CENTER, width=cw)
                    if d !="":
                        self.my_tree.column("{d}".format(d=d), anchor=CENTER, width=dw)
                        if e !="":
                            self.my_tree.column("{e}".format(e=e), anchor=CENTER, width=ew)

        self.my_tree.heading("#0", text="", anchor=W)
        if a != "":
         self.my_tree.heading("{a}".format(a=a), text="{a}".format(a=a), anchor=W)
         if b !="":
                self.my_tree.heading("{b}".format(b=b), text="{b}".format(b=b), anchor=W)
                if c !="":
                    self.my_tree.heading("{c}".format(c=c), text="{c}".format(c=c), anchor=CENTER)
                    if d !="":
                        self.my_tree.heading("{d}".format(d=d), text="{d}".format(d=d), anchor=CENTER)
                        if e!="":
                            self.my_tree.heading("{e}".format(e=e), text="{e}".format(e=e), anchor=CENTER)

        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")
        

class Buttons(App):
#### Sıralama ########
    def up(self):
        rows = self.my_tree.selection()
        for row in rows:
            self.my_tree.move(row, self.my_tree.parent(row), self.my_tree.index(row)-1)
    
    def down(self):
        rows = self.my_tree.selection()
        for row in reversed(rows):
            self.my_tree.move(row, self.my_tree.parent(row), self.my_tree.index(row)+1)
### Sıralama #########
    
#### Deleting Procesing #########	

    def remove_wathed(self):
        
        conn = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        c = conn.cursor()
        item = self.foundItem(0)
        c.execute("DELETE from movies WHERE MovieName='{item}'".format(item = item))
        conn.commit()
        conn.close()

        x = self.my_tree.selection()[0]
        self.my_tree.delete(x)
    
    def remove_wathed_series(self):
        
        conn = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        c = conn.cursor()
        item = self.foundItem(0)
        c.execute("DELETE from series WHERE diziadi='{item}'".format(item = item))
        conn.commit()
        conn.close()

        x = self.my_tree.selection()[0]
        self.my_tree.delete(x)

    def remove_wathed_anime(self):
        
        conn = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        c = conn.cursor()
        item = self.foundItem(0)
        c.execute("DELETE from anime WHERE taitoru='{item}'".format(item = item))
        conn.commit()
        conn.close()

        x = self.my_tree.selection()[0]
        self.my_tree.delete(x)


#### Deleting Procesing  Bitti #####

#### IMDB BUTONU #####
    def value(self):
        try:
            item = self.foundItem(0)
            x = getmyimdb (item)

            class MakeImdb(Buttons):
                def __init__(self) -> None:
                    self.construct("850x70",3)
                    self.table()
                    self.tableDetails("Title","Directors","Writers","Rating","Genres",120,220,220,60,200)

                    self.my_tree.insert(parent='',index='end',iid=0,text='',
                    values= x)
                    self.root.mainloop()
            MakeImdb()
        except:
            Logs.errorlog("Film Bulunamadı.")
#### IMDB BUTONU BITTI ######     
#### IMDB BUTONU Series #####
    def valueS(self):
        try:
            item = self.foundItem(0)
            x = getmyseries(item)

            class MakeImdb(Buttons):
                def __init__(self) -> None:
                    self.construct("660x80",3)
                    self.table()
                    self.tableDetails("Title","Rating","Genres","Seasons","",240,70,220,90,50)

                    self.my_tree.insert(parent='',index='end',iid=0,text='',
                    values= x)
                    self.root.mainloop()
            MakeImdb()
        except:
            Logs.errorlog("Dizi Bulunamadı.")
#### IMDB Butonu Series Bitti ########
#### Anime Butonu ####   
    def valueAnime(self):
        try:
            item = self.foundItem(0)
            x = myanimelist(item)

            class MakeAnime(Buttons):
                def __init__(self) -> None:
                    self.construct("480x80",3)
                    self.table()
                    self.tableDetails("Taitoru","Airingu Taymu","Statusu","Episode Numburu","",150,120,120,60,60)

                    self.my_tree.insert(parent='',index='end',iid=0,text='',
                    values= x)
                    self.root.mainloop()
            MakeAnime()
        except:
            Logs.errorlog("Anime Bulunamadı.")

    def valueWaifu(self):
        item = self.foundItem(3)
        return item
        

###### Anime Butonu Bitti ##############
### Button Frames #########################
    def buttonframe(self):

        button_frame = LabelFrame(self.root, text="Commands", fg="#FFFFFF", font="sans 12 bold")
        button_frame.pack(fill="x", expand="yes", padx=10)
        button_frame.configure(background='#003D4D')

        move_up_button = Button(button_frame, background="#001318", text="Move Up",fg="White", command=self.up)
        move_up_button.grid(row=0, column=1, padx=5, pady=5)

        move_down_button = Button(button_frame, background="#001318", text="Move Down",fg="White", command=self.down)
        move_down_button.grid(row=0, column=2, padx=5, pady=5)

        del_entry_button = Button(button_frame, background="#001318", text="Delete", fg="White", command=self.remove_wathed)
        del_entry_button.grid(row=0, column=3, padx=5, pady= 5)

        make_entry_button = Button(button_frame, background="#001318", text="IMDB", fg="White", command= lambda : self.value())
        make_entry_button.grid(row=0, column=4, padx=5, pady= 5)

    def buttonframseries(self):

        button_frame = LabelFrame(self.root, text="Commands", fg="#FFFFFF", font="sans 12 bold")
        button_frame.configure(background='#003D4D')
        button_frame.pack(fill="x", expand="yes", padx=10)

        move_up_button = Button(button_frame, background="#001318", text="Move Up",fg="White", command=self.up)
        move_up_button.grid(row=0, column=1, padx=5, pady=5)

        move_down_button = Button(button_frame, background="#001318", text="Move Down",fg="White", command=self.down)
        move_down_button.grid(row=0, column=2, padx=5, pady=5)

        del_entry_button = Button(button_frame, background="#001318", text="Delete",fg="White", command=self.remove_wathed_series)
        del_entry_button.grid(row=0, column=3, padx=5, pady= 5)

        make_entry_button = Button(button_frame, background="#001318", text="IMDB",fg="White", command= lambda : self.valueS())
        make_entry_button.grid(row=0, column=4, padx=5, pady= 5)

    def buttonframeanime(self):

        button_frame = LabelFrame(self.root, text="Commands", fg="#FFFFFF", font="sans 12 bold")
        button_frame.pack(fill="x", expand="yes", padx=10)
        button_frame.configure(background='#003D4D')

        move_up_button = Button(button_frame, background="#001318", text="Move Up",fg="White", command=self.up)
        move_up_button.grid(row=0, column=1, padx=5, pady=5)

        move_down_button = Button(button_frame, background="#001318", text="Move Down",fg="White", command=self.down)
        move_down_button.grid(row=0, column=2, padx=5, pady=5)

        del_entry_button = Button(button_frame, background="#001318", text="Delete",fg="White", command=self.remove_wathed_anime)
        del_entry_button.grid(row=0, column=3, padx=5, pady= 5)

        make_entry_button = Button(button_frame, background="#001318", text="Myanimelist",fg="White", command= lambda : self.valueAnime())
        make_entry_button.grid(row=0, column=4, padx=5, pady= 5)   

        make_entry_button = Button(button_frame, background="#001318", text="Show My Waifu",fg="White", command= lambda : Waifu(self.valueWaifu()))
        make_entry_button.grid(row=0, column=5, padx=5, pady= 5)   


    def updateforbutton(self):
        data_frame = LabelFrame(self.root, text="Son Bölüm Güncelleme", fg="#FFFFFF", font="sans 12 bold")
        data_frame.pack(fill="x", expand="yes", padx=10)
        data_frame.configure(background='#003D4D')

        no_label = Label(data_frame, text="Bölüm No:")
        no_label.grid(row=0, column=0, padx=10, pady=10)
        no_entry = Entry(data_frame)
        no_entry.grid(row=0, column=0, padx=10, pady=10)

        make_entry_button = Button(data_frame,background="#001318", text="Getir",fg="White", command= lambda : getir())
        make_entry_button.grid(row=0, column=2, padx=10, pady= 10)

        make_entry_button = Button(data_frame, background="#001318", text="Güncelle",fg="White", command= lambda : update())
        make_entry_button.grid(row=0, column=3, padx=10, pady= 10)


        def update():
            s_item = self.foundItem(2)
            conn = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
            c = conn.cursor()
            c.execute("update series set en_son_bolum = '{update}' where en_son_bolum='{tag}'".format(tag=s_item, update=no_entry.get()))
            conn.commit()
            conn.close()
            no_entry.delete(0, END)
        
        def getir():
            try:
                no_entry.insert(0, self.foundItem(2))
            except:
                pass

    def updateforbutton_anime(self):
        data_frame = LabelFrame(self.root, text="Son Bölüm Güncelleme",fg="#FFFFFF", font="sans 12 bold")
        data_frame.pack(fill="x", expand="yes", padx=10)
        data_frame.configure(background='#003D4D')

        no_label = Label(data_frame, text="Bölüm No:")
        no_label.grid(row=0, column=0, padx=10, pady=10)
        no_entry = Entry(data_frame)
        no_entry.grid(row=0, column=0, padx=10, pady=10)

        make_entry_button = Button(data_frame, background="#001318", text="Getir",fg="White", command= lambda : getir())
        make_entry_button.grid(row=0, column=2, padx=10, pady= 10)

        make_entry_button = Button(data_frame, background="#001318", text="Güncelle",fg="White", command= lambda : update())
        make_entry_button.grid(row=0, column=3, padx=10, pady= 10)


        def update():
            s_item = self.foundItem(4)
            taitoru = self. foundItem(0)
            if  s_item == "None":
                conn = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
                c = conn.cursor()
                c.execute("update anime set en_son_bolum = '{update}' where taitoru= '{title}'".format(title=taitoru, update=no_entry.get()))
                conn.commit()
                conn.close()
            else:
                conn = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
                c = conn.cursor()
                c.execute("update anime set en_son_bolum = '{update}' where en_son_bolum='{tag}'".format(tag=s_item, update=no_entry.get()))
                conn.commit()
                conn.close()
                no_entry.delete(0, END)
        def getir():
            try:
                no_entry.insert(0, self.foundItem(4))
            except:
                pass
############# Button Frames Bitti ###############################

############# Watchlist Tabloları İçin Butonlar #######################

class ButtonforWL(Buttons):

    def remove_wl(self):
        
        conn = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        c = conn.cursor()
        item = self.foundItem(0)
        c.execute("DELETE from watchlist WHERE MovieName='{item}'".format(item = item))
        conn.commit()
        conn.close()

        x = self.my_tree.selection()[0]
        self.my_tree.delete(x)

    def remove_wl_series(self):
        
        conn = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        c = conn.cursor()
        item = self.foundItem(0)
        c.execute("DELETE from watchlist_series WHERE SeriesName='{item}'".format(item = item))
        conn.commit()
        conn.close()

        x = self.my_tree.selection()[0]
        self.my_tree.delete(x)
        
    def remove_wl_anime(self):
        
        conn = sqlite3.connect(Paths.relative_to_data("siseriesdb.db"))
        c = conn.cursor()
        item = self.foundItem(0)
        c.execute("DELETE from watchlist_anime WHERE taitoru='{item}'".format(item = item))
        conn.commit()
        conn.close()

        x = self.my_tree.selection()[0]
        self.my_tree.delete(x)

    def watchlistbuttons(self):
        button_frame = LabelFrame(self.root, text="Commands", fg="#FFFFFF", font="sans 12 bold")
        button_frame.pack(fill="x", expand="yes", padx=10)
        button_frame.configure(background='#003D4D')

        del_entry_button = Button(button_frame, text="Delete",background="#001318", fg="white", command=self.remove_wl)
        del_entry_button.grid(row=0, column=1, padx=5, pady= 5)


    def watchlist_seriesbuttons(self):
        button_frame = LabelFrame(self.root, text="Commands", fg="#FFFFFF", font="sans 12 bold")
        button_frame.pack(fill="x", expand="yes", padx=10)
        button_frame.configure(background='#003D4D')

        del_entry_button = Button(button_frame, text="Delete", background="#001318", fg="white", command=self.remove_wl_series)
        del_entry_button.grid(row=0, column=1, padx=5, pady= 5)
        
    def watchlist_animebuttons(self):
        button_frame = LabelFrame(self.root, text="Commands", fg="#FFFFFF", font="sans 12 bold")
        button_frame.pack(fill="x", expand="yes", padx=10)
        button_frame.configure(background='#003D4D')

        del_entry_button = Button(button_frame, text="Delete", background="#001318", fg="white", command=self.remove_wl_anime)
        del_entry_button.grid(row=0, column=1, padx=5, pady= 5)
###################### Watchist Butonlar Seriesi Bitti########################################
###################### Bitti #############################

###################### Tabloların Oluşturulmuş Halleri ########################
class Make1(Buttons):
    def __init__(self) -> None:
        self.construct("550x315",25)
        self.table()
        self.tableDetails("MovieName","Score","Catagory","Comment","",150,50,100,200,100)
        self.tags()
        self.buttonframe()
        self.root.mainloop()

    def tags(self):
        tag = "movies"
        col = "*"
        Sql.SelectTable(self.my_tree,tag,col)

class Make2(ButtonforWL):
    def __init__(self) -> None:
        self.construct("280x370",25)
        self.table()
        self.tableDetails("MovieName","","","","",250,50,50,50,50)
        self.tags()
        self.watchlistbuttons()

        self.root.mainloop()

    def tags(self):
        Sql.SelectTableW(self.my_tree)

class Make3(Buttons):
        def __init__(self) -> None:
            self.construct("540x400",25)
            self.table()
            self.tableDetails("diziadi","score","en_son_bolum","","",200,50,200,50,50)
            self.tags()
            self.buttonframseries()
            self.updateforbutton()
            self.root.mainloop()
        
        def tags(self):
            tag = "series"
            col = "*"
            Sql.SelectTableSeries(self.my_tree,tag,col)

class Make4(ButtonforWL):
    def __init__(self) -> None:
        self.construct("280x370",25)
        self.table()
        self.tableDetails("MovieName","","","","",250,50,50,50,50)
        self.tags()
        self.watchlist_seriesbuttons()
        self.root.mainloop()

    def tags(self):
        Sql.SelectTableSeriesWL(self.my_tree)

class Make5(Buttons):
    def __init__(self) -> None:
        self.construct("665x390",18)
        self.table()
        self.tableDetails("Taitoru","Reitingu","Kategorii","Waifu","en_son_bolum",150,50,100,200,100)
        self.tags()
        self.buttonframeanime()
        self.updateforbutton_anime()
        self.root.mainloop()

    def tags(self):
        tag = "anime"
        col = "*"
        Sql.SelectTableAnime(self.my_tree,tag,col)

class Make6(ButtonforWL):
    def __init__(self) -> None:
        self.construct("280x320",25)
        self.table()
        self.tableDetails("MovieName","","","","",250,50,50,50,50)
        self.tags()
        self.watchlist_animebuttons()
        self.root.mainloop()

    def tags(self):
        Sql.SelectTableAnimeWL(self.my_tree)

class Make7(Buttons):
    def __init__(self) -> None:
        self.construct("280x300",25)
        self.table()
        self.tableDetails("Title - Rating","Genres","Website","","",250,250,250,50,50)
        
#### Game BUTONU #####
class Game:
    def valueGame(item):
        x = gameid(item)
        try:
            y =  Igdb(x)
            class MakeGame(Buttons):
                def __init__(self) -> None:
                    self.construct("1300x80",15)
                    self.table()
                    self.tableDetails("Title + Score","Genres","Websites","","",300,250,700,60,200)

                    self.my_tree.insert(parent='',index='end',iid=0,text='',
                    values= y)
                    self.root.mainloop()
            MakeGame()
        except:
            Logs.errorlog("Oyun Bulunamadı.")
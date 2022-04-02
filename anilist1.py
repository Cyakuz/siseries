from cgitb import text
from multiprocessing import connection
from AnilistPython import Anilist
import pandas as pd
import numpy as np
import urllib.request
from tkinter import *
from PIL import Image, ImageTk
from tkinter import Canvas


anilist = Anilist()

def myanimelist(anime):
    data = anilist.get_anime(anime)
    pandadata = pd.DataFrame.from_dict(data)
    shortdata= pandadata.loc[:, ['name_romaji', 'ending_time','airing_status',"airing_episodes",'average_score']]
    x= shortdata.values
    y= x[0]
    z = "".join(y[0])
    name = z.replace(" ", "_")
    end = y[1]
    air = y[2]
    score = y[3]
    return name, end,air,score
    

class Waifu:
    def __init__(self,char) -> None:
        self.imageWaifu(char)

    def imageWaifu(self,char):
        w = Toplevel()  ########### Top Level Tkinter for Second Window
        w.geometry("320x410")


        frame = Frame(w, width=320, height=320)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        wImage = self.waifu(char)
        test = ImageTk.PhotoImage(wImage)

        label = Label(frame, image = test)
        label.pack()
        
        label = Label(frame, text="Eğer Aradığın Waifu Bu Değil İse Tam İsim Dene", fg="white", font="sans 10 bold", bg="red", justify= 'center')
        label.pack()
        label = Label(frame, text="Waifu'nu Bulamadıysak Üzgünüz :(", fg="white", font="sans 10 bold", bg="red", justify= 'center')
        label.pack()

        w.mainloop()

    def waifu_link(self,character):
        data = anilist.get_character("{c}".format(c=character))

        img= data["image"]
        return img

    def waifu(self,character):
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        url='{w}'.format(w=self.waifu_link(character))
        local='waifu.png'
        urllib.request.urlretrieve(url,local)
        
        img = Image.open("waifu.png")
        return img
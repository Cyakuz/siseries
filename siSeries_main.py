from tkinter import Tk, Canvas,PhotoImage
from subprocess import call
from logs import Paths

window = Tk()
window.geometry("1280x720")
window.configure(bg = "#003D4D")


    
canvas = Canvas(
    window,
    bg = "#003D4D",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_x = PhotoImage(
    file=Paths.relative_to_assets("mainbg.png"))
image_1 = canvas.create_image(
    640,
    360,
    image=image_image_x
)
########### BUTON KONUMLARI VE İSİMLERİ ######################
BUTTON_IMG_PATH_ANIME = Paths.relative_to_assets("btnanime.png")
BUTTON_IMG_PATH_FILM = Paths.relative_to_assets("btnfilm.png")
BUTTON_IMG_PATH_OYUN = Paths.relative_to_assets("btnoyun.png")
BUTTON_IMG_PATH_DIZI = Paths.relative_to_assets("btndizi.png")

BUTTON_HOVER_PATH_ANIME = Paths.relative_to_assets("btnanime1.png")
BUTTON_HOVER_PATH_FILM = Paths.relative_to_assets("btnfilm2.png")
BUTTON_HOVER_PATH_OYUN = Paths.relative_to_assets("btnoyun2.png")
BUTTON_HOVER_PATH_DIZI = Paths.relative_to_assets("btndizi2.png")

dizi_pic1 = PhotoImage(file=BUTTON_HOVER_PATH_DIZI)
dizi_pic2 = PhotoImage(file=BUTTON_IMG_PATH_DIZI)

anime_pic1 =PhotoImage(file=BUTTON_HOVER_PATH_ANIME)
anime_pic2 = PhotoImage(file=BUTTON_IMG_PATH_ANIME)

film_pic1 = PhotoImage(file=BUTTON_HOVER_PATH_FILM)
film_pic2 = PhotoImage(file=BUTTON_IMG_PATH_FILM)

oyun_pic1 = PhotoImage(file=BUTTON_HOVER_PATH_OYUN)
oyun_pic2 = PhotoImage(file=BUTTON_IMG_PATH_OYUN)

class Btn:
    def __init__(self,canvas,btnpath,x,y,img_obj, hov_obj,tag) -> None:
        self.img_obj = img_obj ############## TK -  PhotoImage Olarak Veriniz... Örn. img = PhotoImage(file=BUTTON_IMG_PATH_DIZI)
        self.hov_obj = hov_obj ############## TK -  PhotoImage Olarak Veriniz...
        self.canvas = canvas
        self.tag = tag
        self.button = PhotoImage(file= btnpath) ###########  Dosya Konumu Veriniz.... Örnek BUTTON_HOVER_PATH_DIZI = Paths.relative_to_assets("btndizi2.png")
        self.obj1 = canvas.create_image(x,y,image=self.button)
        self.canvas.tag_bind(self.obj1, '<Enter>', self.onObject) ####### Enter Event
        canvas.tag_bind(self.obj1, '<Leave>', self.onObject2)  ####### Leave Event
    
    def sub1(self):
        window.destroy()
        call(["python", "siMovies.py"])
    def sub2(self):
        window.destroy()
        call(["python", "siSeri.py"])
    def sub3(self):
        window.destroy()
        call(["python", "siAnime.py"])
    def sub4(self):
        window.destroy()
        call(["python", "siOyun.py"])
    
    
    def onObject(self,event):
        def pimg():
            self.canvas.itemconfig(self.obj1, image=self.img_obj)
        def click(event):
            if self.tag == "a":
                self.canvas.tag_bind(self.obj1, "<ButtonRelease-1>",
                            lambda event: self.sub1())
            elif self.tag == "b":
                        self.canvas.tag_bind(self.obj1, "<ButtonRelease-1>",
                    lambda event: self.sub2())
            elif self.tag == "c":
                        self.canvas.tag_bind(self.obj1, "<ButtonRelease-1>",
                    lambda event: self.sub3())  
            elif self.tag == "d":
                        self.canvas.tag_bind(self.obj1, "<ButtonRelease-1>",
                    lambda event: self.sub4()) 
        pimg()
        click(event="<ButtonRelease-1>")

    def onObject2(self,event):
        def pimg():
            self.canvas.itemconfig(self.obj1, image=self.hov_obj) 
        def click(event):
            if self.tag == "a":
                self.canvas.tag_bind(self.obj1, "<ButtonRelease-1>",
                            lambda event: self.sub1())
            elif self.tag == "b":
                        self.canvas.tag_bind(self.obj1, "<ButtonRelease-1>",
                    lambda event: self.sub2())
            elif self.tag == "c":
                        self.canvas.tag_bind(self.obj1, "<ButtonRelease-1>",
                    lambda event: self.sub3())  
            elif self.tag == "d":
                        self.canvas.tag_bind(self.obj1, "<ButtonRelease-1>",
                    lambda event: self.sub4())                 
        pimg()
        click(event="<ButtonRelease-1>")
        
try:
    Btn(canvas,BUTTON_IMG_PATH_DIZI,1130,180,dizi_pic1,dizi_pic2,"b")
    Btn(canvas,BUTTON_IMG_PATH_FILM,475,465,film_pic1,film_pic2,"a")
    Btn(canvas,BUTTON_IMG_PATH_ANIME,150,580,anime_pic1,anime_pic2,"c")
    Btn(canvas,BUTTON_IMG_PATH_OYUN,800,320,oyun_pic1,oyun_pic2,"d")
except:
    pass


window.resizable(False, False)
window.mainloop()
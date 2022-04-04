from tkinter import Tk, Canvas,PhotoImage
from subprocess import call
from logs import Paths,Btn

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

try:
    Btn(canvas,window,BUTTON_IMG_PATH_DIZI,1130,180,dizi_pic1,dizi_pic2,"b")
    Btn(canvas,window,BUTTON_IMG_PATH_FILM,475,465,film_pic1,film_pic2,"a")
    Btn(canvas,window,BUTTON_IMG_PATH_ANIME,150,580,anime_pic1,anime_pic2,"c")
    Btn(canvas,window,BUTTON_IMG_PATH_OYUN,800,320,oyun_pic1,oyun_pic2,"d")
except:
    pass


window.resizable(False, False)
window.mainloop()
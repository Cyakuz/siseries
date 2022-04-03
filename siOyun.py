from tkinter import  StringVar, Tk, Canvas, Entry,  PhotoImage, mainloop
from logs import Logs,Paths,CanvasButton
from tables import Game
### Class ###
class Movies:
    def __init__(self,name,score,catg,comment) -> None:
        self.name = name
        self.score = score
        self.catg = catg
        self.comment = comment
### Class ###

## Film Ekleme ##
def submit(): 
    n= Movies.name.get()
    Game.valueGame(n)
### GUI ###
window = Tk()

window.geometry("1280x720")
window.configure(bg = "#FCEABB")

Movies = Movies(StringVar(),StringVar(),StringVar(),StringVar())

### Canvas Ayarları ####
canvas = Canvas(window, bg = "#FCEABB", height = 720, width = 1280, bd = 0, highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)
image_image_x = PhotoImage(
    file=Paths.relative_to_assets("bg.png"))
image_1 = canvas.create_image(
    640,
    360,
    image=image_image_x
)
canvas.place(x = 0, y = 0)

image_image_not = PhotoImage(
    file=Paths.relative_to_assets("not1.png"))
image_1 = canvas.create_image(
    400.0,
    630.0,
    image=image_image_not
)

image_image_1 = PhotoImage(
    file=Paths.relative_to_assets("cbk4.png"))
image_1 = canvas.create_image(
    1055.0,
    360.0,
    image=image_image_1
)

##### Canvas Ayarları Bitti

### TextBox Başlama ####
entry_1 = Entry(
    bd=0,
    bg= "#003D4D",
    highlightthickness=0,
    textvariable= Movies.name
)
entry_1.place(
    x=190.0,
    y=240.0,
    width=250.0,
    height=40.0
)
entry_image_1 = PhotoImage(
    file=Paths.relative_to_assets("entry_oyunadi1.png"))
entry_bg_1 = canvas.create_image(
    400,
    240,
    image=entry_image_1
)
#### Text Box Bitiş ####

############## BUTONLAR ##############
BUTTON_IMG_PATH_ARA = Paths.relative_to_assets("ara.png")


button_1 = CanvasButton(canvas, 200 , 350, BUTTON_IMG_PATH_ARA, command=lambda: submit())


##### BUTONLAR BİTTİ ########

window.resizable(False, False)
window.mainloop()
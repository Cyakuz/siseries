from cProfile import label
from tkinter import Label, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, mainloop
from logs import Logs,Paths,CanvasButton
from tables import Make1, Make2
from sisql import Sql
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
    s= Movies.score.get()
    ca= Movies.catg.get()
    co = Movies.comment.get()
    mi = n
    Sql.SelectOps(mi)
    return Sql.ins_movies_db(n,s,ca,co)

def submitwl():
    m = Movies.name.get()
    mi = m
    Sql.SelectOpsWl(mi)
    return Sql.ins_wl_db(m)
### Film Ekleme ####
### GUI ###
window = Tk()

window.geometry("1280x720")
window.configure(bg = "#F5CC3A")

Movies = Movies(StringVar(),StringVar(),StringVar(),StringVar())

### Canvas Ayarları ####
canvas = Canvas(window, bg = "#F5CC3A", height = 720, width = 1280, bd = 0, highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.place(x = 0, y = 0)
image_image_x = PhotoImage(
    file=Paths.relative_to_assets("bg.png"))
image_1 = canvas.create_image(
    640,
    360,
    image=image_image_x
)
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=Paths.relative_to_assets("cbk2.png"))
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
    x=65.0,
    y=240.0,
    width=250.0,
    height=40.0
)
entry_image_1 = PhotoImage(
    file=Paths.relative_to_assets("entry_filmadi1.png"))
entry_bg_1 = canvas.create_image(
    180,
    240,
    image=entry_image_1
)
entry_image_2 = PhotoImage(
    file=Paths.relative_to_assets("entry_21.png"))
entry_bg_2 = canvas.create_image(
    180,
    345.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#003D4D",
    highlightthickness=0,
    textvariable= Movies.score
)
entry_2.place(
    x=65.0,
    y=345.0,
    width=250.0,
    height=40.0
)
entry_image_3 = PhotoImage(
    file=Paths.relative_to_assets("kategori1.png"))
entry_bg_3 = canvas.create_image(
    180,
    450,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#003D4D",
    highlightthickness=0,
    textvariable= Movies.catg
)
entry_3.place(
    x=65.0,
    y=450.0,
    width=250.0,
    height=40.0
)
entry_image_4 = PhotoImage(
    file=Paths.relative_to_assets("yorum1.png"))
entry_bg_4 = canvas.create_image(
    180,
    555,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#003D4D",
    highlightthickness=0,
    textvariable= Movies.comment
)
entry_4.place(
    x=65.0,
    y=555.0,
    width=250.0,
    height=40.0
)
#### Text Box Bitiş ####
### Başlıklar ####
image_image_4 = PhotoImage(
    file=Paths.relative_to_assets("yenifilm1.png"))
image_4 = canvas.create_image( 175, 150, image=image_image_4 )

image_image_5 = PhotoImage(
    file=Paths.relative_to_assets("planlama1.png"))
image_5 = canvas.create_image(
    580,
    60,
    image=image_image_5
)
### Başlıklar ####
##### TEXT BOX İKİNCİ KISIM #####
image_image_6 = PhotoImage(
    file=Paths.relative_to_assets("izlediklerim1.png"))
image_6 = canvas.create_image(
    580.0,
    310.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=Paths.relative_to_assets("izlemelistesi1.png"))
image_7 = canvas.create_image(
    580.0,
    470.0,
    image=image_image_7
)

entry_image_5 = PhotoImage(
    file=Paths.relative_to_assets("izlenecekfilm1.png"))
entry_bg_5 = canvas.create_image(
    580.5,
    140.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#003D4D",
    highlightthickness=0,
    textvariable= Movies.name
)
entry_5.place(
    x=475.0,
    y=150.0,
    width=230.0,
    height=40.0
)
##### TEXT BOX İKİNCİ KISIM #####

############## BUTONLAR ##############
BUTTON_IMG_PATH_EKLE = Paths.relative_to_assets("ekle1.png")
BUTTON_IMG_PATH_GETIR = Paths.relative_to_assets("getir1.png")

button_1 = CanvasButton(canvas, 173 , 595, BUTTON_IMG_PATH_EKLE, command=lambda: submit())
button_2 = CanvasButton(canvas, 560 , 180, BUTTON_IMG_PATH_EKLE, command=lambda: submitwl()) 
button_3 = CanvasButton(canvas, 560 , 330, BUTTON_IMG_PATH_GETIR, command=lambda: Make1()) 
button_4 = CanvasButton(canvas, 560 , 490, BUTTON_IMG_PATH_GETIR, command=lambda: Make2())
##### BUTONLAR BİTTİ ########

window.resizable(False, False)
window.mainloop()
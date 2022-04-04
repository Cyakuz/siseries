from tkinter import Canvas, Label, Tk, mainloop, PhotoImage
from pathlib import Path
import tkinter as tk
from subprocess import call


class Logs:
    def errorlog(errorText):
        logwindow = Tk()
        logwindow.geometry("200x80")
        logwindow.title("UYARI")
        logwindow.configure(bg = "#F5CC3A")
        Label(logwindow, text= "UYARI!", fg="#0000FF",bg="yellow").pack()
        label = Label(logwindow, text = errorText)
        label.config(fg="#0000FF")
        label.config(bg="yellow")
        label.pack(pady = 10)
        logwindow.resizable(False, False)
        mainloop()

class Paths:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    DATA_PATH = OUTPUT_PATH / Path("./datas")

    def relative_to_assets(path: str) -> Path:
        return Paths.ASSETS_PATH / Path(path)

    def relative_to_data(path: str) -> Path:
        return Paths.DATA_PATH / Path(path)

class Tbfs:
    def table(a,b,c,d,e):
        col = [a,b,c,d,e]
        columbs = []
        for i in col:
            if i != "":
                columbs.append(i)
        tup = tuple(columbs)
        return (tup)

class CanvasButton:

    flash_delay = 150  # Milliseconds.

    def __init__(self, canvas, x, y, image_path, command, state=tk.NORMAL):
        self.canvas = canvas
        self.btn_image = tk.PhotoImage(file=image_path)
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='nw', state=state,
                                                      image=self.btn_image)
        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonRelease-1>",
                        lambda event: (self.flash(), command()))
    def flash(self):
        self.set_state(tk.HIDDEN)
        self.canvas.after(self.flash_delay, self.set_state, tk.NORMAL)

    def set_state(self, state):
        """ Change canvas button image's state.

        Normally, image objects are created in state tk.NORMAL. Use value
        tk.DISABLED to make it unresponsive to the mouse, or use tk.HIDDEN to
        make it invisible.
        """
        self.canvas.itemconfigure(self.canvas_btn_img_obj, state=state)
        
class Btn:
    def __init__(self,canvas,window,btnpath,x,y,img_obj, hov_obj,tag) -> None:
        self.img_obj = img_obj ############## TK -  PhotoImage Olarak Veriniz... Örn. img = PhotoImage(file=BUTTON_IMG_PATH_DIZI)
        self.hov_obj = hov_obj ############## TK -  PhotoImage Olarak Veriniz...
        self.canvas = canvas
        self.tag = tag
        self.button = PhotoImage(file= btnpath) ###########  Dosya Konumu Veriniz.... Örnek BUTTON_HOVER_PATH_DIZI = Paths.relative_to_assets("btndizi2.png")
        self.obj1 = canvas.create_image(x,y,image=self.button)
        self.canvas.tag_bind(self.obj1, '<Enter>', self.onObject) ####### Enter Event
        canvas.tag_bind(self.obj1, '<Leave>', self.onObject2)  ####### Leave Event
        self.window = window
    
    def sub1(self):
        self.window.destroy()
        call(["python", "siMovies.py"])
    def sub2(self):
        self.window.destroy()
        call(["python", "siSeri.py"])
    def sub3(self):
        self.window.destroy()
        call(["python", "siAnime.py"])
    def sub4(self):
        self.window.destroy()
        call(["python", "siOyun.py"])
    def submain(self):
        self.window.destroy()
        call(["python","siSeries_main.py"])
    
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
            elif self.tag == "e":
                        self.canvas.tag_bind(self.obj1, "<ButtonRelease-1>",
                    lambda event: self.submain()) 
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
            elif self.tag == "e":
                        self.canvas.tag_bind(self.obj1, "<ButtonRelease-1>",
                    lambda event: self.submain())              
        pimg()
        click(event="<ButtonRelease-1>")
class Homebutton():
    def __init__(self,canvas,window) -> None:
        self.canvas = canvas
        self.window = window
        self.homebutton()
        
        
    def homebutton(self):
        BUTTON_IMG_PATH_MAIN = Paths.relative_to_assets("home.png")
        BUTTON_HOVER_PATH_MAIN = Paths.relative_to_assets("homehover.png")
        main_pic1 = PhotoImage(file=BUTTON_HOVER_PATH_MAIN)
        main_pic2 = PhotoImage(file=BUTTON_IMG_PATH_MAIN)

        Btn(self.canvas,self.window,BUTTON_IMG_PATH_MAIN,800,670,main_pic1,main_pic2,"e")
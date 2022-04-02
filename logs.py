from distutils.log import Log
from logging import exception
from tkinter import Label, Tk, mainloop
from pathlib import Path
import tkinter as tk


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
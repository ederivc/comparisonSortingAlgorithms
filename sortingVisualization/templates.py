from tkinter import Canvas
import tkinter
import GUI

class Canvass:
    def __init__(self, window, color, relx, relwidth, relheight) -> None:
        self.canvas = Canvas(window, bg = color)
        self.canvas.place(relx = relx, relwidth = relwidth, relheight = relheight)

class Data:
    def __init__(self) -> None:
        self.start = True

class Comparisons:
    def __init__(self) -> None:
        self.number = 0

class List:
    def __init__(self) -> None:
        self._list = []  

class Setup:
    MAX_WIDTH = 1600
    MAX_HEIGHT = 1000

    def __init__(self, window: tkinter.Tk) -> None:
        window.minsize(self.MAX_WIDTH, self.MAX_HEIGHT)
        window.maxsize(self.MAX_WIDTH, self.MAX_HEIGHT)

        window.title("Algorithm visualization")

        #Initialize(window)


class Initialize:
    def __init__(self, root: tkinter.Tk) -> None:
        canvas_1 = Canvass(root,"#de594d", 0, 0.33, 0.8)
        canvas_2 = Canvass(root, "#32a6ac", 0.33, 0.66, 0.8)
        canvas_3 = Canvass(root,"#ca48cc", 0.67, 0.9, 0.8)
        GUI.Window(root, canvas_1, canvas_2, canvas_3)
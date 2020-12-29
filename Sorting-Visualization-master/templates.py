import GUI
import tkinter

from typing import Any
from tkinter import Canvas

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

class Time:
    def __init__(self) -> None:
        self.time_now = 0

class Setup:
    MAX_WIDTH = 1600
    MAX_HEIGHT = 1000

    def __init__(self, window: tkinter.Tk) -> None:
        window.minsize(self.MAX_WIDTH, self.MAX_HEIGHT)
        window.maxsize(self.MAX_WIDTH, self.MAX_HEIGHT)

        window.title("Algorithm visualization")


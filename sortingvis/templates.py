import tkinter

from typing import Any
from tkinter import Canvas, PhotoImage

class Canvass(tkinter.Canvas):
    def __init__(self, window, color, relx, relwidth, relheight) -> None:
        super().__init__(master=window)
        self.config(bg = color)
        self.place(relx = relx, relwidth = relwidth, relheight = relheight)

class Data:
    def __init__(self) -> None:
        self.start = True

class Comparisons:
    def __init__(self) -> None:
        self.number = 0

class List:
    def __init__(self) -> None:
        self.value = []  
         
class Time:
    def __init__(self) -> None:
        self.time_now = 0

class Sorting:
    def __init__(self) -> None:
        self.status = "waiting"

class Setup:
    MAX_WIDTH = 1600
    MAX_HEIGHT = 1000

    def __init__(self, window: tkinter.Tk) -> None:
        window.minsize(self.MAX_WIDTH, self.MAX_HEIGHT)
        window.maxsize(self.MAX_WIDTH, self.MAX_HEIGHT)

        window.title("SORTING VISUALIZATION")

class ChangeColor:
    def __init__(self, _list: list, **kwargs: Any) -> None:
        _list[0][0].config(bg=kwargs["up_1"])
        _list[0][1].config(bg=kwargs["up_2"])
        _list[0][2].config(bg=kwargs["up_3"])

        for label in _list[1:]:
            label.config(bg=kwargs["down"])

class Objects:
    def __init__(self) -> None:
        self.start_drawing1 = Data()
        self.start_drawing2 = Data()
        self.start_drawing3 = Data()

        self.comparisons_1 = Comparisons()
        self.comparisons_2 = Comparisons()
        self.comparisons_3 = Comparisons()

        self.list_1 = List()
        self.list_2 = List()
        self.list_3 = List()

        self.info_data_1 = List()
        self.info_data_2 = List()
        self.info_data_3 = List()

        self.random_list = List()

        self.time_1 = Time()
        self.time_2 = Time()
        self.time_3 = Time()

        self.is_sorting_1 = Sorting()
        self.is_sorting_2 = Sorting()
        self.is_sorting_3 = Sorting()

        self.change_color = Data()

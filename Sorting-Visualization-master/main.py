import GUI
import templates
import tkinter as tk

from templates import Canvass


if __name__ == "__main__":

    window = tk.Tk()

    canvas_1 = Canvass(window,"#9067c6", 0, 0.33, 0.8)
    canvas_2 = Canvass(window, "#8d86c9", 0.33, 0.66, 0.8)
    canvas_3 = Canvass(window,"#9067c6", 0.67, 0.9, 0.8)
    templates.Setup(window)

    app = GUI.Application(window, canvas_1, canvas_2, canvas_3)

    app.start() 
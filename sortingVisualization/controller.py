import re
import GUI
import threads 
import time
from tkinter import Canvas, Button
from tkinter import messagebox as mBox

def draw_info(comp_value: int, color: list, canva: Canvas, _list: list) -> None:
    canva.canvas.delete("all")
    x = 25
    y = 60
    for key, value in enumerate(_list):
        canva.canvas.create_rectangle(x, value[1], y, 10, fill= color[key])
        canva.canvas.create_text(
            x, value[1]+20, anchor="sw", text=value[0], fill="black"
        )
        canva.canvas.create_text(
            400, 580, anchor="sw", text="Comparisons", fill="black"
        )
        canva.canvas.create_text(
            400, 600, anchor="sw", text=comp_value, fill="black"
        )
        x += 40
        y += 40

def final_animation(comp_value: int, canva: Canvas , _list: list, time) -> None:
    for _ in range(len(_list)):
        draw_info(comp_value, ["#d755a6"  for i in range(len(_list))], canva, _list)

    canva.canvas.create_text(20, 580, anchor="sw", text="TIME", fill="black")
    canva.canvas.create_text(20, 600, anchor="sw", text=time.time_now, fill="black")


def select_algorithm(
    speed: float, algorithm: list, random_list: list, dicc: dict
) -> None:
    if algorithm[0] == algorithm[1] or algorithm[0] == algorithm[2] or algorithm[1] == algorithm[2]:
        mBox.showerror("ERROR", "Algorithms must be different")
        return

    algorithm1 = dicc.get((re.split("\s", algorithm[0], 1)[0].lower()))
    algorithm2 = dicc.get((re.split("\s", algorithm[1], 1)[0].lower()))
    algorithm3 = dicc.get((re.split("\s", algorithm[2], 1)[0].lower()))

    GUI.obj.list_1._list = random_list.copy()
    GUI.obj.list_2._list = random_list.copy()
    GUI.obj.list_3._list = random_list.copy()

    threads.start_thread_animation(algorithm1, algorithm2, algorithm3, speed)

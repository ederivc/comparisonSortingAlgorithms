import re

import sortingvis.GUI
import sortingvis.threads

from tkinter import Canvas, Button
from tkinter import messagebox as mBox


def draw_info(
    comp_value: int, color: list, canva: Canvas, _list: list, sorting: str
) -> None:
    canva.delete("all")
    x = 25
    y = 60
    for key, value in enumerate(_list):
        canva.create_rectangle(x, value[1], y, 10, fill= color[key])
        canva.create_text(
            x, value[1]+20, anchor="sw", text=value[0], fill="black"
        )
        canva.create_text(
            40, 580, anchor="sw", font=("Helvetica", 10), text="Comparisons", fill="black"
        )
        canva.create_text(
            40, 600, anchor="sw", font=("Helvetica", 10), text=comp_value, fill="black"
        )

        validate_status(canva, sorting)

        x += 40
        y += 40

def final_animation(
    comp_value: int, canva: Canvas , _list: list, _time: int
) -> None:
    for _ in _list:
        draw_info(comp_value, ["#d755a6"  for _ in _list], canva, _list, "done")

    canva.create_text(
        400, 580, anchor="sw", font=("Helvetica", 10), text="TIME", fill="black"
    )
    canva.create_text(
        400, 600, anchor="sw", font=("Helvetica", 10), text=_time.time_now, fill="black"
    )


def select_algorithm(
    speed: float, algorithm: list, random_list: list, dicc: dict
) -> None:

    if len(set(algorithm)) == 3:
        pass
    else:
        mBox.showerror("ERROR", "Algorithms must be different")
        return

    algorithm1 = dicc.get((re.split("\s", algorithm[0], 1)[0].lower()))
    algorithm2 = dicc.get((re.split("\s", algorithm[1], 1)[0].lower()))
    algorithm3 = dicc.get((re.split("\s", algorithm[2], 1)[0].lower()))

    sortingvis.GUI.obj.list_1.value = random_list.copy()
    sortingvis.GUI.obj.list_2.value = random_list.copy()
    sortingvis.GUI.obj.list_3.value = random_list.copy()

    sortingvis.threads.start_thread_animation(algorithm1, algorithm2, algorithm3, speed)


def validate_status(canva: Canvas, status: str) -> Canvas:
    if status == "waiting":
        return canva.create_text(
            210, 580, anchor="sw", font=("Helvetica", 10), text="Status: Waiting", 
            fill="black"
        )
    
    if status == "sorting":
        return canva.create_text(
            210, 580, anchor="sw", font=("Helvetica", 10), text="Status: Sorting", 
            fill="black"
        )
    
    if status == "done":
        return canva.create_text(
            210, 580, anchor="sw", font=("Helvetica", 10), text="Status: Sorted", 
            fill="black"
        )
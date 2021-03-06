import threading

from typing import Callable

from sortingvis import GUI
from sortingvis.templates import Canvass
from sortingvis.controller import draw_info

def start_thread(
    canvas_1: Canvass, canvas_2: Canvass, canvas_3: Canvass, _list: list
) -> None:

    t1 = threading.Thread(
        target=draw_info, args=(0, ["#ffa500" for x in enumerate(_list)], 
        canvas_1, _list, GUI.obj.is_sorting_1.status), daemon=True
    )

    t2 = threading.Thread(
        target=draw_info, args=(0, ["#ffa500" for x in enumerate(_list)],
        canvas_2, _list, GUI.obj.is_sorting_2.status), daemon=True
    )

    t3 = threading.Thread(
        target=draw_info, args=(0, ["#ffa500" for x in enumerate(_list)],
        canvas_3, _list, GUI.obj.is_sorting_3.status), daemon=True
    )

    t1.start()
    t2.start()
    t3.start()


def start_thread_animation(
    algorithm_1: Callable, algorithm_2: Callable, algorithm_3: Callable, speed: float
) -> None:

    t1 = threading.Thread(
        target=algorithm_1, args=(speed , GUI.obj.list_1, GUI.obj.start_drawing1,
        GUI.obj.comparisons_1, GUI.obj.info_data_1, GUI.obj.time_1, 
        GUI.obj.is_sorting_1), daemon=True
    )

    t2 = threading.Thread(
        target=algorithm_2, args=(speed, GUI.obj.list_2, GUI.obj.start_drawing2, 
        GUI.obj.comparisons_2, GUI.obj.info_data_2, GUI.obj.time_2, 
        GUI.obj.is_sorting_2), daemon=True
    )

    t3 = threading.Thread(
        target=algorithm_3, args=(speed, GUI.obj.list_3, GUI.obj.start_drawing3, 
        GUI.obj.comparisons_3, GUI.obj.info_data_3, GUI.obj.time_3, 
        GUI.obj.is_sorting_3), daemon=True
    )

    t1.start()
    t2.start()
    t3.start()



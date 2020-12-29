import GUI
import threading

from typing import Callable
from templates import Canvass
from controller import draw_info

def start_thread(canvas_1: Canvass, canvas_2: Canvass, canvas_3: Canvass, _list: list) -> None:

    t1 = threading.Thread(target=draw_info, args=(0, ["#ffa500" for i in range(len(_list))], 
    canvas_1, _list), daemon=True)

    t2 = threading.Thread(target=draw_info, args=(0, ["#ffa500" for i in range(len(_list))],
    canvas_2, _list), daemon=True)

    t3 = threading.Thread(target=draw_info, args=(0, ["#ffa500" for i in range(len(_list))],
    canvas_3, _list), daemon=True)

    t1.start()
    t2.start()
    t3.start()


def start_thread_animation(algorithm_1: Callable, algorithm_2: Callable, algorithm_3: Callable) -> None:

    t1 = threading.Thread(target=algorithm_1, args=(0.02 , GUI.list_1,
    1, GUI.start_drawing1, GUI.comparisons_1, GUI.info_data_1, GUI.time_1), daemon=True)

    t2 = threading.Thread(target=algorithm_2, args=(0.02, GUI.list_2, 
    2, GUI.start_drawing2, GUI.comparisons_2, GUI.info_data_2, GUI.time_2), daemon=True)

    t3 = threading.Thread(target=algorithm_3, args=(0.02, GUI.list_3,
    3, GUI.start_drawing3, GUI.comparisons_3, GUI.info_data_3, GUI.time_3), daemon=True)

    t1.start()
    t2.start()
    t3.start()



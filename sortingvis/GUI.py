import os
import random
import tkinter as tk

from typing import Callable
from tkinter import messagebox as mBox
from tkinter import ttk, Scale, PhotoImage, Image, Canvas

import sortingvis.templates
from sortingvis.threads import start_thread
from sortingvis.validation import validate_canva, validate_animation
from sortingvis.controller import select_algorithm
from sortingvis.algorithms import (
    bubble_sort, 
    selection_sort, 
    insertion_sort, 
    cocktail_sort, 
    shell_sort
)


obj = sortingvis.templates.Objects()


class Options(tk.Frame):
    def __init__(
        self, master, generate_info: Callable, algo_keys: dict, canvas_list: list
    ) -> None:
        super().__init__(master)   
        self.master = master
        self.labels_conf = CreateLabel(self, canvas_list)
        self.combo_config = CreateCombo(self)
        self.scale_config = CreateScale(self)

        combo_list = [
            self.combo_config.combo_algorithm1, self.combo_config.combo_algorithm2,
            self.combo_config.combo_algorithm3
        ]

        values = [
            generate_info, algo_keys, self.scale_config.min_value, 
            self.scale_config.max_value, self.scale_config.speed_value, combo_list
        ]

        self.buttons_conf = CreateButton(self, values, canvas_list)

    def _config(self) -> None:
        bg = "#1b3945"
        self.config(bg = "#242038")
        self.place(relx = 0, rely = 0.8, relwidth = 1, relheight = 0.2)


class CreateImage(PhotoImage):
    def __init__(self) -> None:
        super().__init__()
        DIRNAME = os.path.dirname(__file__) 
        FILENAME = os.path.join(DIRNAME, 'change_color.png') 
        self.dark_image = PhotoImage(file = FILENAME)
        self.dark_image = self.dark_image.zoom(2)
        self.dark_image = self.dark_image.subsample(30)


class CreateLabel(tk.Label):
    def __init__(self, master: tk.Frame, canvas_list: list) -> None:
        super().__init__(master)
        self.master = master
        self.canvas_list = canvas_list
        self.algorithm_title = tk.Label(master, text="ALGORITHMS")
        self.values_title = tk.Label(master, text="VALUES")
        self.options_title = tk.Label(master, text="OPTIONS")
        self.algorithm_label_1 = tk.Label(master, text="Algorithm 1")
        self.algorithm_label_2 = tk.Label(master, text = "Algorithm 2")
        self.algorithm_label_3 = tk.Label(master, text = "Algorithm 3")
        self.min_value = tk.Label(master, text = "Min. Value")
        self.max_value = tk.Label(master, text = "Max. Value")
        self.speed = tk.Label(master, text = "Speed")
        self.img_label = tk.Label(master)
        self.image = CreateImage()
        self._config()
        self._place()

    def _config(self) -> None:
        self.algorithm_title.config(width = 30, height = 2, 
        font = "Helvetica 15 bold", bg = "#242038", fg = "white")
        self.values_title.config(width = 30, height = 2, 
        font = "Helvetica 15 bold", bg = "#242038", fg = "white")
        self.options_title.config(width = 30, height = 2, 
        font = "Helvetica 15 bold", bg = "#242038", fg = "white")
        self.img_label.config(bg="#242038", image = self.image.dark_image )
        self.img_label.bind('<Button-1>', lambda x: self.change_color())

        self.width_config(
            [self.algorithm_label_1, self.algorithm_label_2, self.algorithm_label_3,
            self.min_value, self.max_value, self.speed]
        )

    def _place(self) -> None:
        self.algorithm_title.place(x = 140, y = 20)
        self.values_title.place(x = 695, y = 20)
        self.options_title.place(x = 1180, y = 20)
        self.algorithm_label_1.place(x = 20, y = 80)
        self.algorithm_label_2.place(x = 220, y = 80)
        self.algorithm_label_3.place(x = 420, y = 80)
        self.min_value.place(x = 670, y = 80)    
        self.max_value.place(x = 850, y = 80)
        self.speed.place(x = 1100, y = 80)
        self.img_label.place(x = 1530, y = 80)

    def width_config(self, labels: list) -> None:
        for label in labels:
            label.config(width = 20)

    def change_color(self) -> None:
        _list = [self.canvas_list, self.master, self.algorithm_title,
            self.values_title, self.options_title, self.img_label]
        if obj.change_color.start:
            sortingvis.templates.ChangeColor(
                _list, down="#1b3945", up_1="#d2f4f4", up_2="#defefe", up_3="#d2f4f4"
            )
            obj.change_color.start = False
        
        else:
            sortingvis.templates.ChangeColor(
                _list, down="#242038", up_1="#9067c6", up_2="#8d86c9", up_3="#9067c6"
            )
            obj.change_color.start = True


class CreateButton:
    def __init__(self, *args) -> None:        
        self.new_info_btn = tk.Button(args[0], text="Generate graph")
        self.sort_items = tk.Button(args[0], text="Sort")
        self.delete_btn = tk.Button(args[0], text="Delete all")
        self.args = args
        self._config()
        self._place()

    def _config(self) -> None:
        self.new_info_btn.config(activebackground = "#468499",
        width = 12, command = lambda: self.args[1][0](
            self.args[1][2].get(), self.args[1][3].get()
        ))
        
        self.sort_items.config(activebackground = "#468499", width = 12, 
        command = lambda: select_algorithm(
            self.speed_values(self.args[1][4].get()), [self.args[1][5][0].get(), 
            self.args[1][5][1].get(), self.args[1][5][2].get()], obj.random_list.value, 
            self.args[1][1]
        ))    

        self.delete_btn.config(activebackground = "#468499", width = 12,
        command = self.delete_all)

    def _place(self) -> None:
        self.new_info_btn.place(x = 1380, y = 80)
        self.sort_items.place(x = 1300, y = 130)
        self.delete_btn.place(x = 1460, y = 130)

    def delete_all(self) -> None: 
        for canva in self.args[2]:
            canva.delete("all")

    def speed_values(self, speed: int) -> float:
        SPEED = {1: 0.4, 2: 0.3, 3: 0.2, 4: 0.1, 5: 0.08}
        return SPEED.get(speed)


class CreateCombo(ttk.Combobox):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.combo_algorithm1 = ttk.Combobox(master)
        self.combo_algorithm2 = ttk.Combobox(master)
        self.combo_algorithm3 = ttk.Combobox(master)
        self._config([self.combo_algorithm1, self.combo_algorithm2, self.combo_algorithm3])
        self._place()

    def _config(self, combos: list) -> None:
        combo_font = ("Helvetica", 12)
        for combo in combos:
            combo.config(values=[
                                "Bubble sort",
                                "Selection sort",
                                "Insertion sort",
                                "Cocktail shaker sort",
                                "Shell sort"],
                                font = combo_font,
                                width = 16)

            combo.current(0)

    def _place(self) -> None:
        self.combo_algorithm1.place(x = 20, y = 120)
        self.combo_algorithm2.place(x = 220, y = 120)
        self.combo_algorithm3.place(x = 420, y = 120)


class CreateScale(tk.Scale):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.min_value = tk.Scale(master)
        self.max_value = tk.Scale(master)
        self.speed_value = tk.Scale(master)
        self._config()
        self._place()

    def _config(self) -> None:
        self.min_value.config(from_=1, to=1000, orient=tk.HORIZONTAL, width = 5)
        self.max_value.config(from_=1, to=1000, orient=tk.HORIZONTAL, width = 5)
        self.speed_value.config(from_=1, to=5, orient=tk.HORIZONTAL, width = 5)
    
    def _place(self) -> None:
        self.min_value.place(x = 700, y = 120)
        self.max_value.place(x = 880, y = 120)
        self.speed_value.place(x = 1130, y = 120)


class Application:
    def __init__(
        self, window: tk.Tk, canvas_1: Canvas, canvas_2: Canvas, canvas_3: Canvas
    ) -> None:
        self.window = window
        
        self.time_list = [obj.time_1, obj.time_2, obj.time_3]

        self.canvas_1 = canvas_1
        self.canvas_2 = canvas_2
        self.canvas_3 = canvas_3

        self.canvas_list = [self.canvas_1, self.canvas_2, self.canvas_3]
        self.comp_list = [obj.comparisons_1, obj.comparisons_2, obj.comparisons_3]

        self.algo_keys = {
                    "bubble" : bubble_sort,
                    "insertion" : insertion_sort,
                    "selection" : selection_sort,
                    "cocktail" : cocktail_sort,
                    "shell" : shell_sort
        }

        self.display = Options(
            self.window, self.generate_info, self.algo_keys, self.canvas_list
        )
        
        self.display._config()
        

    def generate_info(self, min_value: int, max_value: int) -> None:    
        for canvas in self.canvas_list:
            canvas.delete("all")

        for comp in self.comp_list:
            comp.number = 0

        obj.random_list.value.clear()

        if min_value > max_value:
            mBox.showerror("ERROR", "Value error")
            return

        for i in range(12):
            number = random.randint(min_value, max_value)
            obj.random_list.value.append(number)

        max_value = max(obj.random_list.value)
        temp_list = []

        for i in obj.random_list.value:
            height_value = 	int(i * 450 / max_value)	 #max_value = 450  -> i?

            if height_value <= 9:
                temp_list.append((i, 9))
                continue

            temp_list.append((i, height_value))			 #[(1, 10), (32, 300)]

        obj.random_list.value = temp_list
        print(obj.random_list.value)

        start_thread(
            self.canvas_1, self.canvas_2, self.canvas_3, obj.random_list.value
        )

    def _periodic_refresh(self) -> None:
        validate_canva(self.canvas_1, self.canvas_2, self.canvas_3)
        validate_animation(
            self.canvas_1, self.canvas_2, self.canvas_3, self.time_list
        )
        self.window.after(1000 // 1000, self._periodic_refresh)

    def start(self) -> None:
        self._periodic_refresh()
        self.window.mainloop()
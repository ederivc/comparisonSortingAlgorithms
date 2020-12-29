import random
import threads
import controller
import validation
import tkinter as tk

from typing import Callable
from tkinter import messagebox as mBox
from templates import Data, Comparisons, List, Canvas, Time
from tkinter import ttk, Scale, PhotoImage, Image
from Algorithms import bubble_sort, selection_sort, insertion_sort, cocktail_sort, shell_sort


start_drawing1 = Data()
start_drawing2 = Data()
start_drawing3 = Data()

comparisons_1 = Comparisons()
comparisons_2 = Comparisons()
comparisons_3 = Comparisons()

list_1 = List()
list_2 = List()
list_3 = List()

info_data_1 = List()
info_data_2 = List()
info_data_3 = List()

random_list = List()

time_1 = Time()
time_2 = Time()
time_3 = Time()

class Application:
    def __init__(self, window: tk.Tk, canvas_1: Canvas, canvas_2: Canvas, canvas_3: Canvas) -> None:
        self.window = window
        self.color = "black"
        self.flag = "resume"

        #self.dark_image = PhotoImage(file = "dark_mode.png")
        #self.dark_image = self.dark_image.zoom(1)
        #self.dark_image = self.dark_image.subsample(30)

        self.time_list = [time_1, time_2, time_3]

        self.canvas_1 = canvas_1
        self.canvas_2 = canvas_2
        self.canvas_3 = canvas_3

        self.canvas_list = [self.canvas_1, self.canvas_2, self.canvas_3]

        self.algo_keys = {"bubble" : bubble_sort,
                        "insertion" : insertion_sort,
                        "selection" : selection_sort,
                        "cocktail" : cocktail_sort,
                        "shell" : shell_sort}
        
        self.obj = Options(self.window, self.generate_info, self.algo_keys, self.canvas_list)
        self.obj._setup()
        

    def comparisons_info(self, comp_value):
        self.canvas_1.canvas.create_text(20,500,anchor = "sw", text = "Insertion sort", fill = self.color)
        self.canvas_2.canvas.create_text(20,500,anchor = "sw", text = "Bubble sort", fill = self.color)
        self.canvas_3.canvas.create_text(20,500,anchor = "sw", text = "Selection sort", fill = self.color)

    def speed_values(self, speed: int) -> float:
        if speed == 1:
            return 0.4
        elif speed == 2:
            return 0.3
        elif speed == 3:
            return 0.2
        elif speed == 4:
            return 0.1
        else:
            return 0.08


    def dark_screen(self, lower_frame):
        pass
        """if self.color == "black":
            self.canvas.config(bg = "#666666")
            lower_frame.config(bg = "#333333")
            self.canvas.update_idletasks()
            self.color = "white"
        else:
            self.canvas.config(bg = "#f0ffff")
            lower_frame.config(bg = "#1b3945")
            self.canvas.update_idletasks()
            self.color = "black"""
      

    def generate_info(self, min_value: int, max_value: int) -> None:    
        for canvas in self.canvas_list:
            canvas.canvas.delete("all")
        
        random_list._list.clear()

        if min_value > max_value:
            mBox.showerror("ERROR", "Value error")
            return

        for i in range(12):
            number = random.randint(min_value, max_value)
            random_list._list.append(number)

        max_value = max(random_list._list)
        temp_list = []

        for i in random_list._list:
            height_value = 	int(i * 450 / max_value)	 #max_value = 450  -> i?

            if height_value <= 9:
                temp_list.append((i, 9))
                continue

            temp_list.append((i, height_value))			 #[(1, 10), (32, 300)]

        random_list._list = temp_list
        print(random_list._list)

        threads.start_thread(self.canvas_1, self.canvas_2, self.canvas_3, random_list._list)


    def _periodic_refresh(self) -> None:
        validation.validate_canva(self.canvas_1, self.canvas_2, self.canvas_3)
        validation.validate_animation(self.canvas_1, self.canvas_2, self.canvas_3, self.time_list)
        self.window.after(1000 // 1000, self._periodic_refresh)


    def start(self) -> None:
        self._periodic_refresh()
        self.window.mainloop()


class Options(tk.Frame):
    def __init__(self, master, generate_info: Callable, algo_keys: dict, canvas_list: list) -> None:
        super().__init__(master)   
        self.master = master
        self.labels_conf = CreateLabel(self)
        self.combo_config = CreateCombo(self)
        self.scale_config = CreateScale(self)

        combo_list = [self.combo_config.combo_algorithm1, self.combo_config.combo_algorithm2,
                    self.combo_config.combo_algorithm3]

        values = [generate_info, algo_keys, self.scale_config.min_value_number, 
                self.scale_config.max_value_number, self.scale_config.speed_value, combo_list]

        self.buttons_conf = CreateButton(self, values, canvas_list)

    def _setup(self):
        bg = "#1b3945"
        self.config(bg = "#242038")
        self.place(relx = 0, rely = 0.8, relwidth = 1, relheight = 0.2)


class CreateLabel(tk.Label):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master = master
        self.algorithm_title = tk.Label(master, text="ALGORITHMS")
        self.values_title = tk.Label(master, text="VALUES")
        self.options_title = tk.Label(master, text="OPTIONS")
        self.algorithm_label_1 = tk.Label(master, text="Algorithm 1")
        self.algorithm_label_2 = tk.Label(master, text = "Algorithm 2")
        self.algorithm_label_3 = tk.Label(master, text = "Algorithm 3")
        self.min_value = tk.Label(master, text = "Min. Value")
        self.max_value = tk.Label(master, text = "Max. Value")
        self.speed = tk.Label(master, text = "Speed")
        self._setup()
        self._place()

    def _setup(self) -> None:
        self.algorithm_title.config(width = 30, height = 2, 
        font = "Helvetica 15 bold", bg = "#242038", fg = "white")
        self.values_title.config(width = 30, height = 2, 
        font = "Helvetica 15 bold", bg = "#242038", fg = "white")
        self.options_title.config(width = 30, height = 2, 
        font = "Helvetica 15 bold", bg = "#242038", fg = "white")

        self.width_config([self.algorithm_label_1, self.algorithm_label_2, self.algorithm_label_3,
                        self.min_value, self.max_value, self.speed])

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

    def width_config(self, labels: list) -> None:
        for label in labels:
            label.config(width = 20)


class CreateButton():
    def __init__(self, *args) -> None:        
        self.new_info_btn = tk.Button(args[0], text="Generate graph")
        self.sort_items = tk.Button(args[0], text="Sort")
        self.delete_btn = tk.Button(args[0], text="Delete all")
        self.args = args
        self._setup()
        self._place()

    def _setup(self):
        self.new_info_btn.config(activebackground = "#468499",
        width = 12, command = lambda: self.args[1][0](self.args[1][2].get(), self.args[1][3].get()))
        
        self.sort_items.config(activebackground = "#468499", width = 12, 
        command = lambda: controller.select_algorithm(self.args[1][4].get(), [self.args[1][5][0].get(), 
        self.args[1][5][1].get(), self.args[1][5][2].get()], random_list._list, self.args[1][1]))

        self.delete_btn.config(activebackground = "#468499", width = 12,
        command = self.delete_all)

    def _place(self):
        self.new_info_btn.place(x = 1380, y = 80)
        self.sort_items.place(x = 1300, y = 130)
        self.delete_btn.place(x = 1460, y = 130)

    def delete_all(self): 
        for canva in self.args[2]:
            canva.canvas.delete("all")


class CreateCombo(ttk.Combobox):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.combo_algorithm1 = ttk.Combobox(master)
        self.combo_algorithm2 = ttk.Combobox(master)
        self.combo_algorithm3 = ttk.Combobox(master)
        self._setup([self.combo_algorithm1, self.combo_algorithm2, self.combo_algorithm3])
        self._place()

    def _setup(self, combos: list) -> None:
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
        self.min_value_number = tk.Scale(master)
        self.max_value_number = tk.Scale(master)
        self.speed_value = tk.Scale(master)
        self._setup()
        self._place()

    def _setup(self):
        self.min_value_number.config(from_=1, to=1000, orient=tk.HORIZONTAL, width = 5)
        self.max_value_number.config(from_=1, to=1000, orient=tk.HORIZONTAL, width = 5)
        self.speed_value.config(from_=1, to=5, orient=tk.HORIZONTAL, width = 5)
    
    def _place(self):
        self.min_value_number.place(x = 700, y = 120)
        self.max_value_number.place(x = 880, y = 120)
        self.speed_value.place(x = 1130, y = 120)
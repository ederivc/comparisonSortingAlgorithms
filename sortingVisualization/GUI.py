import re
import time
import random
import threading
import tkinter as tk
import Algorithms
from Algorithms import *
from templates import Data, Comparisons, List, Canvass
from tkinter import messagebox as mBox
from tkinter import ttk, Canvas, Scale, PhotoImage, Image

global hola, hola2, hola3, finish1, finish2, finish3
start_drawing1 = True
start_drawing2 = True
start_drawing3 = True
finish1 = False
finish2 = False
finish3 = False

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

class Window:
    def __init__(self, window: tk.Tk, canvas_1: Canvas, canvas_2: Canvas, canvas_3: Canvas) -> None:
        self.window = window
        self.random_list = []
        self.color = "black"

        self.dark_image = PhotoImage(file = "dark_mode.png")
        self.dark_image = self.dark_image.zoom(1)
        self.dark_image = self.dark_image.subsample(30)

        #self.canvas1 = Canvass(self.window,"#de594d", 0, 0.33, 0.8)
        #self.canvas2 = Canvass(self.window, "#32a6ac", 0.33, 0.66, 0.8)
        #self.canvas3 = Canvass(self.window, "#ca48cc", 0.67, 0.9, 0.8)

        self.canvas_1 = canvas_1
        self.canvas_2 = canvas_2
        self.canvas_3 = canvas_3

        self.canvas_list = [self.canvas_1, self.canvas_2, self.canvas_3]

        self.algo_keys = {"bubble" : bubble_sort,
                        "insertion" : insertion_sort,
                        "selection" : selection_sort,
                        "cocktail" : cocktail_sort,
                        "shell" : shell_sort}
        
        self.display_options()
        


    def display_options(self) -> None:
        lower_frame = tk.Frame(self.window, bg = "#1b3945")
        lower_frame.place(relx = 0, rely = 0.8, relwidth = 1, relheight = 0.2)

        algorithm_title = tk.Label(lower_frame, text = "ALGORITHMS", width = 30, height = 2, 
        font = "Helvetica 15 bold", bg = "#1b3945", fg = "white")
        algorithm_title.place(x = 140, y = 20)

        values_title = tk.Label(lower_frame, text = "VALUES", width = 30, height = 2, 
        font = "Helvetica 15 bold", bg = "#1b3945", fg = "white")
        values_title.place(x = 695, y = 20)

        options_title = tk.Label(lower_frame, text = "OPTIONS", width = 30, height = 2, 
        font = "Helvetica 15 bold", bg = "#1b3945", fg = "white")
        options_title.place(x = 1180, y = 20)

        algorithm_label = tk.Label(lower_frame, text = "Algorithm 1", width = 20)
        algorithm_label.place(x = 20, y = 80)

        combo_algorithm1 = ttk.Combobox(lower_frame,
                                    values=[
                                            "Bubble sort",
                                            "Selection sort",
                                            "Insertion sort",
                                            "Cocktail shaker sort",
                                            "Shell sort"],
                                            font = (8))
        combo_algorithm1.place(x = 20, y = 120)
        combo_algorithm1.config(font = ("Helvetica"), width = 16)
        combo_algorithm1.current(0)

        algorithm_label2 = tk.Label(lower_frame, text = "Algorithm 2", width = 20)
        algorithm_label2.place(x = 220, y = 80)

        combo_algorithm2 = ttk.Combobox(lower_frame,
                                    values=[
                                            "Bubble sort",
                                            "Selection sort",
                                            "Insertion sort",
                                            "Cocktail shaker sort",
                                            "Shell sort"],
                                            font = (8))
        combo_algorithm2.place(x = 220, y = 120)
        combo_algorithm2.config(font = ("Helvetica"), width = 16)
        combo_algorithm2.current(0)

        algorithm_label3 = tk.Label(lower_frame, text = "Algorithm 3", width = 20)
        algorithm_label3.place(x = 420, y = 80)

        combo_algorithm3 = ttk.Combobox(lower_frame,
                                    values=[
                                            "Bubble sort",
                                            "Selection sort",
                                            "Insertion sort",
                                            "Cocktail shaker sort",
                                            "Shell sort"],
                                            font = (8))
        combo_algorithm3.place(x = 420, y = 120)
        combo_algorithm3.config(font = ("Helvetica"), width = 16)
        combo_algorithm3.current(0)

        min_value = tk.Label(lower_frame, text = "Min. Value", width = 20)
        min_value.place(x = 670, y = 80)

        min_value_number = tk.Scale(lower_frame, from_=1, to=1000, orient=tk.HORIZONTAL, width = 5)
        min_value_number.place(x = 700, y = 120)

        max_value = tk.Label(lower_frame, text = "Max. Value", width = 20)
        max_value.place(x = 850, y = 80)

        max_value_number = tk.Scale(lower_frame, from_=1, to=1000, orient=tk.HORIZONTAL, width = 5)
        max_value_number.place(x = 880, y = 120)

        speed = tk.Label(lower_frame, text = "Speed", width = 19)
        speed.place(x = 1100, y = 80)

        speed_var = tk.Scale(lower_frame, from_=1, to=5, orient=tk.HORIZONTAL, width = 5)
        speed_var.place(x = 1130, y = 120)

        new_info_btn = tk.Button(lower_frame, text = "Generate graph", activebackground = "#468499",
        width = 12, command = lambda: self.generate_info(min_value_number.get(), max_value_number.get()))
        new_info_btn.place(x = 1380, y = 80)

        sort_items = tk.Button(lower_frame, text = "Sort",activebackground = "#468499", width = 12,
        command = lambda: self.select_algorithm(speed_var.get(), [combo_algorithm1.get(), 
        combo_algorithm2.get(), combo_algorithm3.get()]))
        sort_items.place(x = 1300, y = 130)

        delete_btn = tk.Button(lower_frame, text = "Delete all",activebackground = "#468499", width = 12,
        command = self.delete_all)
        delete_btn.place(x = 1460, y = 130)

        img_label = tk.Label(lower_frame, background = "white", image = self.dark_image)
        img_label.place(x = 1545, y = 80)
        img_label.bind('<Button-1>', lambda x: self.dark_screen(lower_frame))


    def comparisons_info(self, comp_value):
        self.canvas_1.canvas.create_text(20,500,anchor = "sw", text = "Insertion sort", fill = self.color)
        self.canvas_2.canvas.create_text(20,500,anchor = "sw", text = "Bubble sort", fill = self.color)
        self.canvas_3.canvas.create_text(20,500,anchor = "sw", text = "Selection sort", fill = self.color)
        #self.canvas.create_text(130, 500,anchor = "sw", text = comp_value, fill = self.color)


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
        

    def select_algorithm(self, speed: float, algorithm: list) -> None:

        if algorithm[0] == algorithm[1] or algorithm[0] == algorithm[2] or algorithm[1] == algorithm[2]:
            mBox.showerror("ERROR", "Algorithms must be different")
            return

        algorithm1 = self.algo_keys.get((re.split("\s", algorithm[0], 1)[0].lower()))
        algorithm2 = self.algo_keys.get((re.split("\s", algorithm[1], 1)[0].lower()))
        algorithm3 = self.algo_keys.get((re.split("\s", algorithm[2], 1)[0].lower()))

        list_1._list = self.random_list.copy()
        list_2._list = self.random_list.copy()
        list_3._list = self.random_list.copy()

        
        #self.speed_values(speed)
        t1 = threading.Thread(target=algorithm1, args=(0.02 , list_1, 
        self.draw_info, self.final_animation, 1, start_drawing1, comparisons_1, info_data_1), daemon=True)

        t2 = threading.Thread(target=algorithm2, args=(0.02, list_2, 
        self.draw_info, self.final_animation, 2, start_drawing2, comparisons_2, info_data_2), daemon=True)

        t3 = threading.Thread(target=algorithm3, args=(0.02, list_3,
        self.draw_info, self.final_animation, 3, start_drawing3, comparisons_3, info_data_3), daemon=True)

        t1.start()
        t2.start()
        t3.start()


    def final_animation(self, comp_value: int, canva: Canvas , _list: list) -> None:
        """for x in range(len(_list)):
            time.sleep(0.03)
            self.draw_info(comp_value, ["red" if i <= x else "green" if i == x+1 else "black" for i in range(len(_list))], canva, 
            _list)"""
            #self.draw_info(["#f3d3a5" if i <= x else "#4e2c7f" if i == x+1 else "#badd99" fothemer i in range(len(self.random_list))])
        for x in range(len(_list)):
            #time.sleep(0.03)
            self.draw_info(comp_value, ["green"  for i in range(len(_list))], canva, _list)

    def delete_all(self):
        pass
        #self.canvas.delete("all")


    def generate_info(self, min_value: int, max_value: int) -> None:
        for canvas in self.canvas_list:
            canvas.canvas.delete("all")
        
        self.random_list.clear()

        if min_value > max_value:
            mBox.showerror("ERROR", "Value error")
            return

        for i in range(12):
            number = random.randint(min_value, max_value)
            self.random_list.append(number)

        max_value = max(self.random_list)
        temp_list = []

        for i in self.random_list:
            height_value = 	int(i * 450 / max_value)	 #max_value = 450  -> i?

            if height_value <= 9:
                temp_list.append((i, 9))
                continue

            temp_list.append((i, height_value))			 #[(1, 10), (32, 300)]

        self.random_list = temp_list
        print(self.random_list)

        #self.draw_info(0, ["#ffa500" for i in range(len(self.random_list))])
        #self.draw_info2(0, ["#ffa500" for i in range(len(self.random_list))])

        self.start_thread()


    def start_thread(self) -> None:
        t1 = threading.Thread(target=self.draw_info, args=(0, ["#ffa500" for i in range(len(self.random_list))], 
        self.canvas_1, self.random_list), daemon=True)

        t2 = threading.Thread(target=self.draw_info, args=(0, ["#ffa500" for i in range(len(self.random_list))],
        self.canvas_2, self.random_list), daemon=True)

        t3 = threading.Thread(target=self.draw_info, args=(0, ["#ffa500" for i in range(len(self.random_list))],
        self.canvas_3, self.random_list), daemon=True)

        t1.start()
        t2.start()
        t3.start()


    def draw_info(self, comp_value: int, color: list, canva: Canvas, _list: list) -> None:
        #for canvas in self.canvas_list:
            #canvas.canvas.delete("all")

        canva.canvas.delete("all")
        
        #self.comparisons_info(comp_value)

        x = 25
        y = 50
        for key, value in enumerate(_list):
            canva.canvas.create_rectangle(x, value[1], y, 10, fill= color[key])
            canva.canvas.create_text(x,value[1]+20,anchor = "sw", text = value[0], fill = self.color)
            x += 40
            y += 40

        #canva.canvas.update()
        #canva.canvas.update_idletasks()




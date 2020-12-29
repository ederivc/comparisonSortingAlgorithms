import time
import random
import tkinter as tk
import threading
from Algorithms import *
from tkinter import messagebox as mBox
from tkinter import ttk, Canvas, Scale, PhotoImage, Image

global hola
hola = True


class Window:
	def __init__(self, window):
		self.window = window
		self.random_list = []
		self.color = "black"
		self.dark_image = PhotoImage(file = "dark_mode.png")
		self.dark_image = self.dark_image.zoom(1)
		self.dark_image = self.dark_image.subsample(30)
		self.canvas = Canvas(self.window, bg = "#f0ffff")
		self.canvas.place(relx = 0, relwidth =1, relheight = 0.80)
		self.display_options()
		self.my_thread = threading.Thread(target=self.select_algorithm)


	def display_options(self):
		lower_frame = tk.Frame(self.window, bg = "#1b3945")
		lower_frame.place(relx = 0, rely = 0.8, relwidth = 1, relheight = 0.2)

		algorithm_label = tk.Label(lower_frame, text = "Algorithm", width = 20)
		algorithm_label.place(x = 40, y = 20)

		combo_algorithm = ttk.Combobox(lower_frame,
		                            values=[
		                                    "Bubble sort",
		                                    "Selection sort",
											"Insertion sort",
											"Cocktail shaker sort",
											"Shell sort"],
											font = (8))
		combo_algorithm.place(x = 40, y = 60)
		combo_algorithm.config(font = ("Helvetica"), width = 16)
		combo_algorithm.current(0)

		min_value = tk.Label(lower_frame, text = "Min. Value", width = 20)
		min_value.place(x = 240, y = 20)

		min_value_number = tk.Scale(lower_frame, from_=1, to=1000, orient=tk.HORIZONTAL, width = 5)
		min_value_number.place(x = 260, y = 60)

		max_value = tk.Label(lower_frame, text = "Max. Value", width = 20)
		max_value.place(x = 440, y = 20)

		max_value_number = tk.Scale(lower_frame, from_=1, to=1000, orient=tk.HORIZONTAL, width = 5)
		max_value_number.place(x = 460, y = 60)

		speed = tk.Label(lower_frame, text = "Speed", width = 19)
		speed.place(x = 640, y = 20)

		speed_var = tk.Scale(lower_frame, from_=1, to=5, orient=tk.HORIZONTAL, width = 5)
		speed_var.place(x = 660, y = 60)

		new_info_btn = tk.Button(lower_frame, text = "Generate graph", activebackground = "#468499",
		width = 12, command = lambda: self.generate_info(min_value_number.get(), max_value_number.get(), 
		combo_algorithm.get()))
		new_info_btn.place(x = 825, y = 15)

		sort_items = tk.Button(lower_frame, text = "Sort",activebackground = "#468499", width = 12,
		command = lambda: self.select_algorithm(speed_var.get(), combo_algorithm.get()))
		sort_items.place(x = 825, y = 53)

		delete_btn = tk.Button(lower_frame, text = "Delete all",activebackground = "#468499", width = 12,
		command = self.delete_all)
		delete_btn.place(x = 825, y = 90)

		img_label = tk.Label(lower_frame, background = "white", image = self.dark_image)
		img_label.place(x = 955, y = 45)
		img_label.bind('<Button-1>', lambda x: self.dark_screen(lower_frame))


	def comparisons_info(self, comp_value):
		self.canvas.create_text(20,500,anchor = "sw", text = "Comparisons", fill = self.color)
		self.canvas.create_text(130, 500,anchor = "sw", text = comp_value, fill = self.color)

	def info(self, speed, algo):
		self.my_thread.start = threading.Thread(target=self.select_algorithm, args=(speed, algo)).start()

	def speed_values(self, speed):
		if speed == 1:
			return 0.01
		elif speed == 2:
			return 0.3
		elif speed == 3:
			return 0.2
		elif speed == 4:
			return 0.1
		else:
			return 0.08


	def dark_screen(self, lower_frame):
		if self.color == "black":
			self.canvas.config(bg = "#666666")
			lower_frame.config(bg = "#333333")
			self.canvas.update_idletasks()
			self.color = "white"
		else:
			self.canvas.config(bg = "#f0ffff")
			lower_frame.config(bg = "#1b3945")
			self.canvas.update_idletasks()
			self.color = "black"

	def get_info(self, queue, lock_thread):
		global t1
		print(f"CURRENT {threading.current_thread().name}")
		lock_thread.acquire(timeout=2)

		
		print(f"CURRENT2 {threading.current_thread().name}")
		
		print(f"ALIVE {threading.main_thread().is_alive}")
		#print(f"after {threading.current_thread.name()}")
		print("Info", queue.get(0))
		
		print(f"after {threading.current_thread().name}")
		
		lock_thread.release()
		


	def select_algorithm(self, speed, option):
		if option == "Bubble sort":
			print(f"CURRENTs {threading.current_thread().name}")
			#global t1
			t1 = threading.Thread(name="Thread1", target=bubble_sort, args=(self.speed_values(speed), 
			self.random_list, 0, self.draw_info, self.final_animation, self.get_info))
			#bubble_sort(self.speed_values(speed), self.random_list, 0, self.draw_info,
			#self.final_animation, self.get_info)
			t1.start()

		elif option == "Selection sort":
			selection_sort(self.speed_values(speed), self.random_list, 0, self.draw_info,
			self.final_animation)

		elif option == "Insertion sort":
			insertion_sort(self.speed_values(speed), self.random_list, 0, self.draw_info,
			self.final_animation)

		elif option == "Cocktail shaker sort":
			cocktail_sort(self.speed_values(speed), self.random_list, 0, self.draw_info,
			self.final_animation)

		elif option == "Shell sort":
			shell_sort(self.speed_values(speed), self.random_list, 0, self.draw_info,
			self.final_animation)


	def final_animation(self, comp_value):
		for x in range(len(self.random_list)):
			time.sleep(0.03)
			self.draw_info(comp_value, ["#ff7f50" if i <= x else "#4ca3dd" if i == x+1 else "#badd99" for i in range(len(self.random_list))])
			#self.draw_info(["#f3d3a5" if i <= x else "#4e2c7f" if i == x+1 else "#badd99" fothemer i in range(len(self.random_list))])


	def delete_all(self):
		self.canvas.delete("all")


	def generate_info(self, min_value, max_value, algorithm):
		self.canvas.delete("all")
		self.random_list.clear()

		if min_value > max_value:
			mBox.showerror("ERROR", "Value error")
			return

		for i in range(24):
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

		self. random_list = temp_list
		print(self.random_list)

		return self.draw_info(0, ["#ffa500" for i in range(len(self.random_list))])


	def draw_info(self, comp_value, color):
		self.canvas.delete("all")
		self.comparisons_info(comp_value)
		x = 20
		y = 50
		for key, value in enumerate(self.random_list):
			self.canvas.create_rectangle(x, value[1], y, 10,fill= color[key])
			self.canvas.create_text(x,value[1]+20,anchor = "sw", text = value[0], fill = self.color)
			x += 40
			y += 40

		self.window.update_idletasks()






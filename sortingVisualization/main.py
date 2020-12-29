import tkinter as tk
from GUI import Window
import GUI
import threading
from queue import Queue
import Algorithms

def _periodic_refresh() -> None:
    # REVISAR SI CAMBIO Y ACTUALIZAR CANVAS
    #print(f"HERE {threading.current_thread().name}")

    print(GUI.hola)
    if GUI.hola == False:
        print(Algorithms.data[0], Algorithms.data[1])
        #GUI.Window.draw_info(0, Algorithms.data[0], Algorithms.data[1])
        app.draw_info(Algorithms.data[0], Algorithms.data[1])

    if GUI.hola == "nada":
        app.final_animation(Algorithms.comp_value2)
        GUI.hola = True

    window.after(1000 // 100, _periodic_refresh)

def start() -> None:
    _periodic_refresh()
    window.mainloop()

if __name__ == "__main__":
    window = tk.Tk()

    width = 1000
    height = 650
    window.minsize(width, height)
    window.title("Algorithm visualization")

    app = Window(window)
    
    start()
    #window.mainloop()


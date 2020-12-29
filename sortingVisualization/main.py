import GUI
import templates
import Algorithms
import tkinter as tk
from templates import Canvass

def _periodic_refresh() -> None:
    # REVISAR SI CAMBIO Y ACTUALIZAR CANVAS
    #print(f"HERE {threading.current_thread().name}")

    if GUI.start_drawing1.start == False:
        app.draw_info(GUI.info_data_1._list[0], GUI.info_data_1._list[1], canvas_1, GUI.list_1._list)

    if GUI.start_drawing2.start == False:
        app.draw_info(GUI.info_data_2._list[0], GUI.info_data_2._list[1], canvas_2, GUI.list_2._list)
    
    if GUI.start_drawing3.start == False:
        app.draw_info(GUI.info_data_3._list[0], GUI.info_data_3._list[1], canvas_3, GUI.list_3._list)

    if GUI.start_drawing1.start == "animate":
        app.final_animation(GUI.comparisons_1.number, canvas_1, GUI.list_1._list)
        GUI.start_drawing1.start = True

    if GUI.start_drawing2.start == "animate":
        app.final_animation(GUI.comparisons_2.number, canvas_2, GUI.list_2._list)
        GUI.start_drawing2.start = True
        
    if GUI.start_drawing3.start == "animate":
        app.final_animation(GUI.comparisons_3.number, canvas_3, GUI.list_3._list)
        GUI.start_drawing3.start = True

    window.after(1000 // 1000, _periodic_refresh)


def start() -> None:
    _periodic_refresh()
    window.mainloop()


if __name__ == "__main__":

    window = tk.Tk()

    canvas_1 = Canvass(window,"#de594d", 0, 0.33, 0.8)
    canvas_2 = Canvass(window, "#32a6ac", 0.33, 0.66, 0.8)
    canvas_3 = Canvass(window,"#ca48cc", 0.67, 0.9, 0.8)

    templates.Setup(window)

    app = GUI.Window(window, canvas_1, canvas_2, canvas_3)

    start()
from sortingvis import GUI   

from sortingvis.templates import Canvass
from sortingvis.controller import draw_info, final_animation

def validate_canva(
    canvas_1: Canvass, canvas_2: Canvass, canvas_3: Canvass
) -> None:
    
    if GUI.obj.start_drawing1.start == False:
        draw_info(
            GUI.obj.info_data_1.value[0], GUI.obj.info_data_1.value[1], 
            canvas_1, GUI.obj.list_1.value, GUI.obj.is_sorting_1.status
        )

    if GUI.obj.start_drawing2.start == False:
        draw_info(
            GUI.obj.info_data_2.value[0], GUI.obj.info_data_2.value[1], 
            canvas_2, GUI.obj.list_2.value, GUI.obj.is_sorting_2.status
        )
        
    if GUI.obj.start_drawing3.start == False:
        draw_info(
            GUI.obj.info_data_3.value[0], GUI.obj.info_data_3.value[1], 
            canvas_3, GUI.obj.list_3.value, GUI.obj.is_sorting_3.status
        )

def validate_animation(
    canvas_1: Canvass, canvas_2: Canvass, canvas_3: Canvass, 
    time_list: list
) -> None:

    if GUI.obj.start_drawing1.start == "animate":
        final_animation(
            GUI.obj.comparisons_1.number, canvas_1, 
            GUI.obj.list_1.value, time_list[0]
        )
        GUI.obj.start_drawing1.start = True
        GUI.obj.is_sorting_1.status = "waiting"

    if GUI.obj.start_drawing2.start == "animate":
        final_animation(
            GUI.obj.comparisons_2.number, canvas_2, 
            GUI.obj.list_2.value, time_list[1]
        )
        GUI.obj.start_drawing2.start = True
        GUI.obj.is_sorting_2.status = "waiting"
            
    if GUI.obj.start_drawing3.start == "animate":
        final_animation(
            GUI.obj.comparisons_3.number, canvas_3, 
            GUI.obj.list_3.value, time_list[2]
        )
        GUI.obj.start_drawing3.start = True
        GUI.obj.is_sorting_3.status = "waiting"
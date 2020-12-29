import GUI   

from templates import Canvass
from controller import draw_info, final_animation

def validate_canva(
    canvas_1: Canvass, canvas_2: Canvass, canvas_3: Canvass
) -> None:
    
    if GUI.obj.start_drawing1.start == False:
        draw_info(
            GUI.obj.info_data_1._list[0], GUI.obj.info_data_1._list[1], 
            canvas_1, GUI.obj.list_1._list
        )

    if GUI.obj.start_drawing2.start == False:
        draw_info(
            GUI.obj.info_data_2._list[0], GUI.obj.info_data_2._list[1], 
            canvas_2, GUI.obj.list_2._list
        )
        
    if GUI.obj.start_drawing3.start == False:
        draw_info(
            GUI.obj.info_data_3._list[0], GUI.obj.info_data_3._list[1], 
            canvas_3, GUI.obj.list_3._list
        )

def validate_animation(
    canvas_1: Canvass, canvas_2: Canvass, canvas_3: Canvass, 
    time_list: list
) -> None:

    if GUI.obj.start_drawing1.start == "animate":
        final_animation(
            GUI.obj.comparisons_1.number, canvas_1, 
            GUI.obj.list_1._list, time_list[0]
        )
        GUI.obj.start_drawing1.start = True

    if GUI.obj.start_drawing2.start == "animate":
        final_animation(
            GUI.obj.comparisons_2.number, canvas_2, 
            GUI.obj.list_2._list, time_list[1]
        )
        GUI.obj.start_drawing2.start = True
            
    if GUI.obj.start_drawing3.start == "animate":
        final_animation(
            GUI.obj.comparisons_3.number, canvas_3, 
            GUI.obj.list_3._list, time_list[2]
        )
        GUI.obj.start_drawing3.start = True
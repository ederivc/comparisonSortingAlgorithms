import GUI   

from controller import draw_info, final_animation

def validate_canva(canvas_1, canvas_2, canvas_3):

    if GUI.start_drawing1.start == False:
        draw_info(GUI.info_data_1._list[0], GUI.info_data_1._list[1], canvas_1, GUI.list_1._list)

    if GUI.start_drawing2.start == False:
        draw_info(GUI.info_data_2._list[0], GUI.info_data_2._list[1], canvas_2, GUI.list_2._list)
        
    if GUI.start_drawing3.start == False:
        draw_info(GUI.info_data_3._list[0], GUI.info_data_3._list[1], canvas_3, GUI.list_3._list)

def validate_animation(canvas_1, canvas_2, canvas_3, time_list):
    if GUI.start_drawing1.start == "animate":
        final_animation(GUI.comparisons_1.number, canvas_1, GUI.list_1._list, time_list[0])
        GUI.start_drawing1.start = True

    if GUI.start_drawing2.start == "animate":
        final_animation(GUI.comparisons_2.number, canvas_2, GUI.list_2._list, time_list[1])
        GUI.start_drawing2.start = True
            
    if GUI.start_drawing3.start == "animate":
        final_animation(GUI.comparisons_3.number, canvas_3, GUI.list_3._list, time_list[2])
        GUI.start_drawing3.start = True
import time
import threading
import GUI


def bubble_sort(speed, _list, draw_info, final_animation, start, change, comparisons, data) -> None:
    print("Task 3 assigned to thread: {}".format(threading.current_thread().name))
    cont = 1
    for _ in range(len(_list._list)-1):
        for j in range(len(_list._list)-1):
            if _list._list[j] > _list._list[j+1]:
                _list._list[j], _list._list[j+1] = _list._list[j+1], _list._list[j]
                comparisons.number += 1
                time.sleep(speed)

                colors = ["green" if x == j else "red" if x == j+1 else "pink" if x > len(_list._list) - cont
                                       else "yellow" for x in range(len(_list._list))]

                data._list = [comparisons.number, colors]

                change.start = False

        cont += 1

    change.start = "animate"
    GUI.finish1 = True


def selection_sort(speed, _list, draw_info, final_animation, start, change, comparisons, data) -> None:
    for i in range(len(_list._list)):
        min_idx = i
        for j in range(i+1, len(_list._list)):
            comparisons.number += 1
            time.sleep(speed)

            colors = ["#99badd" if x == min_idx else "#ec7788" if x ==
                      j else "#badd99" if x < i else "#ffa500" for x in range(len(_list._list))]

            data._list = [comparisons.number, colors]
            
            change.start = False

            if _list._list[min_idx] > _list._list[j]:
                min_idx = j

        _list._list[i], _list._list[min_idx] = _list._list[min_idx], _list._list[i]

    change.start = "animate"
    GUI.finish2 = True

def insertion_sort(speed, _list, draw_info, final_animation, start, change, comparisons, data) -> None:
    actual = 1
    while actual < len(_list._list):
        before = actual
        while before > 0 and _list._list[before-1] > _list._list[before]:
            comparisons.number += 1
            time.sleep(speed)

            colors = ["#99badd" if x == before 
                    else "#772a3d" if x == before-1 
                    else "#ec7788" if x == actual 
                    else "#badd99" if x < actual 
                    else "#ffa500" for x in range(len(_list._list))]

            data._list = [comparisons.number, colors]
            
            change.start = False

            _list._list[before], _list._list[before-1] = _list._list[before-1], _list._list[before]
            before -= 1
        actual += 1

    change.start = "animate"
    GUI.finish3 = True
    #final_animation(comp_value, canva, _list._list)


def cocktail_sort(speed, _list, draw_info, final_animation, start, change, comparisons, data) -> None:
    cont = 0
    temp = 1
    left = 1
    right = len(_list._list) - 1
    verif = True
    while verif == True:
        verif = False
        for i in range(right):
            if _list._list[i] > _list._list[i+1]:
                comparisons.number += 1
                _list._list[i], _list._list[i+1] = _list._list[i+1], _list._list[i]
                time.sleep(speed)

                colors = ["#99badd" if x == i 
                        else "#772a3d" if x == i+1 
                        else "#ec7788" if x > len(_list._list) - temp or x < cont 
                        else "#ffa500" for x in range(len(_list._list))]

                data._list = [comparisons.number, colors]

                change.start = False

                verif = True

        verif = False
        temp += 1

        for i in range(right, left, -1):
            if _list._list[i] < _list._list[i-1]:
                comparisons.number += 1
                _list._list[i], _list._list[i-1] = _list._list[i-1], _list._list[i]
                time.sleep(speed)

                colors = ["#99badd" if x == i 
                        else "#772a3d" if x == i-1 
                        else "#ec7788" if x > len(_list._list) - temp or x < cont 
                        else "#ffa500" for x in range(len(_list._list))]

                data._list = [comparisons.number, colors]

                verif = True

        if verif == False:
            break

        left += 1
        cont += 1

    change.start = "animate"
    GUI.finish2 = True

def shell_sort(speed, _list, draw_info, final_animation, start, change, comparisons, data) -> None:
    div = len(_list._list) // 2
    while div > 0:
        for i in range(div, len(_list._list)):
            actual = _list._list[i]

            comparison = i
            while comparison >= div and _list._list[comparison - div] > actual:
                time.sleep(speed)

                colors = ["#99badd" if x == comparison - div 
                        else "#772a3d" if x == comparison 
                        else "#ffa500" for x in range(len(_list._list))]

                data._list = [comparisons.number, colors]

                change.start = False

                _list._list[comparison], _list._list[comparison - div] =  _list._list[comparison - div], _list._list[comparison]
                comparison -= div
                

        div = div // 2

    change.start = "animate"

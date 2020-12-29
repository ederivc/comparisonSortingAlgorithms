import GUI
import time

from random import randint
from templates import Objects
from datetime import datetime

def bubble_sort(
    speed: float, _list: list, change:Objects , comparisons: Objects, 
    data: Objects, _time: Objects
) -> None:
    _time.time_now = datetime.now()
    cont = 1
    for _ in range(len(_list._list)-1):
        for j in range(len(_list._list)-1):
            if _list._list[j] > _list._list[j+1]:
                _list._list[j], _list._list[j+1] = _list._list[j+1], _list._list[j]
                comparisons.number += 1
                time.sleep(speed)

                colors = ["#99badd" if x == j 
                        else "#ec7788" if x == j+1 
                        else "#badd99" if x > len(_list._list) - cont
                        else "#ffa500" for x in range(len(_list._list))]

                data._list = [comparisons.number, colors]

                change.start = False

        cont += 1

    _time.time_now = (datetime.now() - _time.time_now)
    change.start = "animate"


def selection_sort(
    speed: float, _list: list, change:Objects , comparisons: Objects, 
    data: Objects, _time: Objects
) -> None:
    _time.time_now = datetime.now()
    for i in range(len(_list._list)):
        min_idx = i
        for j in range(i+1, len(_list._list)):
            comparisons.number += 1
            time.sleep(speed)

            colors = ["#99badd" if x == min_idx 
                    else "#ec7788" if x == j 
                    else "#badd99" if x < i 
                    else "#ffa500" for x in range(len(_list._list))]

            data._list = [comparisons.number, colors]
            
            change.start = False

            if _list._list[min_idx] > _list._list[j]:
                min_idx = j

        _list._list[i], _list._list[min_idx] = _list._list[min_idx], _list._list[i]

    _time.time_now = (datetime.now() - _time.time_now)
    change.start = "animate"


def insertion_sort(
    speed: float, _list: list, change:Objects , comparisons: Objects, 
    data: Objects, _time: Objects
) -> None:
    _time.time_now = datetime.now()
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

    _time.time_now = (datetime.now() - _time.time_now)
    change.start = "animate"


def cocktail_sort(
    speed: float, _list: list, change:Objects , comparisons: Objects, 
    data: Objects, _time: Objects
) -> None:
    _time.time_now = datetime.now()
    temp = 1
    cont = 0
    n = len(_list._list)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):

        swapped = False
 
        for i in range(start, end):
            if (_list._list[i] > _list._list[i + 1]):
                comparisons.number += 1
                _list._list[i], _list._list[i + 1] = _list._list[i + 1], _list._list[i]
                swapped = True
                time.sleep(speed)

                colors = ["#99badd" if x == i 
                        else "#772a3d" if x == i+1 
                        else "#ec7788" if x > len(_list._list) - temp or x < cont 
                        else "#ffa500" for x in range(len(_list._list))]

                data._list = [comparisons.number, colors]
                
                change.start = False

        if (swapped == False):
            break

        swapped = False
        temp += 1

        end = end-1

        for i in range(end-1, start-1, -1):
            if (_list._list[i] > _list._list[i + 1]):
                comparisons.number += 1
                _list._list[i], _list._list[i + 1] = _list._list[i + 1], _list._list[i]
                time.sleep(speed)

                colors = ["#99badd" if x == i 
                        else "#772a3d" if x == i-1 
                        else "#ec7788" if x > len(_list._list) - temp or x < cont 
                        else "#ffa500" for x in range(len(_list._list))]

                data._list = [comparisons.number, colors]

                swapped = True
 

        start += 1
        cont += 1

    _time.time_now = (datetime.now() - _time.time_now)
    change.start = "animate"


def shell_sort(
    speed: float, _list: list, change:Objects , comparisons: Objects, 
    data: Objects, _time: Objects
) -> None:
    _time.time_now = datetime.now()
    div = len(_list._list) // 2
    while div > 0:
        for i in range(div, len(_list._list)):
            actual = _list._list[i]

            comparison = i
            while comparison >= div and _list._list[comparison - div] > actual:
                comparisons.number += 1
                time.sleep(speed)

                colors = ["#99badd" if x == comparison - div 
                        else "#772a3d" if x == comparison 
                        else "#ffa500" for x in range(len(_list._list))]

                data._list = [comparisons.number, colors]

                change.start = False

                _list._list[comparison], _list._list[comparison - div] =  _list._list[comparison - div], _list._list[comparison]
                comparison -= div
                

        div = div // 2

    _time.time_now = (datetime.now() - _time.time_now)
    change.start = "animate"

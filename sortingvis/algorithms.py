import time

from random import randint
from datetime import datetime

from typing import Any

def bubble_sort(
    delay: float, _list: list, change: bool , comparisons: int, 
    data: list, _time: int, is_sorting: Any
) -> None:
    _time.time_now = datetime.now()
    cont = 1
    for _ in range(len(_list.value)-1):
        for j in range(len(_list.value)-1):
            if _list.value[j] > _list.value[j+1]:
                _list.value[j], _list.value[j+1] = _list.value[j+1], _list.value[j]
                comparisons.number += 1
                time.sleep(delay)

                colors = [generate_bubble_colors(x, j, cont, len(_list.value)) for x, _ in enumerate(_list.value)]

                data.value = [comparisons.number, colors]

                is_sorting.status = "sorting"
                change.start = False

        cont += 1

    _time.time_now = (datetime.now() - _time.time_now)
    change.start = "animate"


def selection_sort(
    delay: float, _list: list, change: bool , comparisons: int, 
    data: list, _time: int, is_sorting: Any
) -> None:
    _time.time_now = datetime.now()
    for i in range(len(_list.value)):
        min_idx = i
        for j in range(i+1, len(_list.value)):
            comparisons.number += 1
            time.sleep(delay)

            colors = [generate_selection_colors(x, min_idx, j, i) for x, _ in enumerate(_list.value)]

            data.value = [comparisons.number, colors]
            
            is_sorting.status = "sorting"
            change.start = False

            if _list.value[min_idx] > _list.value[j]:
                min_idx = j

        _list.value[i], _list.value[min_idx] = _list.value[min_idx], _list.value[i]

    _time.time_now = (datetime.now() - _time.time_now)
    change.start = "animate"


def insertion_sort(
    delay: float, _list: list, change: bool , comparisons: int, 
    data: list, _time: int, is_sorting: Any
) -> None:
    _time.time_now = datetime.now()
    actual = 1
    while actual < len(_list.value):
        before = actual
        while before > 0 and _list.value[before-1] > _list.value[before]:
            comparisons.number += 1
            time.sleep(delay)

            colors = [generate_insertion_colors(x, before, actual) for x, _ in enumerate(_list.value)]

            data.value = [comparisons.number, colors]
            
            is_sorting.status = "sorting"
            change.start = False

            _list.value[before], _list.value[before-1] = _list.value[before-1], _list.value[before]
            before -= 1
        actual += 1

    _time.time_now = (datetime.now() - _time.time_now)
    change.start = "animate"


def cocktail_sort(
    delay: float, _list: list, change: bool , comparisons: int, 
    data: list, _time: int, is_sorting: Any
) -> None:
    _time.time_now = datetime.now()
    temp = 1
    cont = 0
    n = len(_list.value)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):

        swapped = False
 
        for i in range(start, end):
            if (_list.value[i] > _list.value[i + 1]):
                comparisons.number += 1
                _list.value[i], _list.value[i + 1] = _list.value[i + 1], _list.value[i]
                swapped = True
                time.sleep(delay)

                colors = ["#99badd" if x == i 
                        else "#772a3d" if x == i+1 
                        else "#ec7788" if x > len(_list.value) - temp or x < cont 
                        else "#ffa500" for x in range(len(_list.value))]

                data.value = [comparisons.number, colors]
                
                is_sorting.status = "sorting"
                change.start = False

        if (swapped == False):
            break

        swapped = False
        temp += 1

        end = end-1

        for i in range(end-1, start-1, -1):
            if (_list.value[i] > _list.value[i + 1]):
                comparisons.number += 1
                _list.value[i], _list.value[i + 1] = _list.value[i + 1], _list.value[i]
                time.sleep(delay)

                colors = ["#99badd" if x == i 
                        else "#772a3d" if x == i-1 
                        else "#ec7788" if x > len(_list.value) - temp or x < cont 
                        else "#ffa500" for x in range(len(_list.value))]

                data.value = [comparisons.number, colors]

                swapped = True
 

        start += 1
        cont += 1

    _time.time_now = (datetime.now() - _time.time_now)
    change.start = "animate"


def shell_sort(
    delay: float, _list: list, change: bool , comparisons: int, 
    data: list, _time: int, is_sorting: Any
) -> None:
    _time.time_now = datetime.now()
    div = len(_list.value) // 2
    while div > 0:
        for i in range(div, len(_list.value)):
            actual = _list.value[i]

            comparison = i
            while comparison >= div and _list.value[comparison - div] > actual:
                comparisons.number += 1
                time.sleep(delay)

                colors = [generate_shell_colors(x, comparison, div) for x, _ in enumerate(_list.value)]

                data.value = [comparisons.number, colors]

                is_sorting.status = "sorting"
                change.start = False

                _list.value[comparison], _list.value[comparison - div] =  _list.value[comparison - div], _list.value[comparison]
                comparison -= div
                

        div = div // 2

    _time.time_now = (datetime.now() - _time.time_now)
    change.start = "animate"

def getNextGap(gap): 
    gap = int((gap * 10)/13)

    if gap < 1: 
        return 1

    return gap 


def comb_sort(
    delay: float, _list: list, change: bool , comparisons: int, 
    data: list, _time: int, is_sorting: Any   
) -> None:
    _time.time_now = datetime.now()
    n = len(_list.value)  
    gap = n 
    swapped = True

    while gap !=1 or swapped == 1: 

        gap = getNextGap(gap) 

        swapped = False
  
        for i in range(0, n-gap): 
            if _list.value[i] > _list.value[i + gap]: 
                
                _list.value[i], _list.value[i + gap]=_list.value[i + gap], _list.value[i] 
                comparisons.number += 1
                time.sleep(delay)

                colors = ["#99badd" if x == i
                        else "#ec7788" if x == gap
                        else "#badd99" if x > gap
                        else "#ffa500" for x in range(len(_list.value))]

                data.value = [comparisons.number, colors]

                is_sorting.status = "sorting"
                change.start = False

                swapped = True

    _time.time_now = (datetime.now() - _time.time_now)
    change.start = "animate"


def gnome_sort(    
    delay: float, _list: list, change: bool , comparisons: int, 
    data: list, _time: int, is_sorting: Any
) -> None:
    _time.time_now = datetime.now()
    n = len(_list.value)
    index = 0

    while index < n: 

        if index == 0: 
            index = index + 1

        if _list.value[index] >= _list.value[index - 1]: 
            index = index + 1

            comparisons.number += 1
            time.sleep(delay)

            colors = ["#99badd" if x == index
                        else "#ec7788" if x == index - 1
                        else "#ffa500" for x in range(len(_list.value))]

            data.value = [comparisons.number, colors]

            is_sorting.status = "sorting"
            change.start = False

        else: 
            _list.value[index], _list.value[index-1] = _list.value[index-1], _list.value[index] 
            index = index - 1

    _time.time_now = (datetime.now() - _time.time_now)
    change.start = "animate"


def generate_bubble_colors(x: int, j: int, cont: int, length: int) -> str:
    if x == j:
        return "#99badd"
    if x == j + 1:
        return "#ec7788"
    if x > length - cont:
        return "#badd99"
    else:
        return "#ffa500"


def generate_selection_colors(x: int, ind: int, j: int, i: int) -> str:
    if x == ind:
        return "#99badd" 
    if x == j:
        return "#ec7788"
    if x < i:
        return "#badd99"
    else:
        return "#ffa500"


def generate_insertion_colors(x: int, before: int, actual: int) -> str:
    if x == before:
        return "#99badd"
    if x == before - 1:
        return "#772a3d"
    if x == actual:
        return "#ec7788"
    if x < actual:
        return "#badd99"
    else:
        return "#ffa500"


def generate_shell_colors(x: int, comparison: int, div: int) -> str:
    if x == comparison - div:
        return "#99badd"
    if x == comparison:
        return "#772a3d"
    else:
        return "#ffa500"
    
from typing import Union, List, Dict, Any


def filter_by_states(voc_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Эта функция фильтрует словари, находящиеся в принимаемом списке
    по значению ключа 'state'"""

    filtered_voc_list = [] # создаем пустой список который заполним отфильтрованными словарями
    for voc in voc_list: # перебираем словари в списке по значению ключа "state"
        if voc[state] == state: # если условие выполняется добавляем словарь в список
            filtered_voc_list.append(voc)
        else:
            pass
    return filtered_voc_list # возвращаем список отфильтрованных словарей


def sort_by_date(voc_list: List[Dict[str, Any]], sorting_methode: str = "descending") -> List[Dict[str, Any]]:
    """Эта функция сортирует принимаемый список словарей по дате"""
    sorted_voc_list = [] # создаем пустой список, который заполним отсортированными по дате словарями

    for voc in voc_list: # проверяем словари в списке на наличие ключа 'date'
        if "date" not in voc:
            raise KeyError(f"Словарь {voc} не содержит ключа 'date'")

    for voc in voc_list: # перебираем словари в списке, сортируем их и помещаем в новый сортированный список
        if sorting_methode == "descending": # Да и метод сортировки тоже не забываем использовать который задан
            sorted_voc_list = sorted(voc_list, key=lambda x: x["date"], reverse=True)
        elif sorting_methode == "ascending":
            sorted_voc_list = sorted(voc_list, key=lambda x: x["date"], reverse=False)
        else:
            sorted_voc_list = voc_list # если метод сортировки не задан почему-то - возвращаем исходный список
    return sorted_voc_list

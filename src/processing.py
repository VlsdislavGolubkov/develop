from typing import Union, List, Dict, Any


def filter_by_states(voc_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    filtered_voc_list = []
    for voc in voc_list:
        if voc[state] == state:
            filtered_voc_list.append(voc)
        else:
            pass
    return filtered_voc_list


def sort_by_date(voc_list: List[Dict[str, Any]], sorting_methode: str = "descending") -> List[Dict[str, Any]]:
    sorted_voc_list = []

    for voc in voc_list:
        if "date" not in voc:
            raise KeyError(f"Словарь {voc} не содержит ключа 'date'")

    for voc in voc_list:
        if sorting_methode == "descending":
            sorted_voc_list = sorted(voc_list, key=lambda x: x["date"], reverse=True)
        elif sorting_methode == "ascending":
            sorted_voc_list = sorted(voc_list, key=lambda x: x["date"], reverse=False)
        else:
            sorted_voc_list = voc_list
    return sorted_voc_list

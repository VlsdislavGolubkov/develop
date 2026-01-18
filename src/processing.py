def filter_by_states(voc_list, state="EXECUTED"):
    filtered_voc_list = []
    for voc in voc_list:
        if voc[state] == state:
            filtered_voc_list.append(voc)
        else:
            pass


def sort_by_date(voc_list, sorting_methode="descending"):
    sorted_voc_list = []

    for voc in voc_list:
        if "date" not in voc:
            raise KeyError(f"Словарь {voc} не содержит ключа 'date'")

    for voc in voc_list:
        if sorting_methode == "descending":
            sorted_voc_list = sorted(voc, key=lambda x: x["date"], reverse=True)
        elif sorting_methode == "ascending":
            sorted_voc_list = sorted(voc, key=lambda x: x["date"], reverse=False)
        else:
            sorted_voc_list = voc_list
    return sorted_voc_list

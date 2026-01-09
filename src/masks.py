from typing import Union


# Реализуем функцию получения номера карты и возврата ее маски
def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция, которая принимает числовое или строковое
    значение номера карты и меняет некоторые символы на звездочки ***"""
    divided_card_number: str = (
        str(card_number)[:6] + "*" * 6 + str(card_number)[12:]
    )  # заменяем нужные символы звездочками
    masked_card_number = " ".join(divided_card_number[i : i + 4] for i in range(0, len(divided_card_number), 4))
    # разделяем число на группы по 4 символа
    return masked_card_number  # возвращаем номер карты с маской


#  Реализуем функцию получения номера счета и возврата его маски
def get_mask_account(account: Union[str, int]) -> str:
    """Функция, которая принимает числовое или строковое
    значение номера счета и возвращает последние 4 числа,
    а остальные заменяет двумя звездочками"""
    masked_account: str = f"**{str(account)[-4:]}"  # берем последние 4 числа и добавляем две звезды в начале
    return masked_account  # Возвращаем номер счета с маской

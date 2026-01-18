from typing import Union

def get_mask_account(account_number: str) -> str:
    """Маскирует номер карты или счета"""

    # Обработка счета
    if 'счет' in account_number.lower():
        # Извлекаем цифры
        digits = ''.join(filter(str.isdigit, account_number))
        if len(digits) >= 4:
            masked_account_number = f"Счет **{digits[-4:]}"

    return masked_account_number.strip()

def get_mask_card_number(card_number: str) -> str:
    # Разделяем на тип карты и номер
    # Тип карты - все буквы и пробелы до первой цифры
    card_type = ""
    card_number1 = ""

    # Ищем первую цифру
    for char in card_number:
        if char.isdigit():
            # Нашли первую цифру - всё что после будет номером
            # Находим индекс этой цифры
            idx = card_number.index(char)
            card_type = card_number[:idx].strip()
            card_number1 = card_number[idx:]

        # Маскируем номер карты
        digits = ''.join(filter(str.isdigit, card_number1))
        if len(digits) >= 16:
            masked_number = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
        else:
            masked_number = card_number1

    return f"{card_type} {masked_number}".strip()

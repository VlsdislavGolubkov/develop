def mask_account_card (card_or_account_number:str):
    """Маскирует номер карты или счета"""

    # Обработка счета
    if 'счет' in card_or_account_number.lower():
        # Извлекаем цифры
        digits = ''.join(filter(str.isdigit, card_or_account_number))
        if len(digits) >= 4:
            return f"Счет **{digits[-4:]}"
        return card_or_account_number

    # Обработка карты
    else:
        # Разделяем на тип карты и номер
        # Тип карты - все буквы и пробелы до первой цифры
        card_type = ""
        card_number = ""

        # Ищем первую цифру
        for char in card_or_account_number:
            if char.isdigit():
                # Нашли первую цифру - всё что после будет номером
                # Находим индекс этой цифры
                idx = card_or_account_number.index(char)
                card_type = card_or_account_number[:idx].strip()
                card_number = card_or_account_number[idx:]
                break

        # Если не нашли цифр
        if not card_number:
            return card_or_account_number

        # Маскируем номер карты
        digits = ''.join(filter(str.isdigit, card_number))
        if len(digits) >= 16:
            masked_number = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
        else:
            masked_number = card_number

        return f"{card_type} {masked_number}".strip()


def get_date(date_ISO_8601:str):
    date=date_ISO_8601.replace("-", "")
    year=date[:4]
    month=date[4:6]
    day=date[6:8]
    return f"{day}.{month}.{year}"

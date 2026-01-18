from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: str) -> str:
    if 'счет' in card_or_account_number.lower():
        masked_account_number = get_mask_account(card_or_account_number)
        return masked_account_number
    else:
        masked_card_number = get_mask_card_number(card_or_account_number)
        return masked_card_number


def get_date(date_iso_8601: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""
    date = date_iso_8601.replace("-", "")
    year = date[:4]
    month = date[4:6]
    day = date[6:8]
    return f"{day}.{month}.{year}"

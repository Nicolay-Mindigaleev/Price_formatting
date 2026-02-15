import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def format_number(value: (int)) -> str:
    if value >= 1_000_000_000:
        num = value / 1_000_000_000
        suffix = " млрд ₽"
    elif value >= 1_000_000:
        num = value / 1_000_000
        suffix = " млн ₽"
    elif value >= 1000:
        num = value / 1000
        suffix = " тыс ₽"
    else:
        return f"{value} ₽"
    formatted = f"{num:.1f}".rstrip('0').rstrip('.')
    return formatted + suffix
def format_price(price_from: int | None = None, price_to: int | None = None) -> str:
    if price_from is None and price_to is None:
        raise ValueError("At least one value is required")
    range_of_price = ""      
    if price_from is not None and price_to is None:
        formated_price_from = format_number(price_from)
        range_of_price += "от " + formated_price_from
    elif price_from is None and price_to is not None:
        formated_price_to = format_number(price_to)
        range_of_price += "до " + formated_price_to
    else:
        formated_price_from = format_number(price_from)
        formated_price_to = format_number(price_to)
        range_of_price += formated_price_from + " - " + formated_price_to
    return range_of_price.replace(".",",")
a = 2100
b = 300_000
print(f"{format_price(price_from= a, price_to= b)}")
        

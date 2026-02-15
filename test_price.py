from main import format_price
import pytest

def test_negative_value():
    with pytest.raises(ValueError, match="Value must be positive"):
        format_price(price_from=-10)
    
    with pytest.raises(ValueError, match="Value must be positive"):
        format_price(price_to=-5)
    
    with pytest.raises(ValueError, match="Value must be positive"):
        format_price(-10, -5)

def test_zero_values():
    assert format_price(price_from=0, price_to=100500) == "до 100,5 тыс ₽"

    assert format_price(price_from=2001, price_to=0) == "от 2 тыс ₽"
    
    with pytest.raises(ValueError, match="At least one value is required"):
        format_price(price_from=0, price_to=0)

def test_auto_swap():
    assert format_price(300000, 2001) == "2 тыс ₽ - 300 тыс ₽"

def test_values_from_the_task():
    value_beg_1 = 20
    value_end_1 = 30
    value_beg_2 = 20
    value_end_2 = 300000
    value_beg_3 = 2001
    value_end_3 = 300000
    value_beg_4 = 2001
    value_end_5 = 100500
    value_end_6 = 10_050_000
    
    assert format_price(value_beg_1, value_end_1) == "20 ₽ - 30 ₽"
    assert format_price(value_beg_2, value_end_2) == "20 ₽ - 300 тыс ₽"
    assert format_price(value_beg_3, value_end_3) == "2 тыс ₽ - 300 тыс ₽"
    assert format_price(value_beg_4) == "от 2 тыс ₽"
    assert format_price(price_to=value_end_5) == "до 100,5 тыс ₽"
    assert format_price(price_to=value_end_6) == "до 10,1 млн ₽"
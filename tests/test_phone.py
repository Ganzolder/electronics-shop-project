from src.phone import Phone
from src.item import Item

def test_isinstance_of_item():
    ph_class = Phone("Iphone 14", 135000, 4, 2)
    if not isinstance(ph_class, Item):
        raise TypeError('Something went wrong')
    return ph_class

def test_repr_func():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
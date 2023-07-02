"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


#  testcase#1 isinstance
def test_isinstance_creation():

    item = Item('iphone', 99000, 20)
    assert isinstance(item, Item)

#  testcase#2 testing discounting
def test_apply_discount():
    item = Item('iphone', 99000, 20)
    Item.pay_rate = 0.5
    assert item.apply_discount() == 49500

#  testcase#3 testing calculate_total
def test_calculate_total_price():
    item = Item('iphone', 99000, 20)
    assert item.calculate_total_price() == 1980000

#  testcase#4 testing count of instances
def test_instance_registrator():
    assert len(Item.all) != []

#  testcase#5 testing setting
def test_name_setter():
    item = Item('iphone', 99000, 20)
    item.name = 'samsung'
    assert item.name == 'samsung'
    item.name = 'RussianSuperSmartphone'
    assert len(item.name) == 10

#  testcase#6 testing csv parser
def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert Item.all[0].name == 'Смартфон'


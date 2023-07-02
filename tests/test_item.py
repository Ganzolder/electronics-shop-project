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
    item = Item('iphone', 99000, 20)
    assert len(Item.all) != []
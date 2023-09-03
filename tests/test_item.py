"""Здесь надо написать тесты с использованием pytest для модуля item."""
import src.item
import pytest
from src.item import Item, DmgdFileException, EmptyFileException


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

def test_item_dunders():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'

def test_EmptyFileException():
    Item.filepath = 'C:\python\electronics-shop-project\src\items2.csv'
    with pytest.raises(EmptyFileException):
        Item.instantiate_from_csv()

def test_DmgdFileException():
    Item.filepath = 'C:\python\electronics-shop-project\src\items_dmgd.csv'
    with pytest.raises(DmgdFileException):
        Item.instantiate_from_csv()


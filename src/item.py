import csv
import os.path


class EmptyFileException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = 'FileNotFoundError: Отсутствует файл item.csv'


class DmgdFileException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = 'InstantiateCSVError: Файл item.csv поврежден'


class InstantiateCSVError:
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []
    filepath = 'C:\python\electronics-shop-project\src\items2.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        short_name = name[:10]
        self.__name = short_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = int(self.quantity) * int(self.price)
        return total_price

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = int(self.price) * float(self.__class__.pay_rate)
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        try:
            if os.path.isfile(cls.filepath):
                with open(cls.filepath, newline='') as csvfile:
                    reader = list(csv.DictReader(csvfile))
                    for row in reader:
                        if len(row) == 3:
                            item = Item(row['name'], row['price'], row['quantity'])
                            Item.all.append(item)
                        else:
                            raise DmgdFileException
            else:
                raise EmptyFileException

        except EmptyFileException as ex:
            print(ex.message)
        except DmgdFileException as ex:
            print(ex.message)



    @staticmethod
    def string_to_number(num):
        return int(float(num))

    def __add__(self, other):
        if not isinstance(other, Item):
            raise TypeError('Не является экземпляром класса или субкласса Item')
        return self.quantity + other.quantity

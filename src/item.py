import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []

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

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = int(self.price) * float(self.__class__.pay_rate)
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open('C:\python\electronics-shop-project\src\items.csv', newline='') as csvfile:
            reader = list(csv.DictReader(csvfile))
            for row in reader:
                item = Item(row['name'], row['price'], row['quantity'])
                Item.all.append(item)

    @staticmethod
    def string_to_number(num):
        return int(float(num))

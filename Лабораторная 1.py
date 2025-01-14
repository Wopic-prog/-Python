import doctest
from abc import ABC, abstractmethod


class Scissors(ABC):
    def __init__(self, blade_length: float, is_sharp: bool):
        """
        Создание и подготовка к работе объекта "Ножницы".

        :param blade_length: Длина лезвия в сантиметрах.
        :param is_sharp: Состояние остроты ножниц (True — острые, False — тупые).

        Примеры:
        >>> scissors = ScissorsImplementation(15.5, True)
        """
        if not isinstance(blade_length, (int, float)):
            raise TypeError("Длина лезвия должна быть числом.")
        if blade_length <= 0:
            raise ValueError("Длина лезвия должна быть положительным числом.")
        self.blade_length = blade_length

        if not isinstance(is_sharp, bool):
            raise TypeError("Состояние остроты должно быть булевым значением.")
        self.is_sharp = is_sharp

    @abstractmethod
    def cut(self, material: str) -> str:
        """
        Осуществляет разрезание материала.

        :param material: Материал для разрезания.
        :return: Сообщение о результате разрезания.

        Примеры:
        >>> scissors = ScissorsImplementation(15.5, True)
        >>> scissors.cut("бумага")
        """
        ...

    @abstractmethod
    def sharpen(self) -> None:
        """
        Заточка ножниц. Делает ножницы острыми.

        Примеры:
        >>> scissors = ScissorsImplementation(15.5, False)
        >>> scissors.sharpen()
        """
        ...


class ScissorsImplementation(Scissors):
    def cut(self, material: str) -> str:
        if not self.is_sharp:
            return f"Ножницы слишком тупые, чтобы разрезать {material}."
        return f"Материал {material} успешно разрезан ножницами длиной {self.blade_length} см."

    def sharpen(self) -> None:
        self.is_sharp = True

class AutoDullingScissors(Scissors):
    def __init__(self, blade_length: float, is_sharp: bool, durability: int):
        """
        Создание и подготовка к работе объекта "Самозатупляющиеся ножницы".

        :param blade_length: Длина лезвия в сантиметрах.
        :param is_sharp: Состояние остроты ножниц (True — острые, False — тупые).
        :param durability: Количество раз, которое ножницы могут разрезать материал до затупления.

        Примеры:
        >>> scissors = AutoDullingScissors(12.0, True, 3)
        """
        super().__init__(blade_length, is_sharp)
        if not isinstance(durability, int) or durability < 0:
            raise ValueError("Износ должен быть положительным целым числом.")
        self.durability = durability
        self.initial_durability = durability

    def cut(self, material: str) -> str:
        if not self.is_sharp:
            return f"Ножницы слишком тупые, чтобы разрезать {material}."
        if self.durability <= 0:
            self.is_sharp = False
            return f"Ножницы затупились и не могут разрезать {material}."
        self.durability -= 1
        return f"Материал {material} успешно разрезан ножницами длиной {self.blade_length} см."

    def sharpen(self) -> None:
        self.is_sharp = True
        self.durability = self.initial_durability


if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров в документации

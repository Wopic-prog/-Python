from typing import Any


class Rocket:
    def __init__(self, name: str, range_km: int) -> None:
        self._name = name
        self.range_km = range_km

    def launch(self) -> str:
        return "Запуск ракеты..."

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self._name}, дальность {self.range_km} км"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, range_km={self.range_km})"


class GuidedRocket(Rocket):
    def __init__(self, name: str, range_km: int, guidance_system: str) -> None:
        super().__init__(name, range_km)
        self.guidance_system = guidance_system

    def launch(self) -> str:
        return "Запуск управляемой ракеты!"

    def __str__(self) -> str:
        return f"Управляемая ракета {self._name}, система наведения: {self.guidance_system}, дальность {self.range_km} км"


class UnguidedRocket(Rocket):
    def __init__(self, name: str, range_km: int, propulsion_type: str) -> None:
        super().__init__(name, range_km)
        self.propulsion_type = propulsion_type

    def launch(self) -> str:
        return "Запуск неуправляемой ракеты!"

    def __str__(self) -> str:
        return f"Неуправляемая ракета {self._name}, тип двигателя: {self.propulsion_type}, дальность {self.range_km} км"

from abc import ABC, abstractmethod
from enum import Enum


class Engine(ABC):
    @abstractmethod
    def move(self):
        ...

    @classmethod
    def create_engine(cls, engine_type: str):
        return EngineType[engine_type.upper()].value()


class CombustionEngine(Engine):
    def move(self):
        print("I'm moving using explosions!!! So badass *_*")


class ElectricEngine(Engine):
    def move(self):
        print(
            "I'm moving around by using the power of electricity. Good for the environment!"
        )


class EngineType(Enum):
    COMBUSTION = CombustionEngine
    ELECTRIC = ElectricEngine


if __name__ == "__main__":
    # engine = ElectricEngine()
    engine = Engine.create_engine("combustion")
    engine.move()

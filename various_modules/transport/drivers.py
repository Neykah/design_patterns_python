from abc import ABC, abstractmethod


class Driver(ABC):
    @abstractmethod
    def navigate(self):
        ...


class Robot(Driver):
    def navigate(self):
        print("I'm driving around automatically, but I cannot solve a CATCHA...")


class Human(Driver):
    def navigate(self):
        print("I'm driving around manually. I'm vintage!")


if __name__ == "__main__":
    driver = Human()
    driver.navigate()

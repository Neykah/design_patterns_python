from enum import Enum

from drivers import Driver, Human, Robot
from engines import Engine


class Transport:
    def __init__(self, engine_type: str, driver: Driver):
        self.engine = Engine.create_engine(engine_type)
        self.driver = driver

    def deliver(self, destination: str, cargo: str):
        print(f"The transport needs to move to {destination} to deliver {cargo}...")
        self.driver.navigate()
        self.engine.move()


if __name__ == "__main__":
    driver = Robot()
    transport = Transport("electric", driver)
    transport.deliver("Osaka", "Beer")

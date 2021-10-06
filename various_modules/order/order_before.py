from dataclasses import dataclass
from datetime import date


@dataclass
class Item:
    name: str
    price: int
    weight: int


class Order:
    def __init__(self, items: list[Item], shipping: str):
        self.line_items = items
        self._shipping_type = shipping
        self.shipping_date = date.today()

    @property
    def total(self) -> int:
        return sum(item.price for item in self.line_items)

    @property
    def total_weight(self) -> int:
        return sum(item.weight for item in self.line_items)

    @property
    def shipping(self) -> str:
        return self._shipping_type

    @shipping.setter
    def shipping(self, ship_type: str) -> None:
        self._shipping_type = ship_type

    def get_shipping_cost(self) -> int:
        if self.shipping == "ground":
            # Free ground delivery on big orders
            if self.total > 100:
                return 0
            # $1.5 per kilogram, but $10 minimum
            return max(10, self.total_weight * 1.5)

        if self.shipping == "air":
            # $3 per kilogram, but $20 minimum
            return max(20, self.total_weight * 3)



if __name__ == "__main__":
    items = [
        Item("Sturdy Chair", 230, 40),
        Item("Amazing Desk", 400, 100),
        Item("Bright Lamp", 50, 4),
    ]

    order = Order(items, "ground")
    assert order.get_shipping_cost() == 0
    assert order.total == 230 + 400 + 50
    assert order.total_weight == 40 + 100 + 4
    print("All unit tests have passed.")

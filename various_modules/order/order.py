from datetime import date
from dataclasses import dataclass

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shipping import Shipping, Item


@dataclass
class Item:
    name: str
    price: int
    weight: int


class Order:
    def __init__(self, items: list["Item"], shipping: "Shipping"):
        self.line_items = items
        self.shipping = shipping
        self.shipping_date = date.today()

    @property
    def total(self) -> int:
        return sum(item.price for item in self.line_items)

    @property
    def total_weight(self) -> int:
        return sum(item.weight for item in self.line_items)

    def get_shipping_cost(self) -> float:
        return self.shipping.get_cost(self)

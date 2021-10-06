from datetime import date
from abc import ABC, abstractmethod

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from order import Order

class Shipping(ABC):
    @abstractmethod
    def get_cost(order: "Order") -> float:
        ...

    @abstractmethod
    def get_date(order: "Order") -> date:
        ...

class Ground(Shipping):
    def get_cost(self, order: "Order") -> float:
        if order.total > 100:
            return 0
        return max(10, order.total_weight * 1.5)

    def get_date(self, order: "Order") -> date:
        return order.shipping_date


class Air(Shipping):
    def get_cost(self, order: "Order") -> float:
        return max(20, order.total_weight * 3)

    def get_date(self, order: "Order") -> date:
        return order.shipping_date

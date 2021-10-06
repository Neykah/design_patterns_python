from order import Order, Item
from shipping import Air, Ground

if __name__ == "__main__":
    items = [
        Item("Sturdy Chair", 230, 40),
        Item("Amazing Desk", 400, 100),
        Item("Bright Lamp", 50, 4),
    ]

    order = Order(items, Ground())
    assert (ship_cost := order.get_shipping_cost()) >= 0
    print("Shipping cost: ", ship_cost)
    assert order.total == 230 + 400 + 50
    assert order.total_weight == 40 + 100 + 4
    print("All unit tests have passed.")

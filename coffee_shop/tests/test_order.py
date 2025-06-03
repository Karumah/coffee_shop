from order import Order
from customer import Customer
from coffee import Coffee

def test_create_order():
    customer = Customer("Sam")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 4.5)
    assert order.price == 4.5
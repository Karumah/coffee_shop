from customer import Customer
from coffee import Coffee

class Order:
    _all_orders = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self._all_orders.append(self)
        coffee._orders.append(self)  
        customer._orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("customer order must be a customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("Order coffee must be a Coffee instance.")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not (isinstance(value, float) or isinstance(value, int)):
            raise TypeError("Price must be a float or int.")
        if not (1.0 <= float(value) <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = float(value)
class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters long")
        self._name = value

    def orders(self):
        return self._orders  
    
    def coffees(self):
        from coffee import Coffee  
        return list({order.coffee for order in self._orders})
    
    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        top_customer = None
        top_spent = 0
        for customer in coffee.customers():
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total > top_spent:
                top_spent = total
                top_customer = customer
        return top_customer
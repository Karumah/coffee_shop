class Coffee :
    def __init__(self,name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name
    
    def orders(self):
        return self._orders

    def customers(self):
        from customer import Customer 
        return list({order.customer for order in self._orders})

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = value   

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders) 
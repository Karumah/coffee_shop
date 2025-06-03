from customer import Customer
from coffee import Coffee
from order import Order

customer1 = Customer("Trevor")
customer2 = Customer("Grace")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

Order(customer1, coffee1, 4.0)
Order(customer2, coffee1, 5.0)
Order(customer1, coffee2, 4.5)



print(f"Customer 1: {customer1.name}")
print(f"{coffee1.name} Customers:", [c.name for c in coffee1.customers()])
print(f"{coffee1.name} Num Orders:", coffee1.num_orders())
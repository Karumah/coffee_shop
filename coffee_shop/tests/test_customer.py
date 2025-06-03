from customer import Customer

def test_customer_name():
    c1 = Customer("Trevor")
    assert c1.name == "Trevor"
    
    c2 = Customer("Grace")
    assert c2.name == "Grace"

def test_bad_names():
    try:
        Customer("MyNameIsTrevorMukundi")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    try:
        Customer(123)
        assert False, "Should have raised TypeError"
    except TypeError:
        pass
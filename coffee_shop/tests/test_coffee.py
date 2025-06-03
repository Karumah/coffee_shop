from coffee import Coffee

def test_create_coffee():
    my_coffee = Coffee("Latte")
    assert my_coffee.name == "Latte"

def test_bad_coffee_name():
    try:
        Coffee(123)
        assert False  
    except TypeError:
        pass  
def add_int(x):
    temp = x + 3
    return temp

def floating_add(x):
    temp = x + 2.39
    temp = round(temp, 2)
    return temp

def greet(name):
    greeting = f"Hello, {name}"
    return greeting

def is_positive(x):
    is_pos = x > 0
    return is_pos

def test_add_int():
    assert add_int(3) == 6

def test_floating_add():
    assert floating_add(2) == 4.39

def test_greet():
    assert greet("Jason") == "Hello, Jason"

def test_is_positive():
    assert is_positive(3) == True

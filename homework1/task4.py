def calculate_discount(price, discount):
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        print("Enter a valid numeric value for price and discount")
        return -1

    if discount < 0 or discount > 100:
        print("Discount must be a value between 0 and 100")
        return -1

    discounted_price = round(price - (price * (discount / 100)), 2)
    print(f"The new price after a %{discount} discount is ${discounted_price}, the original price was ${price}")

    return discounted_price

discounted = calculate_discount(100.50, 10.5)
print(discounted)

def test_calculate_discount_with_integers():
    assert calculate_discount(100, 20) == 80  

def test_calculate_discount_with_floats():
    assert calculate_discount(100.50, 10.5) == 89.95

def test_calculate_discount_zero_discount():
    assert calculate_discount(200, 0) == 200  

def test_calculate_discount_full_discount():
    assert calculate_discount(75, 100) == 0

def test_calculate_discount_invalid_inputs():
    assert calculate_discount("100", 20) == -1  
    assert calculate_discount(100, "20") == -1  
    assert calculate_discount(100, -10) == -1   
    assert calculate_discount(100, 110) == -1 
def check_number(x):
    state = ""
    if x > 0:
        state = "Positive"
    elif x < 0:
        state = "Negative"
    else:
        state = "Zero"
    return state

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def print_primes():
    primes = []
    num = 2
    for j in range(10):
        while is_prime(num) == False:
            num += 1
        primes.append(num)
        num += 1

    print(primes)


def sum_100():
    counter = 1
    sum = 0
    while counter <= 100:
        sum += counter
        counter += 1
    print(sum)

check_number(3)
print_primes()
sum_100()

def test_check_number():
    assert check_number(3) == "Positive"

def test_for_loop(capsys):
    print_primes()
    captured = capsys.readouterr()
    assert captured.out == "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]\n"

def test_while_loop(capsys):
    sum_100()
    captured = capsys.readouterr()
    assert captured.out == "5050\n"
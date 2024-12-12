def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Nuh uh")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def is_prime(number):
    if number <= 1:
        raise ValueError("Nuh uh")
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == "__name__":
    print(fibonacci(10))
    print(is_prime(2))

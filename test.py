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
    if number == 0 or number == -1:
        raise ValueError("Nuh uh")
    elif number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def primes_in(n):
    if n < 2:
        return []
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == "__main__":
    print(fibonacci(10))
    print(is_prime(1)) 
    print(is_prime(0)) 
    print(is_prime(-1)) 
    print(primes_in(10))  


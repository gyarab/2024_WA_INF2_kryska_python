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
        raise ValueError("this aint it")
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

def primes_in_range(a, b):

    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both a and b must be integers")
    if a > b:
        raise ValueError("a must be less than or equal to b")
    
    primes = []
    
    if is_prime(a):
        primes.append(a)
    
    for i in range(a + 1, b + 1):
        if is_prime(i):
            primes.append(i)
    
    if not primes:
        return ()
    
    return primes

def split_into_threes(text):

    if not isinstance(text, str):
        raise ValueError("no string here buddy")
    
    result = []
    
    for i in range(0, len(text), 3):
        result.append(text[i:i+3]) 
    
    return result







def caesar_encode(text):
    if not all(c.isalpha() or c == ' ' or c == '.' for c in text):
        raise ValueError("Text obsahuje nepovolené znaky")
    
    result = []
    
    for char in text:
        if char.islower():
            new_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
            result.append(new_char)
        elif char.isupper(): 
            new_char = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            result.append(new_char)
        elif char == ' ': 
            result.append(' ')
        elif char == '.':  
            result.append('.')
    
    return ''.join(result)


def caesar_decode(code):
    if not all(c.isalpha() or c == ' ' or c == '.' for c in code):
        raise ValueError("Text obsahuje nepovolené znaky")
    
    result = []
    
    for char in code:
        if char.islower(): 
            new_char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
            result.append(new_char)
        elif char.isupper(): 
            new_char = chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
            result.append(new_char)
        elif char == ' ': 
            result.append(' ')
        elif char == '.':  
            result.append('.')
    
    return ''.join(result)

if __name__ == "__main__":
    print(fibonacci(10))
    print(is_prime(3)) 
    print(primes_in(10))  
    print(primes_in_range(8, 10))  
    print(primes_in_range(2, 5))
    try:
        print(split_into_threes("abcdefg"))  
        print(split_into_threes("abcd")) 
        print(split_into_threes("a"))    
        print(split_into_threes(123))    
    except ValueError as e:
        print(e) 

    try:
        text = "Hello World."
        encoded_text = caesar_encode(text)
        decoded_text = caesar_decode(encoded_text)
        
        print(f"Original: {text}")
        print(f"Encoded: {encoded_text}")
        print(f"Decoded: {decoded_text}")
        
        print(caesar_encode("Hello@World"))
    except ValueError as e:
        print(e)

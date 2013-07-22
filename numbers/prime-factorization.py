__author__ = 'JoshMa'

def is_a_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input('Enter the number to find prime factors of: '))
    factors = []

    for i in range(2, n + 1):
        if n % 1 == 0:
            if is_a_prime(i):
                factors.append(i)
                n /= i

    print(factors)


__author__ = 'JoshMa'

def is_a_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = 0
    while True:
        n += 1
        while not is_a_prime(n):
            n += 1
        print(n)
        if not input('Print the next prime number? [y/n]: ') == 'y':
            break




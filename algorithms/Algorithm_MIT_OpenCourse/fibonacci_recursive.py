

def fibonacci(n):
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 1

    # Recursive case
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


# print('Enter the N: ')
n = input('Enter the N: ')
print(fibonacci(int(n)))

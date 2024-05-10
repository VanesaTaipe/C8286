import time

def fib(n: int) -> None:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def print_fib(number: int) -> None:
    print(f'fib({number}) is {fib(number)}')

def fibs_no_threading():
    print_fib(40)
    print_fib(41)

start = time.time()
fibs_no_threading()
end = time.time()
print(f'Completed in {end-start:.4f} seconds.')

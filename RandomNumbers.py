import random

def print_smallest(n):
    list = [random.randint(0, 1000) for _ in range(500)]
    list.sort()
    print list[n]

print_smallest(10)

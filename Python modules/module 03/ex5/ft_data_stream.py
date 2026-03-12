import random
from time import time


def get_event(num: int):
    names = ['Bob', 'Lucy', 'Marty', 'Tyler', 'Grno']
    events = ['killed monster', 'found treasure', 'leveled up']
    number = 0
    while number <= num:
        number += 1
        yield (number, names[random.randint(0, 4)],
               events[random.randint(0, 2)], random.randint(0, 20))


def fibo(num: int):
    old = 0
    new = 1
    count = 1
    while count <= num:
        yield old
        old, new = new, old + new
        count += 1


def isprime(number: int) -> int:
    count = 0
    if number == 2:
        return 1
    for i in range(2, number):
        if number % i == 0:
            count += 1
        if count == 1:
            return 0
    return 1


def prime(num: int):
    primenum = 2
    count = 0
    while count < num:
        if isprime(primenum):
            primenum += 1
            count += 1
            yield primenum - 1
        else:
            primenum += 1


print("=== Game Data Stream Processor ===\n")
print("Processing 1000 game events...\n")
start = time()
proccesed_games = 0
high = 0
treasue = 0
lvlup = 0

for event in get_event(1000):
    print(f"Event {event[0]}: Player {event[1]} (level {event[3]}) {event[2]}")
    proccesed_games = event[0]
    if event[3] >= 10:
        high += 1
    if event[2] == "found treasure":
        treasue += 1
    elif event[2] == "leveled up":
        lvlup += 1

print("\n=== Stream Analytics ===")
print("Total events processed:", proccesed_games)
print("High-level players (10+):", high)
print("Treasure events:", treasue)
print("Level-up events:", lvlup)
print("\nMemory usage: Constant (streaming)")
end = time()
print(f"Processing time: {(end - start):.5f} seconds\n")
print("=== Generator Demonstration ===")
print("Fibonacci sequence (first 10): ", end="")
a = 1
for i in fibo(10):
    if a < 10:
        print(i, ", ", sep="", end="")
    else:
        print(i, end="\n")
    a += 1
a = 1
print("Prime numbers (first 5): ", end="")
for i in prime(5):
    if a < 5:
        print(i, ", ", sep="", end="")
    else:
        print(i, end="\n")
    a += 1

def running_total(numbers):
    total = 0
    for n in numbers:
        total += n
        yield total

data = [5, 10, 3, 7]

for value in running_total(data):
    print(value)

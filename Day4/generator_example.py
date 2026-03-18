def simple_numbers():
    yield 1
    yield 2
    yield 3


for num in simple_numbers():
    print(num)


def generate_numbers():
    for i in range(1, 11):
        yield i


def square_numbers(numbers):
    for n in numbers:
        yield n * n


def filter_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n


nums = generate_numbers()
squared = square_numbers(nums)
even_numbers = filter_even(squared)

for value in even_numbers:
    print(value)



# Pipeline flow:
# generate_numbers()
#         ↓
# square_numbers()
#         ↓
# filter_even()
#         ↓
# print()
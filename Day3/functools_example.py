# from functools import partial

# def add(a,b):
#     return a + b

# temp = partial(add, 1)
# print("We are learnig python")
# print("This is the addition of two numbers")
# print(temp(3))


# from functools import partialmethod

# class main:
#     def __init__(self):
#         self.name = "Aatish"
#     def change(self, changeName):
#         self.name = changeName
#     change_to_ayush = partialmethod(change,changeName="Ayush")
#     change_to_avneesh = partialmethod(change,changeName="Avneesh")

# m = main()
# print(m.name)
# m.change_to_ayush()
# print(m.name)
# m.change_to_avneesh()
# print(m.name)

from functools import reduce

result = reduce(lambda x,y: x+y, [5,5] )

print(result)

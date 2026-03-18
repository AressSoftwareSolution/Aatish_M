# with open("Example.txt",mode="r") as file:
#     content = file.read()
# print(content)



# with open("Example.txt", mode="w") as file:
#     file.write("Good morning welcome to aress family")

# with open("Example.txt", mode="r+") as file:  #---------- first read it and then write it 
#     print(file.read())

#     file.write("This is file Handling examples.\n")

# File I/O example without exception handling

filename = "Example.txt"


with open(filename, "w") as file:
    file.write("Hello! Welcome to Python File I/O.\n")
    file.write("This is the first line.\n")


with open(filename, "a") as file:
    file.write("This line is appended at the end.\n")


with open(filename, "r") as file:
    content = file.read()

print("--- File Content ---")
print(content)




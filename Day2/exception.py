
try:
    a = int(input("Enter the number: "))
    print("\nMultiplication table of {a} is: ")
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except Exception as e:
    print("Invalid input")

print("Program executes successfully.......")


# File I/O Example in Python

# filename = "example.txt"


# try:
#     with open(filename, "w") as file:
#         file.write("Hello! Welcome to Python File I/O.\n")
#         file.write("This is the first line.\n")
#     print("Data written successfully!")
# except Exception as e:
#     print("Error writing to file:", e)


# try:
#     with open(filename, "a") as file:
#         file.write("This line is appended at the end.\n")
#     print("Data appended successfully!")
# except Exception as e:
#     print("Error appending to file:", e)

# try:
#     with open(filename, "r") as file:
#         content = file.read()  
#     print("\n--- File Content ---")
#     print(content)
# except FileNotFoundError:
#     print("File not found!")
# except Exception as e:
#     print("Error reading file:", e)


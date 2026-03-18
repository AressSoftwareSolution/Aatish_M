# import csv

# # CSV file to store inventory
# filename = "inventory.csv"

# # Function to add item
# def add_item(name, quantity, price):
#     with open(filename, mode="a", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow([name, quantity, price])
#     print(f"Item '{name}' added successfully!")

# # Function to view inventory
# def view_inventory():
#     print("\n--- Inventory ---")
#     try:
#         with open(filename, mode="r") as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 print(f"Name: {row[0]}, Quantity: {row[1]}, Price: {row[2]}")
#     except FileNotFoundError:
#         print("No items in inventory yet.")

# # Function to update quantity
# def update_item(name):
#     try:
#         rows = []
#         updated = False

#         # Read all rows from CSV
#         with open(filename, mode="r") as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 if row[0] == name:
#                     print(f"Current Quantity: {row[1]}, Current Price: {row[2]}")
#                     new_quantity = input("Enter new quantity (leave blank to keep same): ")
#                     new_price = input("Enter new price (leave blank to keep same): ")

#                     # Update quantity if entered
#                     if new_quantity != "":
#                         row[1] = str(new_quantity)

#                     # Update price if entered
#                     if new_price != "":
#                         row[2] = str(new_price)

#                     updated = True
#                 rows.append(row)

#         # Write all rows back to CSV
#         if updated:
#             with open(filename, mode="w", newline="") as file:
#                 writer = csv.writer(file)
#                 writer.writerows(rows)
#             print(f"Item '{name}' updated successfully!")
#         else:
#             print(f"Item '{name}' not found in inventory.")

#     except FileNotFoundError:
#         print("No items in inventory yet.")

# # Main loop
# while True:
#     print("\n1. Add Item")
#     print("2. View Inventory")
#     print("3. Update Quantity")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         name = input("Enter item name: ")
#         quantity = int(input("Enter quantity: "))
#         price = float(input("Enter price: "))
#         add_item(name, quantity, price)

#     elif choice == "2":
#         view_inventory()

#     elif choice == "3":
#         name = input("Enter item name to update: ")
#         new_quantity = int(input("Enter new quantity: "))
#         update_quantity(name, new_quantity)

#     elif choice == "4":
#         print("Exiting...")
#         break

#     else:
#         print("Invalid choice, try again!")
import csv

filename = "inventory.csv"

def add_item(name, quantity, price):
     with open(filename, mode="a", newline="") as file:
         writer = csv.writer(file)
         writer.writerow([name, quantity, price])
     print(f"Item '{name}' added successfully!")

def display_inventory():
    print("\n------ Inventory ------")
    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                print(f"Name: {row[0]}, Quantity: {row[1]}, Price: {row[2]}")
                found = True
            if not found:
                print("Inventory is empty.")
    except FileNotFoundError:
        print("No items in the inventory.")


def update_item(name):
    try:
        rows = []
        updated = False

        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == name.lower():
                    print(f"Current Quantity: {row[1]}, Current Price: {row[2]}")
                    new_quantity = input("Enter new quantity (leave blank to keep same): ")
                    new_price = input("Enter new price (leave blank to keep same): ")

                    if new_quantity != "":
                        row[1] = new_quantity
                    if new_price != "":
                        row[2] = new_price

                    updated = True

                rows.append(row)

        if updated:
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print(f"Item '{name}' updated successfully!")
        else:
            print(f"Item '{name}' not found in inventory.")

    except FileNotFoundError:
        print("No items in the inventory.")


while True:
    print("\n===== Inventory Menu =====")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter item name: ")
        quantity = input("Enter quantity: ")
        price = input("Enter price: ")
        add_item(name, quantity, price)

    elif choice == "2":
        display_inventory()

    elif choice == "3":
        name = input("Enter item name to update: ")
        update_item(name)

    
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")

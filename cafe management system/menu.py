#Define the menu of Tasty Tales restaurant

menu = {
    'pizza' :40,
    'pasta' :50,
    'burger':60,
    'salad' :70,
    'coffee':80,
}

print("WELCOME TO Tasty Tales RESTAURANT")
print("pizza  :Rs40\npasta  :Rs50\nburger :Rs60\nsalad  :Rs60\ncoffee :Rs80 ")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order ")

else:
    print(f"Ordered item {item_1} is not available yet! ")

another_order_1= input("Do you want to add another item? (yes/no)")
if another_order_1== "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to you order")
    else:
        print(f"Ordered item {item_2} is not available! ")

another_order_2 = input("Do you want to add another item? (yes/no)")
if another_order_2 == "yes":
    item_3 = input("Enter the name of third item = ")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"Item {item_3} has been added to you order")
    else:
        print(f"Ordered item {item_3} is not available! ")

print(f"The total amount of item to pay is {order_total}")


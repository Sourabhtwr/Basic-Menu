#Menu
Menu = {
    'Pasta' : 50, 'Coffee' : 20
}
print ("Welcome to Unique Dhaba ")
print ("Pasta: 50\nCoffee: 20\n")

order_total = 0

item_1 = input("Enter your order ")
if item_1 in Menu:
    order_total += Menu[item_1]
    print(f"Your order {item_1}is added ") 
else:
    print(f"this item {item_1} is not avalible ")

another_order = input("Do you want any thing else (Yes or NO) ")
if another_order== ("Yes"):
    item_2 = input("Enter Your item_2")
    if item_2 in Menu:
        order_total += Menu[item_2]
        print (f"Item is added to your Order ")
    else:
        print (f"This item is not avalable ")

print(f"The total amount is to pay =  {order_total} ")

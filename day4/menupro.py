# Menu
# Only Use Nested If Statements
# cafe/restorant
products = ["1.chai", "2.Coffee", "3.Burger", "4.exit"]

chai_types = ["Ginger Chai","Green Chai","Normal Chai"]

for product in products:
    print(product)

selected_product = int(input("Select product:"))

if selected_product == 1:
    print("chai")
    for chai in chai_types:
        print(chai)
    selected_chai = int(input("Select chai:"))
    if selected_chai == 1:
        print("Ginger Chai you select")
    elif selected_chai == 2:
        print("Green Chai you select")
    elif selected_product == 3:
        print("Normal Chai you select")
    else:
        print("No motre choice in Chai...!!!")

elif selected_product == 2:
    print("Coffee:-")
    for Coffee in Coffee_types:
        print(Coffe:)
    selected_Coffe= int(input("Select Coffe:"))
    if selected_Coffe == 1:
        print("Espresso Coffee you select")
    elif selected_Coffee == 2:
        print("Cappuccino Coffee you select")
    elif selected_Coffee == 3:
        print("Cold Brew you select")   
    else:
    print("No more choice in Coffee")

elif selected_product == 3:
    print("Burger:-")
    for Burger in Burger_types:
        print(Burger)
    selected_Burger= int(input("Select Burger:"))
    if selected_Burger == 1:
        print(Classic Veg Burger you select)
    elif selected_Burger == 2:
        print(Spicy barbeque Burger you select)
    elif selected_Burger == 3:
        print(Double Tikki Burger you select)
else:
    print("no more choice in Burger")

elif select_pkg == 4:
        print("Exiting the menu. Thank you!")
        break
    
    else:
        print("Invalid Package Selection! Please Select only (1-3) or 4 to Exit.")
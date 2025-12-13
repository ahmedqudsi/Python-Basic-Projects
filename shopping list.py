# We need a make a shopping cart that consists of items,price and quantity.

Item = input("Enter the item you want to buy: ")
Price = float(input(f"Enter the price of {Item}:$"))
Quantity = int(input(f"Enter the quantity of {Item}:"))
Total_cost = Price * Quantity
print(f"The total cost of {Quantity} {Item}'s is: ${Total_cost}")

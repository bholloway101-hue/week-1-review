def calc_item_total(price, quantity):
    return price * quantity

def calc_cart_total(total1, total2):
    return total1 + total2

Item1 = input("Item 1: ")
price1 = float(input("Item 1 price ($):"))
qty1 = int(input("Item 1 quantity:"))

Item2 = input("Item 2: ")
price2 = float(input("Item 2 price ($): "))
qty2 = int(input("Item 2 quantity: "))

total1 = calc_item_total(price1, qty1)
total2 = calc_item_total(price2, qty2)
cart_total = calc_cart_total(total1, total2)

print("--------------------------")
print(f"Item: {Item1}\nPrice: {price1:.2f} $ Quantity: {qty1}")
print(f"Total price: {total1:.2f} $")
print("--------------------------")
print(f"Item: {Item2}\nPrice: {price2:.2f} $ Quantity: {qty2}")
print(f"Total price: {total2:.2f} $")
print("##############################")
print(f"Total cart price: {cart_total:.2f} $")

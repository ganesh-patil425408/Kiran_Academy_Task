
def calculateElectronicsGST(Mobile, Laptop):
    return (Mobile + Laptop) * 1.18


def calculateFashionGST(T_shirt, Shirt):
    return (T_shirt + Shirt) * 1.13


def calculateBeautyProductsGST(Facewash):
    return Facewash * 1.07


def totalBill(Mobile, Laptop, T_shirt, Shirt, Facewash):
    electronics = calculateElectronicsGST(Mobile, Laptop)
    fashion = calculateFashionGST(T_shirt, Shirt)
    food = calculateBeautyProductsGST(Facewash)

    return electronics + fashion + food


def calculateDiscountedBill(Mobile, Laptop, T_shirt, Shirt, Facewash):
    total = totalBill(Mobile, Laptop, T_shirt, Shirt, Facewash)
    discount = total * 0.20
    return total - discount


Mobile = 20000
Laptop = 50000
T_shirt = 500
Shirt = 600
Facewash = 100

total = totalBill(Mobile, Laptop, T_shirt, Shirt, Facewash)
discount = total * 0.20
final_amount = calculateDiscountedBill(
    Mobile, Laptop, T_shirt, Shirt, Facewash
)

print(f"Total after GST = {total:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Final payable amount = {final_amount:.2f}")

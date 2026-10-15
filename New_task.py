
# 1. Function Definitions

def calculateLightBill(light_bill):
    return light_bill


def calculateWaterBill(water_bill):
    return water_bill


def calculateMilkBill(milk_bill):
    return milk_bill


def calculateGroceryBill(grocery_bill):
    return grocery_bill


def calculateVegetableBill(vegetable_bill):
    return vegetable_bill


def calculateInternetBill(internet_bill):
    return internet_bill


def calculateGasBill(gas_bill):
    return gas_bill


def calculateTransportExpense(transport_expense):
    return transport_expense


def calculateMedicalBill(medical_bill):
    return medical_bill


def totalMonthlyExpense(
    light_bill,
    water_bill,
    milk_bill,
    grocery_bill,
    vegetable_bill,
    internet_bill,
    gas_bill,
    transport_expense,
    medical_bill
):
    total = (
        calculateLightBill(light_bill)
        + calculateWaterBill(water_bill)
        + calculateMilkBill(milk_bill)
        + calculateGroceryBill(grocery_bill)
        + calculateVegetableBill(vegetable_bill)
        + calculateInternetBill(internet_bill)
        + calculateGasBill(gas_bill)
        + calculateTransportExpense(transport_expense)
        + calculateMedicalBill(medical_bill)
    )

    return total


def calculateMonthlySavings(
    monthly_income,
    light_bill,
    water_bill,
    milk_bill,
    grocery_bill,
    vegetable_bill,
    internet_bill,
    gas_bill,
    transport_expense,
    medical_bill
):
    total_expenses = totalMonthlyExpense(
        light_bill,
        water_bill,
        milk_bill,
        grocery_bill,
        vegetable_bill,
        internet_bill,
        gas_bill,
        transport_expense,
        medical_bill
    )

    return monthly_income - total_expenses


# 2. Variable Declarations

light_bill = 1200
water_bill = 300
milk_bill = 1500
grocery_bill = 4000
vegetable_bill = 1200
internet_bill = 700
gas_bill = 1000
transport_expense = 1500
medical_bill = 800

monthly_income = 20000


# 3. Function Calls

total_expenses = totalMonthlyExpense(
    light_bill,
    water_bill,
    milk_bill,
    grocery_bill,
    vegetable_bill,
    internet_bill,
    gas_bill,
    transport_expense,
    medical_bill
)

monthly_savings = calculateMonthlySavings(
    monthly_income,
    light_bill,
    water_bill,
    milk_bill,
    grocery_bill,
    vegetable_bill,
    internet_bill,
    gas_bill,
    transport_expense,
    medical_bill
)


# 4. Display Output

print("  MONTHLY HOME BUDGET  ")

print("Monthly Home Budget")

print(f"Light Bill: Rs. {light_bill}")
print(f"Water Bill: Rs. {water_bill}")
print(f"Milk Bill: Rs. {milk_bill}")
print(f"Grocery Bill: Rs. {grocery_bill}")
print(f"Vegetable Bill: Rs. {vegetable_bill}")
print(f"Internet Bill: Rs. {internet_bill}")
print(f"Gas Bill: Rs. {gas_bill}")
print(f"Transport Expense: Rs. {transport_expense}")
print(f"Medical Bill: Rs. {medical_bill}")

print("--------------------")

print(f"Monthly Income: Rs. {monthly_income}")
print(f"Total Expenses: Rs. {total_expenses}")
print(f"Monthly Savings: Rs. {monthly_savings}")



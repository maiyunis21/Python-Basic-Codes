meal_cost = float(input("Enter the cost of the meal: "))
tax_rate = 0.12
tip_rate = 0.18
mealtax = meal_cost * tax_rate
tip = meal_cost * tip_rate
total_cost = meal_cost + mealtax + tip
print(f"The tax amount is {mealtax:.2f}")
print(f"The tip amount is {tip:.2f}")
print(f"The total grand total of the meal is {total_cost:.2f}")
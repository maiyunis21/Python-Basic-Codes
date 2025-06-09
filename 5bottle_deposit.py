a_liter_or_less = 0.10
more_than_a_liter = 0.25

small_bottles = int(input("Enter the number of small bottles (1 liter or less): "))
large_bottles = int(input("Enter the number of large bottles (more than 1 liter): "))

refund = (small_bottles * a_liter_or_less) + (large_bottles * more_than_a_liter)
print(f"The total refund is: ${refund:.2f}")

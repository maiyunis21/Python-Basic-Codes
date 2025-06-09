a_liter_or_less = 0.10
more_than_a_liter = 0.25

def calculate_deposit(bottle_size):
    num_bottles = (input("Enter the size of the bottle:"))
    
    if bottle_size <= 1:
        return a_liter_or_less
    else:
        return more_than_a_liter
    

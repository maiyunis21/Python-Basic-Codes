#Create a program that reads the length and width of a farmer’s field from the user in
#feet. Display the area of the field in acres.

width = input("Enter the width of the field in feet: ")
length = input("Enter the length of the field in feet: ")
# Calculate the area of the field in square feet
area = float(width) * float(length)
# Convert the area to acres
acre_to_sqft = 1 / 43500
area_acres = area * acre_to_sqft
print("%.3f" %area_acres, "square feet")


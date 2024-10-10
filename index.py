#Pizza Size
sizeP = input("Enter the pizza size:")
addTopping = input("Do you want to add toppings? Y or N: ")
cheese = input("Do you want to add extra chesse? Y or N:")
bill = 0
if (sizeP == 'S'):
  bill = bill + 150
elif (sizeP == 'M'):
  bill += 200
else:
  bill += 250

print(f"Your pizza price: {bill}")

if (addTopping == 'Y'):
  bill += 20
else:
  bill += 0
print(f"Adding extra topings: {bill}")

if (cheese == 'Y'):
  bill += 20
else:
  bill += 0
print(f"Adding extra cheess is: {bill}")

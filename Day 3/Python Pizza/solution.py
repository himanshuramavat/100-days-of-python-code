print("Welcome to Python Pizza Deliveries!")

# Define price mappings for better readability and maintainability
size_prices = {"S": 15, "M": 20, "L": 25}
pepperoni_prices = {"S": 2, "M": 3, "L": 3}

# Get user inputs
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Initialize bill
bill = 0

# Calculate base price
if size in size_prices:
    bill += size_prices[size]
else:
    print("You have chosen an invalid size.")

# Add pepperoni cost if applicable
if pepperoni == "Y" and size in pepperoni_prices:
    bill += pepperoni_prices[size]

# Add extra cheese cost if applicable
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
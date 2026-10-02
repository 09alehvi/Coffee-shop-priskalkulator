#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")

price = 0
#Liste med de forskellige typene kaffe
coffee_types = ["Espresso", "Americano", "Latte", "Cappuccino", "Macchiato", "Mocha", "Flat White"]               
#Liste med prisene
coffee_prices = {    
    "Espresso": 2.50,
    "Americano": 3.00,
    "Latte": 2.50,
    "Cappuccino": 3.00,
    "Macchiato": 2.50,
    "Mocha": 3.50,
    "Flat White": 2.50
}

coffee = input("What type of coffee would you like?").title()

#Dette gjør at den fortsetter å spørre helt til man skriver en gyldig kaffe
while coffee not in coffee_types:
    print("That is not a valid coffee.")
    coffee = input("What type of coffee would you like?").title()

price = price + coffee_prices[coffee]

#Forksjellige størrelser og prisene
sizes = ["Medium", "Large", "XL"]

size_prices = {
    "Medium": 0,
    "Large": 1,
    "XL": 1.50
}

size = input("What size would you like?")

while size not in sizes:
    print("That is not a valid size.")
    size = input("What size would you like?")
price = price + size_prices[size]

takeaway_options = ["Yes", "No"]
takeaway = input("Would you like to takeaway?").title()

#Dette passer på at man sier Ja eller Nei
while takeaway not in takeaway_options:
    print("Please answer Yes or No.")
    takeaway = input("Would you like to takeaway?").title()

if takeaway == "Yes":
    price = price + 1

#Complete the code here...
print("----------------------------")
print("Total Cost: £" + str(price))



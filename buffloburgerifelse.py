print("Welcome to Buffalo Burger \n")

name = input("What's your name?\n")
age = input("What's your age?\n")
location = input("What's your address?\n")

print("Welcome " + name + ", Thanks for using our app \n") 

menu = ("\nold School, Grungey, The Muscular, The Original \n")

print(name + ", what would you like from our menu today? Here is what we are serving: \n" + menu)

order = input()

price = 8

if order == "The Muscular":
  price = 12
elif order == "old school":
   price = 3
elif order == "Grungey":
   price = 6
elif order == "The Original":
   price = 3
else :
   print("Sorry we dont have that")
   price = 0

quantity = input("How many burgers would you like?\n")

total = price * int(quantity)

print("Thank you, your total is: $ " + str(total))

pay = input("How would you like to pay, Mr/Ms " + name + "? Cash or Visa \n")

if pay.lower() == "visa":
    visa_number = input("Please type your visa number: \n")
    print("Your receipt: \nName: " + name + "\nAge: " + age + "\nOrder: " + order + "\nPrice: $" + str(price) + "\nQuantity: " + quantity + "\nPayment Method: Visa (**** **** **** " + visa_number[-4:] + ")\nTotal: $" + str(total))
else:
    print("Okay, cool. Your total is $" + str(total))
    print("Your receipt: \nName: " + name + "\nAge: " + age + "\nOrder: " + order + "\nPrice: $" + str(price) + "\nQuantity: " + quantity + "\nPayment Method: Cash\nTotal: $" + str(total))

print("Thanks for ordering from Buffalo Burger. Your order will be delivered in 25 minutes. Have a great day! :)")


print("Welcome to the GC Fruit Market!")
name = input("What is your name?")
total = 0
apples = 0
oranges = 0
grapes = 0
buyAnother = "y"

while buyAnother == "y":
    purchase = int(input("Welcome " + name + ". Which fruit would you like to buy?\n1. Apple $2\n2. Grape $1\n3. Orange $3"))
    if purchase == 1:
        total += 2
        print("You bought an apple at $2")
        apples += 1

    elif purchase == 2:
        total += 1
        print("You bought a grape at $1")
        grapes += 1
    else:
        total += 3
        print("You bought an orange at $3")
        oranges += 1

    buyAnother = input("Would you like to buy another piece of fruit? y/n")

print("Reciept for " + name)
print(str(apples) + " Apple(s) at $2 apiece\n" + str(grapes) + " Grape(s) at $1 apiece\n" + str(oranges) + " Orange(s) at $3 apiece")
print("Sub Total: $" + str(total))
print("Tax: $" + str(total*0.05))
print("Total: $" + str(total*1.05))

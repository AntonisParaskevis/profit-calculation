while True:
    try:
        # Prompt the user to enter the income
        income = float(input("Enter the income\n"))
        
        # If the user has entered a negative number, prompt them to enter a valid input
        if income < 0:
            print("Invalid entry, please enter zero, or a number greater than zero.")
            continue
        break
    except ValueError:
        # If the user has entered a non-numerical input, prompt them to enter a valid input
        print("Invalid entry, please enter zero, or a number greater than zero.")

# Same for the expenses
while True:
    try:
        expenses = float(input("Enter the expenses\n"))
        
        if expenses < 0:
            print("Invalid entry, please enter zero, or a number greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid entry, please enter zero, or a number greater than zero.")

# Calculate the net income
net_income = income - expenses

# Display the profit or loss, depending on the value of net_income. If income = expenses, display an approppriate message
if net_income > 0:
    print("Profit: $" + str(net_income) + ".")
elif net_income < 0:
    print("Loss: $" + str(abs(net_income)) + ".")
else:
    print("Neither profit nor loss.")

# In the end, prompt the user to press Enter, in order to exit the program
input("Press Enter to exit the program")
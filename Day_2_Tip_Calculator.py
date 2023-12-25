#1. Create the welcome note
#2. Ask for the total bill
#2. Choose the percentage tip you
#3. How many people to split bill
#4. Display how much each person will pay

print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $")) 
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people split the bill? "))
bill_with_tip = tip / 100 * bill + bill
payment = bill_with_tip / people
print(f"Total bill with tip is ${bill_with_tip}")
print(f"Each person should pays $%.2f" % round(payment, 2))
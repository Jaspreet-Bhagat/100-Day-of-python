print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10,12, or 15?"))
split = int(input("How many people to split the bill? "))
result = tip/100*bill + bill
bill_per_person = result /split
final_amount = "{:.2f}".format(bill_per_person)
print(f"each person should pay:{final_amount}")

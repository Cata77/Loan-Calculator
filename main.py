import math

loan_principal = int(input("Enter the loan principal:\n> "))

option = input("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
> """)

if option == "m":
    monthly_payment = int(input("Enter the monthly payment:\n> "))
    months_to_repay = round(loan_principal / monthly_payment)
    if months_to_repay == 1:
        print("\nIt will take 1 month to repay the loan")
    else:
        print("\nIt will take {} months to repay the loan".format(months_to_repay))
else:
    num_of_months = int(input("Enter the number of months:\n> "))
    payment = math.ceil(loan_principal / num_of_months)
    last_payment = loan_principal - (num_of_months - 1) * payment
    if last_payment != payment:
        print("\nYour monthly payment = {} and the last payment = {}".format(payment, last_payment))
    else:
        print("\nYour monthly payment = {}".format(payment))

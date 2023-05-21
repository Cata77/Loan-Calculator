import math

option = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> """)

if option == "n":
    loan_principal = int(input("Enter the loan principal:\n> "))
    monthly_payment = int(input("Enter the monthly payment:\n> "))
    loan_interest = float(input("Enter the monthly payment:\n> "))
    i = (loan_interest * 100) / (12 * 100 * 100)
    number_of_months = math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i))
    years = number_of_months // 12
    months = number_of_months % 12
    if years != 0 and months != 0:
        print("It will take {} years and {} months to repay this loan!".format(years, months))
    elif years == 0 and months != 0:
        print("It will take {} months to repay this loan!".format(months))
    else:
        print("It will take {} years to repay this loan!".format(years))
elif option == "a":
    loan_principal = int(input("Enter the loan principal:\n> "))
    num_of_periods = int(input("Enter the number of periods:\n> "))
    loan_interest = float(input("Enter the loan interest:\n> "))
    i = (loan_interest * 100) / (12 * 100 * 100)
    annuity_payment = loan_principal * ((i * math.pow(1 + i, num_of_periods)) / (math.pow(1 + i, num_of_periods) - 1))
    print("Your monthly payment = {}!".format(math.ceil(annuity_payment)))
else:
    annuity_payment = float(input("Enter the annuity payment:\n> "))
    num_of_periods = int(input("Enter the number of periods:\n> "))
    loan_interest = float(input("Enter the loan interest:\n> "))
    i = (loan_interest * 100) / (12 * 100 * 100)
    loan_principal = annuity_payment / ((i * math.pow(1 + i, num_of_periods)) / (math.pow(1 + i, num_of_periods) - 1))
    print("Your loan principal = {}!".format(round(loan_principal)))

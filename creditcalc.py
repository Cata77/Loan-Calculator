import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=["annuity", "diff"])
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()


def check_for_negative_values(arguments):
    for arg in vars(arguments):
        arg_value = getattr(args, arg)
        if type(arg_value) == int and arg_value < 0:
            return True
    return False


def calculate_diff_payment(m):
    return math.ceil(args.principal / args.periods + i * (args.principal - (args.principal * (m - 1)) / args.periods))


if len(vars(args)) < 5:
    print("Incorrect parameters")
elif args.type != "annuity" and args.type != "diff":
    print("Incorrect parameters")
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
elif check_for_negative_values(args):
    print("Incorrect parameters")
else:
    i = float((args.interest * 100) / (12 * 100 * 100))
    if args.payment is None:
        sum_diff_payments = 0
        if args.type == "diff":
            for idx in range(1, args.periods + 1):
                diff_payment = calculate_diff_payment(idx)
                sum_diff_payments += diff_payment
                print("Month {}: payment is {}".format(idx, diff_payment))
            print("\nOverpayment = {}".format(sum_diff_payments - args.principal))
        else:
            annuity_payment = math.ceil(
                args.principal * ((i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1)))
            print("Your monthly payment = {}!".format(annuity_payment))
            print("Overpayment = {}".format(math.ceil(annuity_payment * args.periods - args.principal)))
    elif args.principal is None:
        loan_principal = math.floor(
            args.payment / ((i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1)))
        print("Your loan principal = {}!".format(loan_principal))
        print("Overpayment = {}".format(math.ceil(args.payment * args.periods - loan_principal)))
    elif args.periods is None:
        number_of_months = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
        years = number_of_months // 12
        months = number_of_months % 12
        if years != 0 and months != 0:
            print("It will take {} years and {} months to repay this loan!".format(years, months))
        elif years == 0 and months != 0:
            print("It will take {} months to repay this loan!".format(months))
        else:
            print("It will take {} years to repay this loan!".format(years))
        print("Overpayment = {}".format(math.ceil(args.payment * number_of_months - args.principal)))

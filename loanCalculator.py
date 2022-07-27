import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()
type_arg = args.type

if type_arg == "diff":
    if args.payment == None:
        principal = float(args.principal)
        periods = int(args.periods)
        interest = float(args.interest)
        i = (interest * 0.01)/12
        m = 1
        overpayment = 0
        while m <= periods:
            D = (principal/periods) + i * (principal - (principal * (m - 1) / periods))
            print("Month " + str(m) + ": payment is " + str(math.ceil(D)))
            overpayment = math.ceil(D) - (principal/periods) + overpayment
            m += 1
        print("Overpayment: " + str(int(overpayment)))
    else:
        print("Incorrect parameters")
elif type_arg == "annuity":
    if args.periods == None and args.principal != None and args.payment != None and args.interest != None:
        principal = float(args.principal)
        payment = int(args.payment)
        interest = float(args.interest)
        i = (interest * 0.01)/12
        n = math.ceil(math.log((payment / (payment - i * principal)), (1 + i)))
        overpayment = payment * n - principal
        if n % 12 != 0 and n > 12:
            print('It will take ' + str(math.floor(n / 12)) + ' years and ' + str(math.ceil(n % 12)) + ' months to repay this loan!')
        elif n < 12 and n != 1:
            print('It will take ' + str(n % 12) + ' months to repay this loan!')
        elif n == 1:
            print('It will take 1 month to repay this loan!')
        else:
            print('It will take ' + str(math.floor(n / 12)) + ' years to repay this loan!')
        print('Overpayment = ' + str(math.ceil(overpayment)))
    elif args.principal != None and args.periods != None and args.payment == None and args.interest != None:
        principal = float(args.principal)
        periods = int(args.periods)
        interest = float(args.interest)
        i = (interest * 0.01)/12
        A = principal * (i * math.pow((1 + i), periods))/(math.pow((1 + i), periods) - 1)
        overpayment = math.ceil(A) * periods - principal
        print('Your annuity payment = ' + str(math.ceil(A)) + '!')
        print('Overpayment = ' + str(math.ceil(overpayment)))
    elif args.periods != None and args.payment != None and args.interest != None and args.principal == None:
        payment = float(args.payment)
        periods = int(args.periods)
        interest = float(args.interest)
        i = (interest * 0.01)/12
        P = payment / ((i * math.pow((1 + i), periods)) / (math.pow((1 + i), periods) - 1))
        overpayment = (payment * periods) - P
        print('Your loan principal = ' + str(int(P)) + '!')
        print('Overpayment = ' + str(math.ceil(overpayment)))
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')


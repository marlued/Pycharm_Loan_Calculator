from math import ceil


def payment(principal, months):
    return ceil(principal / months)


def duration(principal, pay_per_month):
    return ceil(principal / pay_per_month)


def last_payment(principal, rate, periods):
    return principal - (periods - 1) * rate


def overpay(principal, payments, periods):
    return payments * periods > principal


loan_principal = int(input('Enter the loan principal: \n').strip())

choice = input('What do you want to calculate?\n\
type "m" - for number of monthly payments,\n\
type "p" - for the monthly payment:\n')

if choice == 'm':
    print('Enter the monthly payment: ')
    monthly_payment = int(input().strip())
    string = f'It will take {duration(loan_principal, monthly_payment)} months to repay the loan' \
        if duration(loan_principal, monthly_payment) > 1 else \
        f'It will take {duration(loan_principal, monthly_payment)} month to repay the loan'
    print(string)


elif choice == 'p':

    print('Enter the number of months: ')
    number_of_month = int(input().strip())
    monthly_pay = payment(loan_principal, number_of_month)

    if overpay(loan_principal, payment(loan_principal, number_of_month), number_of_month):
        print(f'Your monthly payment = {payment(loan_principal, number_of_month)}\
        and the last payment = {last_payment(loan_principal, monthly_pay, number_of_month)}')
    else:
        print(f'Your monthly payment = {payment(loan_principal, number_of_month)}')

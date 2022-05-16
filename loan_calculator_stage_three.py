from math import log, ceil, floor


def monthly_payment(loan, interest, periods):
    return floor(loan * (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))


def number_of_monthly_payments(loan, payment, interest):
    return ceil(log((payment / (payment - interest * loan)), 1 + interest))


def loan_principal():
    pass


def nominal_interest_rate(interest):
    return interest / (12 * 100)


starting_string = """
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
"""

print(starting_string)

user_input = input().strip()

if user_input == "a":
    loan_principal = int(input('Enter the loan principal: '))
    number_of_periods = int(input('Enter the number of periods: '))
    loan_interest = int(input('Enter the loan interest: '))

    i = nominal_interest_rate(loan_interest)
    pay_per_month = monthly_payment(loan_principal, i, number_of_periods)
    print(f'Your monthly payment = {pay_per_month}!')

if user_input == "p":
    annuity_payment = int(input('Enter the annuity payment:'))
    number_of_periods = int(input('Enter the number of periods: '))
    loan_interest = int(input('Enter the loan interest: '))

if user_input == "n":
    loan_principal = int(input('Enter the loan principal: '))
    monthly_payment = int(input('Enter the monthly payment: '))
    loan_interest = int(input('Enter the loan interest: '))

    i = nominal_interest_rate(loan_interest)

    calculated_period = number_of_monthly_payments(loan_principal, monthly_payment, i)

    years = (calculated_period // 12)
    months = (calculated_period % 12)

    print(f'It will take {years} years and {months} months to repay this loan!')

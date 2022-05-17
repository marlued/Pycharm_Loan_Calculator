from math import log, ceil


def monthly_payment(credit, interest, periods):
    return ceil(credit * (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))


def number_of_monthly_payments(credit, payment, interest):
    return ceil(log((payment / (payment - interest * credit)), 1 + interest))


def loan_principal(payment, i, periods):
    return payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))


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
    loan_principal = float(input('Enter the loan principal: '))
    number_of_periods = int(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest: '))

    i = nominal_interest_rate(loan_interest)
    pay_per_month = monthly_payment(loan_principal, i, number_of_periods)
    print(f'Your monthly payment = {pay_per_month}!')

if user_input == "p":
    annuity_payment = float(input('Enter the annuity payment: '))
    number_of_periods = int(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest: '))

    i = nominal_interest_rate(loan_interest)
    loan = round(loan_principal(annuity_payment, i, number_of_periods))
    print(f'Your loan principal = {loan}!')

if user_input == "n":
    loan_principal = float(input('Enter the loan principal: '))
    monthly_payment = float(input('Enter the monthly payment: '))
    loan_interest = float(input('Enter the loan interest: '))

    i = nominal_interest_rate(loan_interest)

    calculated_period = number_of_monthly_payments(loan_principal, monthly_payment, i)

    years = (calculated_period // 12)
    months = (calculated_period % 12)

    print(f'It will take {years} years and {months} months to repay this loan!')

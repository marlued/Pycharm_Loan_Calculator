def monthly_payment():
    pass

def number_of_monthly_payments():
    pass

def loan_principal():
    pass


starting_string = """
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
"""

user_input = input().strip()

if user_input == "a":
    loan_principal = int(input('Enter the loan principal: '))
    number_of_periods = int(input('Enter the number of periods: '))
    loan_interest = int('Enter the loan interest: ')

if user_input == "p":
    annuity_payment = int(input('Enter the annuity payment:'))
    number_of_periods = int(input('Enter the number of periods: '))
    loan_interest = int('Enter the loan interest: ')

if user_input == "n":
    loan_principal = int(input('Enter the loan principal: '))
    monthly_payment = int(input('Enter the monthly payment: '))
    loan_interest = int('Enter the loan interest: ')

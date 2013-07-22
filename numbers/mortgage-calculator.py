__author__ = 'JoshMa'

import locale

locale.setlocale(locale.LC_ALL, '')

amount = float(locale.atof(
    input('What is the loan amount for the mortgage? ')))
rate = float(input('What is the interest rate of the mortgage? ')) * .01
terms = int(input('How many years will the mortgage last? ')) * 12

payment = (amount + (amount * rate)) / terms
print('The monthly payments for this mortgage are', locale.currency(payment))
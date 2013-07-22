__author__ = 'JoshMa'

from decimal import *
import locale

locale.setlocale(locale.LC_ALL, '')

cost = Decimal(input('What is the cost of the your purchase? '))
paid = Decimal(input('How much money are you paying with? '))

if cost > paid:
    ValueError('You must pay at least as much as the cost.')

coins = {'quarter':0, 'dime':0, 'nickel':0, 'penny':0}
quarter, dime, nickel, penny = (Decimal(.25), Decimal(.10),
                                Decimal(.05), Decimal(.01))

if cost == paid:
    pass
else:
    change = paid - cost
    coins['quarter'] = int(change / quarter)
    change -= coins['quarter'] * quarter
    coins['dime'] = int(change / dime)
    change -= coins['dime'] * dime
    coins['nickel'] = int(change / nickel)
    change -= coins['nickel'] * nickel
    coins['penny'] = int(change / penny)
    change -= coins['penny'] * penny

print('Your change due is', locale.currency(paid - cost))
print('That will be paid in')
print(coins)
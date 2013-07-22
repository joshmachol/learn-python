__author__ = 'JoshMa'

import locale

locale.setlocale(locale.LC_ALL, '')

price = float(input('What is the cost/sq. ft. of the tile? '))
width = float(input('What is the width of the floor? '))
height = float(input('What is the height of the floor? '))

total_cost = price * width * height

print('The total cost of tile for this floor plan is', locale.currency(total_cost))
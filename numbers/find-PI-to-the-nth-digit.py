__author__ = 'JoshMa'

from math import atan

digits = input('Enter number of digits to round PI to: ')

# calculate pi using Machin-like Formula
pi = 4 * (4 * atan(1.0/5.0) - atan(1.0/239.0))
print(('{0:.%df}' % min(30, int(digits))).format(pi))
__author__ = 'JoshMa'

n = int(input('How many numbers do you need? '))
series = [1]

while len(series) < n:
    if len(series) == 1:
        series.append(1)
    else:
        series.append(series[-1] + series[-2])

print(series)
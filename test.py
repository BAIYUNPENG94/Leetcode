import itertools

x = "11122211"

for digit, group in itertools.groupby(x):
    print(digit)
    print(list(group))
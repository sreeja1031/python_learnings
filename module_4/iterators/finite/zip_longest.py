from itertools import zip_longest
for item in zip_longest('ABCD', 'xy', fillvalue='BLANK'):
    print (item)

#('A', 'x')
#('B', 'y')
#('C', 'BLANK')
#('D', 'BLANK')
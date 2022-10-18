from itertools import product
arrays = [[-1], [-3], (-5,5)]
cp = list(product(*arrays))
print (cp)
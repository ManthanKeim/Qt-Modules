from functools import reduce

li=[32 ,21 ,321 ,3143, 56 ,676 ,876]

s= reduce(lambda  x , y : x.union({y}),li , set())

print(s)
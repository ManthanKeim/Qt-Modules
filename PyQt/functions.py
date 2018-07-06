def sqaure(x):
    return x**2

sq = lambda x : x**2


print(sq(32))
print(sqaure(32))

l = [1,2,3,4,55,3,3]

slist = list(map(sq,l))
blist = list(map(lambda x : x-1 ,l))

print(slist)
print(blist)

big = list(filter(lambda x:x>2 , l ))

print(big)

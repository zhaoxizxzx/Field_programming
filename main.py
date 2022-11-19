from small2big import *
from big2small import mybig2small
c = eval(input())


BIG = mysmall2big(c)
print(BIG)
c =BIG+"元整"
print(c)

l = c[:-2]
print(l)
t = mybig2small(BIG)
print(t)
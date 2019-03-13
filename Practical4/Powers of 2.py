#TRY1:failed
from random import randint

from math import floor

x = randint(1,8193)
m=x
print("x is",x)

y=str()
Exp=13
for i in range(0,13):
    #ought to be (0,14)
    n=floor(x/2**Exp)
    x=x%2**Exp
    Exp=Exp-1
#    print(x)
#    print("i=",i)
#    print("Exp=",Exp)
#    print("n=",n)
    y=y+"+"+str(n)+"*"+"2**"+str(Exp)
print(m,"is",y)


#TRY2 with the help of Yuxing
x=1556
y=str(x)+" is "
Exp=13
for i in range(0,14):
    if x/2**Exp>1:
        x=x-2**Exp
        y=y+"2**"+str(Exp)+"+"
    elif x/2**Exp==1:
        x=0
        # at first I forgot to add x=0
        y=y+"2**"+str(Exp)
    else:
        x=x
        Exp=Exp
    Exp=Exp-1
    
print(y)
    

         
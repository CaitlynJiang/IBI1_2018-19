# May 14th: dk why here's no author information 
from random import randint


x = randint(1,8193) # according to protocol ‘for simplicity, you can assume that x is no larger than 8192 = 2^13'
print("x is",x) # to show the value of x
# With the help of Yuxing
y=str(x)+" is " # initiate the output words
Exp=13 # to see if the number can be divided by 2^13, start from the biggest
for i in range(0,14): #loop
    if x/2**Exp>1: # if x > 2^Exp
        x=x-2**Exp #change x for later calculation
        y=y+"2**"+str(Exp)+"+"
    elif x/2**Exp==1: # if x = 2^Exp ----- no more add to y
        x=0
        # at first I forgot to add x=0
        y=y+"2**"+str(Exp)
    else: # because 2^0=1, every possible number is composed by 2^n add together, so there's no x < 2^Exp 
        x=x 
        Exp=Exp
    Exp=Exp-1 # loop down to 
    
print(y)
    

         
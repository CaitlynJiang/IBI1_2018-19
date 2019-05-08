# What does this piece of code do?
# Answer: This cose can be used to choose the prime numbers.

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
# define p as False so that p can loop till it become true.
while p==False:
# Set the loop
    p=True
# make p = True at the beginning of the loop so that it can end when p==True
    n = randint(1,100)
# draw a random number within(1,100)
    u = ceil(n**(0.5))
# extract the cube root and takes the ceiling of it
    for i in range(2,u+1):
        if n%i == 0:
# to define if n is a prime number
            p=False
# Stop/restart the loop

     
print(n)
<<<<<<< HEAD

            
=======
>>>>>>> master

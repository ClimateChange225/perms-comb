"""
Created on Sun Nov  6 01:26:29 2022

@author: Ahad Tariq
Should help you calculate permutations and combinations
Let me know if you face any issues, pretty basic code as I'm still very much a beginner.
If you don't have a program to help you compile this code just look up Online Python Compiler
Click anyone, copy this code and paste it there; you should be good to go!
Thanks and best of luck!
"""

import math
def fact(x):
    return(math.factorial(x))
factorial1=1
factorial2=1
choice=str(input("Enter if you would like to calculate permutations or combinations (p/c): "))
n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
n_r=n-r
nFact = fact(n)
rFact = fact(r)
n_rFact = fact(n_r)
if choice.lower().strip()=="p":
    print("The number of permutations is:", nFact/n_rFact) 
elif choice.lower().strip()=="c":
    print("The number of combinations is:", nFact/(rFact*n_rFact))
else:
    print("Invalid choice")

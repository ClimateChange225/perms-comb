"""
Created on Sun Nov  6 12:20:44 2022

@author: ahad0
An update to the earlier code.
Added a menu for easier choosing, functionally the same thing.
Now also eliminates negative values and cases where r>n
Same as before, just look up any online python interpreter and you should be good to go
Thanks and best of luck!
"""

import math
def fact(x):
    return(math.factorial(x))
factorial1=1
factorial2=1
print("Choose from the given menu: ")
print("1. Permutations")
print("2. Combinations")
choice=int(input("Type the number corresponding to your choice: "))
if choice==1:
    n=int(input("Enter the value for n: "))
    r=int(input("Enter the value for r: "))
    if 0>n or 0>r:
        print("n or r can't be negative.")
    elif n<r:
        print("r can't be greater than n.")
    else:
        n_r=n-r
        nFact = fact(n)
        n_rFact = fact(n_r)
        print("The number of permutations are:", nFact/n_rFact)
elif choice==2:
    n=int(input("Enter the value for n: "))
    r=int(input("Enter the value for r: "))
    if 0>n or 0>r:
        print("n or r can't be negative.")
    elif n<r:
        print("r can't be greater than n.")
    else:
        n_r=n-r
        nFact = fact(n)
        rFact = fact(r)
        n_rFact = fact(n_r)
        print("The number of combinations are:", nFact/rFact*n_rFact)
else:
    print("Invalid choice")

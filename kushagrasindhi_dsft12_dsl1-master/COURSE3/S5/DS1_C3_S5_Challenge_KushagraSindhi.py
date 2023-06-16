#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math as math

out = """Enter:
a) radians to degrees
b) factorial
c) megabyte to nibble
d) kmph to meter per second
e) int to float
f) decimal to octal
g) decimal to hex
h) decimal to binary
i) character to ascii
j) celcius to fahrenheit
k) degress to radian
l) sqareroot
m) fraction to decimal
n) meter per second to kmph
o) float to int
p) octal to decimal
q) hex to decimal
r) binary to decimal
s) ascii to character
t) fahrenheit to celcius"""


def outer(arg, choice):
    if(isinstance(arg, int)) == True:
        if choice == 'a': # radians to degrees
            return arg * 57.3
    
        elif choice == 'b': # factorial
            return math.factorial(arg)
    
        elif choice == 'c': # megabyte to nibble
            return arg * 2000000
    
        elif choice == 'd': # kmph to meter per second
            return arg / 3.6
    
        elif choice == 'e': # int to float
            return float(arg)
    
        elif choice == 'f': #  decimal to octal
            return oct(arg)
    
        elif choice == 'g': # decimal to hex
            return hex(arg)
    
        elif choice == 'h': #  decimal to binary
            return bin(arg)
        
        elif choice == 'j': #  celcius to fahrenheit
            return (arg * 9/5) + 32
    
        elif choice == 'k': # degress to radian
            return arg * (math.pi / 180)
    
        elif choice == 'l': # sqareroot
            return math.sqrt(arg)
    
   # elif choice == 'm': #  fraction to decimal
    #    return 
    
        elif choice == 'n': # meter per second to kmph
            return arg * 3.6
    
        elif choice == 'o': #  float to int
            return int(arg)
    
        elif choice == 'p': #
            return int(str(arg), 8) # oct to decimal
    
        elif choice == 'q':
            return int(str(arg), 16) # hex to decimal
    
        elif choice == 'r': # binary to decimal
            return int(arg, 2)
        
        elif choice == 't': # fahrenheit to celcius
            return (arg - 32) * (5 / 9)
        
        elif choice == 's': # ascii to character
            return chr(arg)
        
    else:
        if choice == 'i': # character to ascii
            return ord(arg)
        
        

print(out)
print("______________________________________________________________________________")
argu = int(input("Enter the number = "))
choices = input("Enter the corresponding alphabet = ")
print(outer(argu, choices))


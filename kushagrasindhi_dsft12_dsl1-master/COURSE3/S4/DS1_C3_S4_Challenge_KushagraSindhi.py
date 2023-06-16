#!/usr/bin/env python
# coding: utf-8

# In[1]:


score = 0
incorrectcount = 0
while incorrectcount < 5 :
    print("""
    1. Python supports the creation of anonymous functions at runtime, using a construct called __________
    a) pi
    b) anonymous
    c) lambda
    d) none of the mentioned""")
    if(input("Answer = ").lower() == 'c'):
        print("Correct")
        score += 1
    else:
        print("Incorrect, C is correct")
        score -= 1
        incorrectcount += 1
    print("""
    2. What is the order of precedence in python?
    a) Exponential, Parentheses, Multiplication, Division, Addition, Subtraction
    b) Exponential, Parentheses, Division, Multiplication, Addition, Subtraction
    c) Parentheses, Exponential, Multiplication, Division, Subtraction, Addition
    d) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction""")
    if(input("Answer = ").lower() == 'd'):
        print("Correct")
        score += 1
    else:
        print("Incorrect, D is correct")
        score -= 1
        incorrectcount += 1
    print("""
    3. What does pip stand for python?
    a) unlimited length
    b) all private members must have leading and trailing underscores
    c) Preferred Installer Program
    d) none of the mentioned""")
    if(input("Answer = ").lower() == 'c'):
        print("Correct")
        score += 1
    else:
        print("Incorrect, C is correct")
        score -= 1
        incorrectcount += 1
    print("""
    4. Which of the following is true for variable names in Python?
    a) underscore and ampersand are the only two special characters allowed
    b) unlimited length
    c) all private members must have leading and trailing underscores
    d) none of the mentioned""")
    if(input("Answer = ").lower() == 'b'):
        print("Correct")
        score += 1
    else:
        print("Incorrect, B is correct")
        score -= 1
        incorrectcount += 1
    print("""
    5. Which of the following is the truncation division operator in Python?
    a) |
    b) //
    c) /
    d) %""")
    if(input("Answer = ").lower() == 'b'):
        print("Correct")
        score += 1
    else:
        print("Incorrect, B is correct")
        score -= 1
        incorrectcount += 1
    print("""
    6. Which of the following functions is a built-in function in python?
    a) factorial()
    b) print()
    c) seed()
    d) sqrt()""")
    if(input("Answer = ").lower() == 'b'):
        print("Correct")
        score += 1
    else:
        print("Incorrect, B is correct")
        score -= 1
        incorrectcount += 1
    print("""
    7. Which of the following is the use of id() function in python?
    a) Every object doesn’t have a unique id
    b) Id returns the identity of the object
    c) All of the mentioned
    d) None of the mentioned""")
    if(input("Answer = ").lower() == 'b'):
        print("Correct")
        score += 1
    else:
        print("Incorrect, B is correct")
        score -= 1
        incorrectcount += 1
    print("""
    8. Which of the following is not a core data type in Python programming?
    a) Tuples
    b) Lists
    c) Class
    d) Dictionary""")
    if(input("Answer = ").lower() == 'c'):
        print("Correct")
        score += 1
    else:
        print("Incorrect, C is correct")
        score -= 1
        incorrectcount += 1
    print("""
    9. Which of these is the definition for packages in Python?
    a) A set of main modules
    b) A folder of python modules
    c) A number of files containing Python definitions and statements
    d) A set of programs making use of Python modules""")
    if(input("Answer = ").lower() == 'b'):
        print("Correct")
        score += 1
    else:
        print("Incorrect, B is correct")
        score -= 1
        incorrectcount += 1
    print("""
    10. What is the order of namespaces in which Python looks for an identifier?
    a) Python first searches the built-in namespace, then the global namespace and finally the local namespace
    b) Python first searches the built-in namespace, then the local namespace and finally the global namespace
    c) Python first searches the local namespace, then the global namespace and finally the built-in namespace
    d) Python first searches the global namespace, then the local namespace and finally the built-in namespace""")
    if(input("Answer = ").lower() == 'c'):
        print("Correct")
        score += 1
    else:
        print("Incorrect, C is correct")
        score -= 1
        incorrectcount += 1
    print(f"You scored = {score}")
    break


"""
Write a pthon function that accepts a string and calculate the number of upper case letters
and lower case letters
sample string: 'The quick Brow Fox'
Expected output:
No. of Upper case character : 3
No. of Lower case character : 12

"""

#Solution

def count_number(test):
    up = 0
    low = 0
    for c in test:
        if c == " ":
            continue
        elif (c == c.upper()):
            up += 1
            #return "No. of Upper case character : " + up
        else:
            low += 1
            #return "No. of Upper case character : " + low
    result = "No. of Upper case character : {}\nNo. of Lower case character : {}".format(up,low)
    print(result)

test = input("Enter your choice of word: ")
count_number(test)



""" Ass 2
Write a function that finds the maximum of 3 numbers

"""

def max_finder(x):


    for num in x:
        num1 = int(x[0])
        num2 = int(x[1])
        num3 = int(x[2])
    

    # return (num1 + num2 + num3)
        if (num1 > num2 and num3):
            return num1
        if (num2 > num1 and num3):
            return num2
        if (num3 > num1 and num2):
            return num3
        else:
            return "None is greater than another. Try again"
        

number= input("Enter a 3 digit number: ")
print(" The max of {} is {}".format(number,max_finder(number)))




"""

Ass 3
Write a Python function that takes a number as a parameter and check the
number is prime or not
"""

def prime(x):
    if x > 1:
        for i in range(2,x):
            if (x % i == 0):
                return "{} is Not Prime".format(x)
            else:
                return "{} is Prime".format(x)

x = int(input("Enter a number: "))
result = prime(x)
print(result)
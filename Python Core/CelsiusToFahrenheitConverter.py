'''
Celsius to Fahrenheit


You are making a Celsius to Fahrenheit converter.
Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.

Sample Input
36

Sample Output
96.8
'''
celsius = int(input())

def conv(c):

    #your code goes here
    return c * (9/5) + 32
    
    
fahrenheit = conv(celsius  )
print (fahrenheit)

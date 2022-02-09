###
Exponentiation is the raising of one number to the power of another.
This operation is performed using two asterisks **.

Let's use exponentiation to solve a known problem.
You are offered a choice of either $1.000.000 or $0.01 (one penny) doubled every day for 30 days (the resulting amount is doubled every day).

Task:
Write a program to calculate the amount that will result from the doubling to understand which choice results in a larger amount.

Hint:
Let's see how exponentiation can be useful to perform the calculation.
For example, if we want to calculate how much money we will have on the 5th day, we can use this expression: 0.01*(2**5) = 0.32 dollars (multiply the penny by 2 raised to the power of 5).
Use the print statement to output the resulting
###
# your code goes here
H = 0.01 #This is the penny value
num = 1  #this is the day of the montb
while num < 31: 
    a = H*(2**num) #raises H to 2 raised to power of the day of the month
    num +=1 #gets to next day till the end of tbe month
print(a) #get amount

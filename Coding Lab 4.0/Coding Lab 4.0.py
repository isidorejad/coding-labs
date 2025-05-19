# Declaration of variables
num1 = int
num2 = int
num3 = int
text = "Average is: "

# Info about program
print("<--This program is designed to calculate the average of any three(3) numbers.-->")
print("<--Enter any three numbers to check the average.-->")

# Prompt the user to enter three numbers
num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Storing sum and average into a function
def sum_avg():
    avg = (num1 + num2 + num3) / 3
    print(text) 
    print(avg)
sum_avg()

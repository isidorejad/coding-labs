# To determine whether a hnumber is odd or even  
# Using conditionals to meet particular results
i = 0
user_num = int(input('Please enter any number to begin: '))
while user_num != 0:
   user_num = int(input("Enter your number: "))
   if (user_num % 2) == 0:
      print("{0} is an Even number".format(user_num))
   elif user_num != 0:
      user_num = int(input("Enter your number: "))
   else:
      print("{0} is an Odd number".format(user_num))
i = i + 1

# To determine whether a hnumber is odd or even  
# Using conditionals to meet particular results
i = 4
for i in range (0,4):
   user_num = int(input("Enter your number: "))
   if (user_num % 2) == 0:
      print("{0} is an Even number".format(user_num))
   else:
      print("{0} is an Odd number".format(user_num))

i = i - 1

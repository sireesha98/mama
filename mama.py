nbr =input()
if nbr < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(nbr > 0):
       sum += nbr
       nbr -= 1
   print("The sum is",sum)

number = int(input("Enter a number"))
print("The even numbers from 0 to {} are:".format(number))
for i in range(2, number+1, 2):
  print(i)
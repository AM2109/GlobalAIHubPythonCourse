number = int(input("Enter a single digit integer"))
if number >= 9 or number <= -9:
    print("The number isn't a single digit!")
else:
    print("The even numbers from 0 to {} are:".format(number))
    if number < 0:
        for i in range(number, 1):
            if i % 2 == 0:
                print(i)
    
    else:
        for i in range(0, number+1):
            if i % 2 == 0:
                print(i)
            else:
                continue
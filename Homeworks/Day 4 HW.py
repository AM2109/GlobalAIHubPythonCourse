"""
variables i and j have been used in for loop 
variable counter has been used to count the number of factors of the number
if the number of factors (count == 2) is 2, it is a prime number
"""
print("The prime numbers from 1 to 100 are:")
def prime_numbers():

  for i in range(2,101):
    count = 0
    for j in range (1, i+1):
        if i%j == 0:
            count += 1
    
    if count == 2:
        print(i)

prime_numbers()
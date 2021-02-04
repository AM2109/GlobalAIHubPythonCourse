#Asking the user for the length of the list
length = int(input("Enter length of list"))
length_for_while_loop = length
list1 = []
#Getting the user to input the elements of the list
print("Enter elements of list")
while length_for_while_loop != 0:
  new_element = input()
  list1.append(new_element)
  length_for_while_loop -= 1
print("The list that you entered is:")
print(list1)
middle = length//2
print("The list after swapping the first half and the second half:")
print(list1[middle:length], list1[0:middle])

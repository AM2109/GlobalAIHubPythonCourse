import time
print("*************** SIGN UP ***************")
username = input("Enter username: ")
password = input("Enter password: ")
details = {"id":username, "pswd":password}
print("\n\n*************** SIGN IN ***************")
inputted_username = input("Enter your username: ")
inputted_password = input("Enter your password: ")
if inputted_username == details["id"]:
  if inputted_password != details["pswd"]:
    print("Invalid Password!")
  else:
    print("Logging in...")
    time.sleep(5)
    print("Your are now logged in.")
else:
   print("invalid username!")


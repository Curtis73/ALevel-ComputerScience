import re
pattern = re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$")

print("""
Criteria:
  Minimum 8 Characters
  At least one uppercase letter
  At least one lowercase letter
  At least one number
  At least one special character
  Less than 18 characters
""")

password = input("Please input your password: ")

if (len(password) > 18):
    print ("Please input a password with less than 18 characters")
    password = input("Please input your password: ")

if pattern.match(password):
    print("Your password meets the criteria!")
else:
    print("Your password doesn't meet the criteria!")
'''
username = input("Username: ")
password = input("Password: ")
if username == 'admin' and password == 'admin123':
    print("Login Successful")
else:
    print("Invalid Credentials")
 

products = ["laptop","mouse","bag","bottle"]
search = input("Enter the product: ")
if search in products:
    print(f'{search} found')
else:
    print(f'{search} not found')
   '''

bill = int(input("Enter the bill: "))
if bill > 99:
    print("Final bill:",bill)
else:
    print("Final bill+ del cha:",bill+30)

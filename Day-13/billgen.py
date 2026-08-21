data = {
    'sugar' : 50,
    'salt' : 30,
    'cooking oil':90,
    'chilli powder': 70,
    'eggs':70,
    'peanuts':85,
    'rice':130,
    'butter':130,
    'bread':200,
    'wheatfloor': 100
}

for i in data:
    print(i.ljust(20),data[i])

prods = input("Enter the products: ").split()
print("---------------Bill---------------")
bill = 0
for i in prods:
    print(i.ljust(20),data[i])
    bill += data[i]
print("Total bill".ljust(20),bill)

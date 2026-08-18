'''budget = int(input("Enter the budget: "))
if budget > 10000:
    print("Trip")
elif budget > 5000:
    print("Resort Stay")
elif budget > 3000:
    print("Movie and Dinner")
elif budget > 1000:
    print("Cafe and Shopping")
elif budget > 500:
    print("Street Food and Park Visit")
else:
    print("Stay Home")'''


hr = int(input("Enter the time: "))

if 5<= hr <=11:
    print("Good Morning")
elif 12 <= hr <=16:
    print("Good Afternoon")
elif 17 <=hr <= 20:
    print("Good Evening")
elif 21 <= hr < 24:
    print("Good Night")
else:
    print("Midnight sleep well")
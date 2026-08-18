'''
fa = eval(input("Follows Account: "))
if fa:
    cf = eval(input("Close Friend: "))
    if cf:
        print("Story Visible")
    else:
        print("Not in Close Friends List")
else:
    print("Follow the Account First") 

reg = eval(input("Registered: "))
if reg:
    fee = eval(input("Fee Paid: "))
    if fee:
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registration Required")
'''

data = {
    'lohitha':{'status':True,'python':90,'mysql':95,'flask':98},
    'dipak':{'status':False,'python':None,'mysql':None,'flask':None},
    'teja':{'status':True,'python':20,'mysql':35,'flask':38},
    'dinesh':{'status':True,'python':60,'mysql':65,'flask':68},
    'kalyani':{'status':True,'python':70,'mysql':75,'flask':78},
    'usharani':{'status':True,'python':80,'mysql':85,'flask':88}
}

name = input("Enter the name: ")
if name in data:
    if data[name]['status']:
        sum = data[name]['python'] + data[name]['mysql'] + data[name]['flask']
        avg = sum/3
        print(f"Hello {name}!!!")
        print(f"Your average score is {avg}")
        if avg >= 90:
            print("Outstanding performance")
        elif avg >= 80:
            print("Very Good")
        elif avg >= 70:
            print("Good, Work hard")
        elif avg >= 35:
            print("Better luck next time")
        else:
            print("You Failed the exam, try hard")

    else:
        print(f'{name} did not attend the exam, bring your parents')
else:
    print(f'{name} not found in the data')




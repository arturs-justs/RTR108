# first part is training:

print('This is training part')

x=int(input("Please enter x: ")) # vadam iekšā x
y=int(input("Please enter y: ")) # vadam iekšā y
if x > 0 and x < 10: # pārbaudām x
    print('x is single-digit number')
if y > 0 and y < 10: # pārbaudām y
    print('y is single-digit number')

if x > 0 : # pārbaudām vai x ir pozitīvs
    print('x is positive number')
if y > 0 : # pārbaudām vai y ir pozitīvs
    print('y is positive number')

if x < y: # pārbaudām vai x < y
    print('x is less than y')
elif x > y: # pārbaudām vai x > y
    print('x is greater than y')
else: # ja x > y un x < y nav tad programma printē "x and y are equal"
    print('x and y are equal')

if x%2 == 0 : # pārbauda vai x ir pāra skaitlis
    print('x is even')
else : # ja nav printē šo
    print('x is odd')

if y%2 == 0 : # pārbauda vai y ir pāra skaitlis
    print('y is even')
else : # ja nav printē šo
    print('y is odd')

choice=str(input("Choose a/b/c: ")) # vadam iekšā a vai b, vai c un pārbaudam, kas tika ievadīts
if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('Close, but not correct')
else :
    print('CHOOSE THE LETTER! (a or b or c)')

# Exercises 1,2 here:

print('Here is exercises 1 and 2:')

hours=input("Enter total hours: ") # vadam iekšā stundas
rate=input("Enter hourly rate: ") # vadam iekšā stundas
try:
    hours2 = int(hours)
    rate2 = int(rate)
    hr = hours2*rate2
    if hours2 > 40: # ja ir vairāk neka 40 stundas parādās koef. 1.5
        hra=hr*1.5
        print("Pay:", hra)
    else :
        print("Pay:", hr)
except:
    print('Please enter a numbers in "total hours" and "rate"')

# Exercise 3 here:

print('Here is exercise 3:')

grade=input("Enter score: ")
try:
    grade2 = float(grade)

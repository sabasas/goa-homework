# მომხმარებელს შეეკითხეთ რიცხვი შემდეგ შექმენით ფუნქცია რომელსაც ექნება პარამეტრი რომელსაც არგუმენტად გადაეცემა მომხლარებლის შემოტანილი რიცხვი შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი

num =int(input("Enter the number: "))

def number(num):
    if num % 2==0:
        print("It is even")

    else:
        print("it is odd")    

number(num)        
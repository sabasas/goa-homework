 # მომხმარებელს შეეკითხეთ რიცხვი შემდეგ შექმენით ფუნქცია რომელსაც ექნება პარამეტრი რომელსაც არგუმენტად გადაეცემა მომხლარებლის შემოტანილი რიცხვი შემდეგ კი დაბეჭდავს ეს რიცხვი დადებითია თუ უარყოფითი

num = int(input("Enter the number: "))

def number(num):
    if num >= 0 :
        print("The number is positive")

    else:
        print("The number is not positive")    


number(num)
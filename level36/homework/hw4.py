#  მომხმარებელს შეეკითხეთ ორი რიცხვი შემდეგ შექმენით ფუნქცია რომელსაც ექნება ორი პარატემტრი რომელსაც არგუმენტად გადაეცემა მომხლარებლის შემოტანილი რიცხვები შემდეგ კი დაბეჭდავს მათ განაყოფს

def number(a,b):
    result = a//b
    print(result)


num = int(input("Enter the number: "))
num1 = int(input("Enter second number: "))

number(num,num1)
# მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ კი დაბეჭდეთ ერთიდან ამ რიცხვამდე მხოლოდ ლუწი რიცხვების ჯამი ცალკე და მხოლოდ კენტი რიცვხების ჯამი
#  ცალკე, გამოიყენეთ for loop
num = int(input("enter your number:"))
num1 = int(input("two number:"))
x = 0
w = 0
for i in range(num):
    if i % 2 ==0:
        x=x+i

for i in range(num1):
    if i % 3 ==0:
        w=w+i

print(x)
print(w)

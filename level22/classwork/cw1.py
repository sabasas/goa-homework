# მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ მხოლოდ ლუწი რიცხვების ჯამი, გამოიყენეთ for loop

num = int(input("enter your name:"))
x =0
for i in range(num):
    if i % 2==0:
        x=x+i

print(x)        

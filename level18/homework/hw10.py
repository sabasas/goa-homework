# მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ლუწი რიცხვები

num = int (input("შეიყვანე რიცხვი:"))
for i in range(num):
    if i % 2 == 0:
        print(i)  
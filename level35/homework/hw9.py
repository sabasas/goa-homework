# შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა რიცხვს

def number():
    num = int(input("შეიყვანე რიცხვი: "))
    for i in range(1, 1+ num):
        print(i)

number()
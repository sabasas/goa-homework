#  შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა კენტ რიცხვს

def number():
    num = int(input("შეიყვანე რიცხვი: "))
    for i in range(1,num +1, 2):
        print(i)
             
number()
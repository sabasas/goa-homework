 # მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ორზე ნამრავლების ჯამი

num = int(input("შეიყვანეთ სახელი :"))

sum = 0

for i in range(1, num + 1):
    sum += i * 2

print(sum)    
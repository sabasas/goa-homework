# შეიყვანეთ რიცხვი და გამოიყენეთ while ციკლი, რომ დაბეჭდოთ ყველა რიცხვი 1-დან იმ რიცხვამდე.

num = int(input("შიყვანეთ რიცხვი:"))
num1 = 1
while num1 <= num: # ციკლი იმუშავებს მანამ სანამ num1 არ გადააჭარბებს num
    print(num1) # დაბეჭდავს num მიმდენარე მნიშვნელობას
    num1 += 1  # ნუმ1 ზრდის ყოველ იტერაციის შედეგ 1

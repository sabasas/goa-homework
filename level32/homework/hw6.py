# გააკეთეთ Sum Of Odd Numbers. მიზანი: შეკრიბეთ ყველა კენტი რიცხვი და შეინახეთ სიაში შემდეგ ეგ სია დაპრინტეთ 10 ჯერ

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = 0

for i in numbers:
    if i % 2 != 0:
        odd_numbers += i

result =[odd_numbers]

for i in range(10):
    print(result)
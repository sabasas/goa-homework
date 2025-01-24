# გააკეთეთ Sum Of Even Numbers. მიზანი: შეკრიბეთ ყველა ლუწი რიცხვი და შეინახეთ სიაში შემდეგ ეგ სია დაპრინტეთ 10 ჯერ

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = 0

for i in numbers:
    if i % 2==0:
        even_numbers += i

result =[even_numbers]


for num in range(10):
    print(result)
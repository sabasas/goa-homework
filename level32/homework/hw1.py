# გააკეთეთ Filter Even Numbers. მიზანი: გაფილტრეთ ყველრა ლუწი რიცხვი და ჩაამატეთ ახალ სიაში და შემდეგ ეგ სია დაპრინტეთ 

numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers=[]

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

# გააკეთეთ Filter Odd Numbers. მიზანი: გაფილტრეთ ყველრა კენტი რიცხვი და ჩაამატეთ ახალ სიაში და შემდეგ ეგ სია დაპრინტეთ
numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []

for i in numbers:
    if i % 2 != 0:
        odd_numbers.append(i)

print(odd_numbers)        
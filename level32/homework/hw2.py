# გააკეთეთ Find Maximum და გამოიყენეთ for loop. მიზანი: სიაში უნდა იპოვოთ მაქსიმუმი ინტეჯერი მაგალითად: [1, 546, 456 ,123] => [546]

numbers =[1, 546, 456, 123]
max_number = numbers[0]

for i in numbers:
    if i > max_number:
        max_number = i

result = [max_number]   
print(result)     
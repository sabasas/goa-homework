# გააკეთეთ Find Minimum და გამოიყენეთ for loop. მიზანი: სიაში უნდა იპოვოთ მინიმალური ინტეჯერი მაგალითად: [1, 546, 456 ,123] => [1]

numbers =[1, 546, 456, 123]
min_numbers = numbers[0]

for i in numbers:
    if i < min_numbers:
        min_numbers = i

result = [min_numbers]
print(result)
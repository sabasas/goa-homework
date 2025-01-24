# გააკეთეთ Reverse List და გამოიყენეთ while loop. შემოაბრუნეთ ყველა რიცხვი ლისტში. ახსნა: [1, 2, 3, 4,  5] => [5, 4, 3, 2, 1]

numbers =[1, 2, 3, 4, 5]
reverse_list =[]

while numbers:
    num = numbers.pop()
    reverse_list.append(num)

print(reverse_list)    
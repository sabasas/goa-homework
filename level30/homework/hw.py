# შექმენით ლისტი სადაც გექნებათ 1-10 ჩათვლით რიცხვები და დაპრინტეთ მხოლოდ ლუწი რიცხვები

numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num =[] 
for i in numbers: 
    if i % 2==0: 
        num.append(i)

print(num)
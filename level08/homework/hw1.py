# a = 5
# b = "10"
# result = a + b
# print("Result:", result)

# კოდი გამოიტანს ერორს დაწერეთ რატომ და ასევე ცალკე დაწერეთ სწორი ფორმა

# პრობლემა  არის მესამე ხაზში რადგან result არის ცვლადი. ასევე int არ ემატება str.

a = 5
b = "10"
result = a + int(b)
print("Result:", result)

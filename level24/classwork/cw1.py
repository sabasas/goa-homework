#გააკეთეთ სარეგისტრაციო, მომხმარებელს შემოატანიეთ სახელი და პაროლი, რეგისტრაციის შემდეგ მოხმარებელი უნდა შევიდეს ექაუნთზე, შეეკითხეთ სახელი და პაროლი მომხარებელს რათა შევიდეს ექაუნთზე სანამ მომხმარებელი არ შეიტანს იმ ინფორმაციას რაც შეიყვანა რეგისტრაციის დროს მანამ დაიბეჭდოს რომ შეტანილი ინფორმაცია არასწორია და შეეკითხოს თავიდან, ხოლო თუ მომხმარებელმა ყველაფერი სწორად შეიყვანა დაიბეჭდოს welcome

print("registration")
name = input("Enter your name; ")
password  = input("Enter your password; ")

print("login")
n_name =input("Enter your name; ")
p_password = input("Enter your password; ")

while n_name != name or p_password != password:
    print("your password or name is inccorect!")
    n_name =input("Enter your name; ")
p_password = input("Enter your password; ")

print("W E L C O M E:")    
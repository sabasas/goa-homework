#  დაწერეთ ციკლი რომელიც ლუწს გამოიტანს " მე მიყვარს გოა" და კენტს " მე მიყვარს პროგრამირება".

for i in range(100): # ციკლი გაიზრდება 0 დან 99
    if i % 2 == 0:   # ვამოწმებთ პირობა ლუწია თუ არა
        print(str(i)+"."+"მე მიყვარს გოა") # თუ ლუწია ბეჭდავს ამას
    else:
        print(str(i)+"."+"მე მიყვარს პროგრამირება") # თუ კენტია ამას
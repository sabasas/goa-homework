#  შექმენით ფუნქცია რომელსაც ექნება ორი პარამეტრი ხოლო ამ ფუნქციამ უნდა გადაამრავლოს ეს ორი რიცხვი ერთმანეთზე შემდეგ კი დაიბეჭდოს მიღებული ნარმავლი ლუწია თუ კენტი ნამრავლთან ერთად, გამოიძახეთ ეს ფუნქცია რამდენჯერმე და გადაეცით არგუმენტები(სვადასვა რიცხვები)

def multiplay(num1, num2):
    result = num1 * num2
    if result % 2==0:
        print("result is " + str(result)+ " and its even")
    else:
        print("result is " + str(result)+ " and its odd")   

multiplay(2, 3)
multiplay(4, 4)
multiplay(5, 3)
multiplay(2, 6)
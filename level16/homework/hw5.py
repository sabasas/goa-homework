# დედამ გაგიშვათ აფთიაქში თავის ტკივილის წამლის საყიდლათ, ეს წამალი დღეში უნდა დალიო შენი წონის მიხედვით. თუ 10 დან 20 კილომდე
#  ხარ ნახევარი ტაბლეტი უნდა დალიო დღეში, თუ 30-40 კილომდე ხარ 1 ტაბლეთი ორჯერ დღეში და თუ 45 კილოზე მეტი ხარ სამი ტაბლეტი უნდა
#  დალიო ორჯერ დღეში. თქვენი მისიაა ამ ინფორმაციით გაარკვიოთ მომხარებელს რამდენი წამალი აქვს დასალევი და დღეში რამდენჯერ უნდა დალიოს.

kg = float(input("შეიყვანე შენი წონა:"))
if kg >= 10 and kg <=20:
    print("შენი დოზა არის ნახევარი ტაბლეტი დღეში 1 ხელ")

elif kg >=30 and kg<= 40:
    print("შენი დოზა არის 1 ტაბლეტი დღეში 2 ჯერ")

elif kg >= 45:
    print("შენი დოზა არის 3 ტაბლეტი დღეში 2 ჯერ")
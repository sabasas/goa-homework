# შექმენით shopping სია სადაც მომხმარებელს შეეძლება რამე ნებისმიერი პროუქტის დამატება და წაშლა, როდესაც მორჩებიან შოპინგს დაუპრინტეთ საბოლოოდ რა შეიძინეს 

shopping_list =[]
shopping = True

while shopping:
    num = input("რა გსურთ? (დამატება/წაშლა/დასრულება): ")

    if num =="დამატება":
        num1 = input("რა დავამატო?: ")
        shopping_list.append(num1)

    elif num == "წაშლა:":
        num1 = input("რა წავშალო?: ")
        shopping_list.remove(num1)       

    elif num == "დასრულება":
        print("თქვენ შეიძინეთ")
        for num1 in shopping_list:
            print(num1)
        shopping = False
        
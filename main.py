flag = True
while True:
    try:
        num1 = int(input("Enter a number: "))
        choise = input("Выберите операцию: + - * /   (0) - Выход: ")
        num2 = int(input("Enter a number: "))
        if choise == "+":
            print(num1 + num2)

        elif choise == "-":
            print(num1 - num2)

        elif choise == "*":
            print(num1 * num2)

        elif choise == "/":
            print(num1 / num2)

        elif choise == "0":
            flag = False

        else:
            print("Ошибка выбора операции:")
    except ValueError as e:
        print(f"Ошибка, вводите цифры")

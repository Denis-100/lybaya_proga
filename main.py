while True:
    try:
        num1 = int(input("Enter a number: "))
        choise = input("Выберите операцию: + - * /   (0) - Выход")
        num2 = int(input("Enter a number: "))
        if choise == "+":
            pass
        elif choise == "-":
            pass

        elif choise == "*":
            pass
        elif choise == "/":
            pass
        else:
            print("Ошибка выбора операции:")
    except ValueError as e:
        print(f"Ошибка, вводите цифры")

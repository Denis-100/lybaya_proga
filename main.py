while True:
    try:
        num1 = float(input("Enter a number: "))
        choise = input("Выберите операцию: + - * /   (0) - Выход: ")
        if choise == "0":
            print("Выход")
            break

        num2 = float(input("Enter a number: "))

        if choise == "+":
            print(num1 + num2)

        elif choise == "-":
            print(num1 - num2)

        elif choise == "*":
            print(num1 * num2)

        elif choise == "/":
            try:
                print(num1 / num2)
            except ZeroDivisionError:
                print("Ошибка. На ноль делить нельзя")

        else:
            print("Ошибка выбора операции:")
    except ValueError as e:
        print(f"Ошибка, вводите цифры")

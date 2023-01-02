#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#  Пример:
#  - 6 -> да
#  - 7 -> да
#  - 1 -> нет

def inputNumbers(inputText): #Защита от дурака
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def checkTerms(num):
    if 6 <= num <= 7:
        print("День является выходным")
    elif 0 < num < 6:
        print("День не является выходным")
    else:
        print("Некорректное число")

num = inputNumbers("Введите число от 0 до 7: ")
checkTerms(num)


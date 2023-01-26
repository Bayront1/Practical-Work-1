number_operation = int(input("Введите количество операций: "))

for i in range(number_operation):
    functions = input("Выберите функцию (+,-,/,*): ")
    number_one = float(input("Введите первое число: "))
    number_two = float(input("Введите второе число: "))
    result = 0
    if functions == '+':
        result = (number_one + number_two)
 
    elif functions == '-':
       result = (number_one - number_two)
  
    elif functions == '/':
        if number_two !=0:
            result = (number_one / number_two)
        else: print("Ошибка! На ноль делить нельзя!")
 
    elif functions == '*':
       result = (number_one * number_two)
    else: print("Ошибка! Данной операции нет!")
    
    print(int(result))


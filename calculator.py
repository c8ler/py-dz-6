# не доделал
# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

def Enumeration(str):
    array_of_string = list(str)
    enumerate = []
    temp = ''
    for i in range(0, len(array_of_string)):
        try:
            int(array_of_string[i])
            temp += array_of_string[i]
        except:
            enumerate.append(temp)
            enumerate.append(array_of_string[i])
            temp = ''
    enumerate.append(array_of_string[-1])
    return enumerate


def Check(str):
    array_of_string = list(str)
    check = ['0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', '+', '-', '/', '*', '(', ')']
    for i in range(0, len(array_of_string)):
        if array_of_string[i] not in check:
            print("В строке должны быть только целые числа и знаки операций + - / * ( ).")
            quit()


string = str(input("Введите пример: "))
Check(string)
print(Enumeration(string))

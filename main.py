from triangle import EquilateralTriangle

Triangle = EquilateralTriangle()

first_choice = str(input('Введите параметр, по которому будут веститсь подсчеты: '))  
if (type(first_choice) == str):
    #while(first_choice.type() == str):
        if (first_choice == 'a'): 
            a = -1
            while (a <= 0): 
                a = float(input('Введите сторону треугольника: '))
                if (a <= 0):
                    print('Такого треугольника не существует! Попробуйте ввести другое значение.')
            Triangle.side = a       
        elif (first_choice == 'R1'):
            R1 = float(input('Введите радиус вписанной окружности: '))
            if (R1 <= 0):
                while (R1 <= 0):
                    print('Такого треугольника не существует! Попробуйте ввести другое значение.')
            Triangle.r_inscribed_circle = R1
        elif (first_choice == 'R2'):
            R2 = float(input('Введите радиус описанной окружности: '))
            if (R2 <= 0):
                while(R2 <= 0):
                    print('Такого треугольника не существует! Попробуйте ввести другое значение.')
            Triangle.r_circumscribed_circle = R2
        elif (first_choice == 'S'):
            S = float(input('Введите площадь равностороннего треугольника: '))
            while (S <= 0):
                if (S <= 0):
                    print('Такого треугольника не существует!')
            Triangle.area = S
else:
    while(first_choice.type() == int or float):
        print('Вы ввели число, а нужно строку! Попробуйте заново!')
    
print(Triangle)

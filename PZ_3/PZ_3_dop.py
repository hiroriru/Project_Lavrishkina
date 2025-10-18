'''
Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном 
случае увеличить его в 1.5 раза. 
'''
try:
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))
    mult = num_1 * num_2
    
    if mult < 0:
      op_1 = mult * 8
      print(op_1)
    else:
      op_2 = mult * 1.5
      print(op_2)
      
except ValueError:
    print("Пожалуйста, попробуйте снова.")
    


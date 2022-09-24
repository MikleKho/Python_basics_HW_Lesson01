# 4. Напишите программу, которая по заданному номеру четверти показывает 
# диапазон возможных координат точек в этой четверти (x и y).

number_quarter = int(input("Input number of quarter --->  "))
if number_quarter == 1:
    print("Points with x > 0 and y > 0")
elif number_quarter == 2:
    print("Points with x < 0 and y > 0")
elif number_quarter == 3:
    print("Points with x < 0 and y < 0")
elif number_quarter == 4:
    print("Points with x > 0 and y < 0")
else:
    print("Input error")
# 5. Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.

x_first = int(input("Input X coordinate first point --->  "))
y_first = int(input("Input Y coordinate first point --->  "))
x_second = int(input("Input X coordinate second point --->  "))
y_second = int(input("Input Y coordinate second point --->  "))
print("Distance berween points ---->", 
'%.4f' % ((x_first - x_second) ** 2 + (y_first - y_second) ** 2) ** 0.5)
# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_number = int(input("Input number of the day ---> "))
if day_number == 6 or day_number == 7:
    print("Weekend")
elif day_number > 0 and day_number < 6:
    print("Workday")
else:
    print("It`s not a day of the week")

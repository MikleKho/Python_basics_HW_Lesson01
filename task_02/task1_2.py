# 2. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


print("x, y, z, result operation")
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, x, "      ", (not (x or y or z)) == (not x and not y and not z))
            

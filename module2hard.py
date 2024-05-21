#Вариант 1
#n = int(input('Введите первое число (от 3 до 20): ', ))
#result = []
#for i in range(1, 21):
#    for j in range(i + 1, 21):
#        if n % (i + j) == 0:
#            result += str(i) + str(j)
#
#print(*result)

#Вариаант 2
for n in range(3, 21):
    result = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    print(n, ' - ', *result)

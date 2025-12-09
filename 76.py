import matplotlib.pyplot as plt
file = open("C:\\Users\\neyle\\doc\\opendata.stat.txt", encoding = "utf-8")
file.readline() #Пропуск строки
pension = []
month = []

for line in file: # 7-14 строка обработка каждой строки файла
    cur = line.split(',')
    date = cur[2]
    if cur[0] == "Средняя пенсия" and cur[1] == "Забайкальский край":
        year = int(date.split("-")[0])
        if year == 2018:
            month.append(int(date.split("-")[1]))
            pension.append(int(cur[3])) 
if len(pension) == 0: # Вычисление средней пенсии с проверкой деления на 0
    print('Нет информации про пенсию в Забайкальском крае на 2018 год.')
else:
    answer = sum(pension) / len(pension)
    print('Средняя пенсия в Забайкальском крае составила:', round(answer, 1), 'рублей')
    plt.plot(month, pension) # 20-25 строка построение графика
    plt.title('График изменения пенсии в Забайкальском районе в 2018')
    plt.xlabel('Дата')
    plt.ylabel('Сумма')
    plt.grid(True)
    plt.show()

#Строка содержит пять временных значений. Они записаны через запятую:
#'1h 45m,360s,25m,30m 120s,2h 60s'.
#Напиши цикл, который посчитает общее количество минут. Результат сохрани в переменную и выведи на экран. Используй в решении методы split(), 
# replace() и оператор in.
#Обрати внимание: временное значение может состоять из одного, двух или трёх единиц времени. Значения расшифровываются так:
#часы — любое положительное целое число и символ h;
#минуты — любое положительное целое число и символ m;
#секунды — положительное целое число кратное 60 и символ s.

string = '1h 45m,360s,25m,30m 120s,2h 60s'
time_lst = ' '.join(string.split(',')).split()

all_munites = 0

for time in time_lst:
    if 'h' in time:
        hour = (time.replace('h', ''))
        all_munites += int(hour) / 60
        
    elif 'm' in time:
        minutes = (time.replace('m', ''))
        all_munites += int(minutes) 
        
    elif time[-1] == 's':
        seconds = (time.replace('s', ''))
        all_munites += int(seconds) * 60


print(int(all_munites))

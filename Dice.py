import random, time

NumberOfDice = int(input('Количество костей:  '))

results = {}
for i in range(NumberOfDice,  (NumberOfDice*6)+1):
    results[i] = 0

print('Моделириуем броски костей')

lastPrintTime = time.time()

for i in range(1000000):
    if time.time() > lastPrintTime +1:
        print('{}% done...'.format(round(i/10000, 1)))
        lastPrintTime = time.time()

    total = 0
    for j in range(NumberOfDice):
        total = total + random.randint(1, 6)
    results[total] += 1

print('TOTAL - ROLLS - PERCENTAGE')
for i in range(NumberOfDice, (NumberOfDice*6) +1):
    roll = results[i]
    percentage = round(results[i]/1000, 1)
    print(' {} - {} rolls - {}%'.format(i,roll,percentage))
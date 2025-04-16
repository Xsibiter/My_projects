'''Данная программа отображает на экране выбранное
пользователем сообщение синусовидной волной по мере
прокрутки текста. Это возможно благодаря функции
math.sin(), реализующей тригонометрическую волновую
функцию синус. Но даже если математическая сторона
вам непонятна, программа довольно коротка и скопировать
ее легко'''

import math,sys, time
import shutil as sh

#Size of the window
WIDTH, HEIGHT = sh.get_terminal_size()
# В Windows нельзя вывести что-либо в последнем столбце без добавления
 # автоматически символа новой строки, поэтому уменьшаем ширину на 1:
WIDTH -= 1
print('Sine message, by Vlad - SLON')
print('(Print Ctrl-C to quit.)')
print('What meassage do you want to display? (MAX', WIDTH // 2, 'chars.) ')
while True:
    message = input('>')
    if 1 <= len(message) <= (WIDTH // 2):
        break
    print('Message must be 1 to', WIDTH // 2, 'characters long.')
step = 0.0
# step определяет, в каком месте синусоиды мы находимся.
# Синус принимает значения от -1.0 до 1.0, так что необходимо умножить на коэффициент:
multiplier = (WIDTH -len(message)) / 2
try:
    while True:
        sinOfStep = math.sin(step)
        padding = ' ' * int((sinOfStep + 1) * multiplier)
        print(padding + message)
        time.sleep(0.1)
        step += 0.2  # (!) Попробуйте заменить это значение на 0.1 или 0.5.
except KeyboardInterrupt:
        sys.exit()  # Если нажато сочетание клавиш Ctrl+C — завершаем программу
import random
import time

BAR = chr(9608)   # Символ 9608 – '█'


def main():
    print('Progress Bar Simulation')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        bytesDownloaded += random.randint(0,100)

        barStr = get_progress_bar(bytesDownloaded, downloadSize)

        print(barStr, end='', flush=True)
        time.sleep(0.2)

        print('\b'*len(barStr), end='', flush = True )


def get_progress_bar(progress, total, barWidth=40):
    progressBar = ' ' # Индикатор хода выполнения будет строковым значением.
    progressBar += '['  # Добавляем левый конец индикатора хода выполнения.

    # Убеждаемся, что progress находится между 0 и total
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    numberOfBars = int((progress/total)*barWidth)

    progressBar += BAR * numberOfBars # Индикатор хода выполнения
    progressBar += ' ' * (barWidth-numberOfBars)

    progressBar += ']'

    percentComplete = round(progress / total *100, 1)
    progressBar += '' + str(percentComplete) + '%'

    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar

if __name__ == '__main__':
    main()

spinner = ['|', '/', '-', '\\']
while True:
    for frame in spinner:
        print('\r' + frame, end='', flush=True)
        time.sleep(0.1)
import math, time, sys, os


PAUSE_AMOUNT = 0.1  # Пауза между кадрами (секунды)
WIDTH, HEIGHT = 80, 24
SCALEX = (WIDTH - 4) // 8
SCALEY = ((HEIGHT - 4) // 8) * 2  # Учитываем пропорции текста
TRANSLATEX = (WIDTH - 4) // 2
TRANSLATEY = (HEIGHT - 4) // 2
LINE_CHAR = chr(9608)  # Символ █ (плотная заливка)

# Скорости вращения
X_ROTATE_SPEED = 0.1
Y_ROTATE_SPEED = 0.1
Z_ROTATE_SPEED = 0.0

# Индексы координат
X, Y, Z = 0, 1, 2


# Алгоритм Брезенхэма (рисование линии)
def line(x1, y1, x2, y2):
    points = []
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]

    isSteep = abs(y2 - y1) > abs(x2 - x1)
    if isSteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    isReversed = x1 > x2
    if isReversed:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y2
        ydirection = 1 if y1 < y2 else -1
        for currentx in range(x2, x1 - 1, -1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray <= 0:
                currenty -= ydirection
                extray += deltax
    else:
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y1
        ydirection = 1 if y1 < y2 else -1
        for currentx in range(x1, x2 + 1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray < 0:
                currenty += ydirection
                extray += deltax
    return points


# Вращение точки в 3D
def rotatePoint(x, y, z, ax, ay, az):
    # Ось X
    rotatedX = x
    rotatedY = y * math.cos(ax) - z * math.sin(ax)
    rotatedZ = y * math.sin(ax) + z * math.cos(ax)
    x, y, z = rotatedX, rotatedY, rotatedZ

    # Ось Y
    rotatedX = z * math.sin(ay) + x * math.cos(ay)
    rotatedY = y
    rotatedZ = z * math.cos(ay) - x * math.sin(ay)
    x, y, z = rotatedX, rotatedY, rotatedZ

    # Ось Z
    rotatedX = x * math.cos(az) - y * math.sin(az)
    rotatedY = x * math.sin(az) + y * math.cos(az)
    rotatedZ = z

    return (rotatedX, rotatedY, rotatedZ)


# Преобразование 3D -> 2D
def adjustPoint(point):
    return (
        int(point[X] * SCALEX + TRANSLATEX),
        int(point[Y] * SCALEY + TRANSLATEY)
    )


# Углы куба (угловые точки)
CUBE_CORNERS = [
    [-1, -1, -1],
    [1, -1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [-1, 1, -1],
    [1, 1, -1],
    [-1, 1, 1],
    [1, 1, 1],
]

rotatedCorners = [None] * 8
xRotation = yRotation = zRotation = 0.0

try:
    while True:
        # Увеличиваем углы
        xRotation += X_ROTATE_SPEED
        yRotation += Y_ROTATE_SPEED
        zRotation += Z_ROTATE_SPEED

        # Вращение точек
        for i in range(len(CUBE_CORNERS)):
            x, y, z = CUBE_CORNERS[i]
            rotatedCorners[i] = rotatePoint(x, y, z, xRotation, yRotation, zRotation)

        # Получаем линии куба
        cubePoints = []
        edges = [
            (0, 1), (1, 3), (3, 2), (2, 0),
            (0, 4), (1, 5), (2, 6), (3, 7),
            (4, 5), (5, 7), (7, 6), (6, 4),
        ]
        for fromIdx, toIdx in edges:
            fromX, fromY = adjustPoint(rotatedCorners[fromIdx])
            toX, toY = adjustPoint(rotatedCorners[toIdx])
            cubePoints.extend(line(fromX, fromY, toX, toY))

        cubePoints = frozenset(cubePoints)

        # Отображение
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in cubePoints:
                    print(LINE_CHAR, end='', flush=False)
                else:
                    print(' ', end='', flush=False)
            print(flush=False)
        print('Press Ctrl-C to quit.', end='', flush=True)

        time.sleep(PAUSE_AMOUNT)

        # Очистка экрана
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

except KeyboardInterrupt:
    print('\nRotating Cube (c) Al Sweigart\n')
    sys.exit()
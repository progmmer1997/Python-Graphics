from graph import *

canvasSize(700, 500)
windowSize(800, 600)


# Функция определения шагов перемещения (dx и dy)
#        при нажатии на клавиши – стрелки или клавишу пробел
# Функция закрывает окно при нажатии на клавишу ESC

def keyPressed(event):
    global dx, dy
    if event.keycode == VK_LEFT:
        dx = -5
        dy = 0
    elif event.keycode == VK_RIGHT:
        dx = 5
        dy = 0
    elif event.keycode == VK_UP:
        dx = 0
        dy = -5
    elif event.keycode == VK_DOWN:
        dx = 0
        dy = 5
    elif event.keycode == VK_SPACE:
        dx = dy = 0

    elif event.keycode == VK_ESCAPE:
        close()


# Функция перемещения объектов

def update():
    moveObjectBy(block, dx, dy)
    moveObjectBy(r_s, dx, dy)
    moveObjectBy(y_s, dx, dy)
    moveObjectBy(g_s, dx, dy)


# Функция проверки выхода фигуры за край поля
def end():
    if 0 > min(coords(block)) or 600 < max(coords(block)):
        print('Светофор вышел за границы поля')
        close()


# Основная программа
x = 200
y = 190
penColor("grey")
penSize(2)
block = rectangle(100, 100, 300, 300)
changeFillColor(block, 'black')
r_s = circle(x, y, 15)
changeFillColor(r_s, "red")
y_s = circle(x, y + 40, 15)
changeFillColor(y_s, "yellow")
g_s = circle(x, y + 80, 15)
changeFillColor(g_s, "green")

# Устанавливаем толщину и цвет пера
penColor("grey")

# Определяем начальное положение фигур
x = 550
y = 200

# Задаем нулевые значения шагов изменения координат
dx = 0
dy = 0

# Выполняем функцию как обработчик нажатия клавиш keyPressed
onKey(keyPressed)

# Определяем функции update и end ,
# которые будет вызываться по таймеру каждые 50 миллисекунд
onTimer(update, 50)
onTimer(end, 50)

run()

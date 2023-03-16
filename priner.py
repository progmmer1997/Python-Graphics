from graph import *
canvasSize (700, 500)
windowSize (800, 600)

# Функция определения шагов перемещения (dx и dy) 
#        при нажатии на клавиши – стрелки или клавишу пробел
# Функция закрывает окно при нажатии на клавишу ESC

def keyPressed (event):

    global dx, dy
    if event.keycode == VK_LEFT:
        dx = -5; dy = 0
    elif event.keycode == VK_RIGHT:
        dx = 5; dy = 0
    elif event.keycode == VK_UP:
        dx = 0; dy = -5
    elif event.keycode == VK_DOWN:
        dx = 0; dy = 5
    elif event.keycode == VK_SPACE:
        dx = dy = 0
    elif event.keycode == VK_ESCAPE:
        close()

# Функция перемещения объектов

def update():

    moveObjectBy(shar, dx, dy)
    moveObjectBy(linia, dx, dy)

# Функция проверки выхода фигуры за край поля 

def end():

    if 0>min (coords(shar)) or 600<max(coords(shar)):
        print ('Шарик улетел')
        close()

#Основная программа

penColor("grey")
penSize(2)
brushColor("white")
rectangle(80, 100, 300, 150)
brushColor("blue")
rectangle(80, 150, 300, 200)
brushColor("red")
rectangle(80, 200, 300, 250)

# Определяем начальное положение фигур 
x = 550; y = 200

# Задаем нулевые значения шагов изменения координат   
dx = 0;	dy = 0

brushColor("yellow")

# Определяем объекты для анимации 
shar = circle(x, y, 30)
linia = line(x-50, y+100, x-10, y+20)

# Выполняем функцию как обработчик нажатия клавиш keyPressed 
onKey (keyPressed)

# Определяем функции update и end ,  
#       которые будет вызываться по таймеру каждые 50 миллисекунд 
onTimer (update, 50)
onTimer (end, 50)

run()

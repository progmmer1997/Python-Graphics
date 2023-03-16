from graph import *

# Устанавливаем толщину и цвет пера
x=200
y=190
penColor ("grey")
penSize (2)
block=rectangle(100,100,300,300)
changeFillColor(block,'black')
r_s=circle (x, y, 15)
changeFillColor(r_s,"red")
y_s=circle (x, y+40, 15)
changeFillColor(y_s,"yellow")
g_s=circle (x, y+80, 15)
changeFillColor(g_s,"green")


run()

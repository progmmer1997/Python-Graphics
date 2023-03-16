from graph import *   
windowSize(800,600)
canvasSize (700, 500)

# Устанавливаем толщину и цвет пера
penColor ("grey")
penSize (2) 

# Устанавливаем цвета заливки и 
# рисуем прямоугольники с координатами протволежащих углов
roof=canvas().create_polygon(100,100,200,50,300,100)
changeFillColor(roof,"red")
coords(roof)
home=rectangle(100,100,300,300)
changeFillColor(home,"yellow")

w1=circle(200,220,30)

# Устанавливаем толщину и цвет пера
penColor ("grey")
print("ljv",coords(home))
print("ropf",coords(roof))

#ljv (99, 99, 401, 401)
#ropf (99, 49, 301, 101)


# Запускаем основной цикл обработки сообщений
run()


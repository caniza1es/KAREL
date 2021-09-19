import turtle

#iniciando ventana
ventana = turtle.Screen()
ventana.setup(1000,1000)

#ancho=30

karel = turtle.Turtle()
karel.speed(1000)

karel.up()
karel.sety(-450)
karel.down()

#Funcion para dibujar las lineas horizontales
def lineaHorizontal(grid,numlinea):
  grid.penup()
  grid.setx(-450)
  grid.down()
  grid.write(numlinea)
  grid.setx(450)

#Funcion para dibujar las lineas verticales
def lineaVertical(grid,num2linea):
  grid.penup()
  grid.sety(-450)
  grid.down()
  if num2linea==30:
    pass
  else:
    grid.write(num2linea)
  grid.sety(450)

#Se hace la gráfica
contadorHorizontal = 0
y=-450
while contadorHorizontal != 31:
  lineaHorizontal(karel,contadorHorizontal)
  y+=30
  karel.up()
  karel.sety(y)
  karel.down()
  contadorHorizontal+=1

karel.up()
karel.goto(-450,-450)
karel.down()

contadorVertical = 0
x=-450
while contadorVertical != 31:
  lineaVertical(karel,contadorVertical)
  x+=30
  karel.up()
  karel.setx(x)
  karel.down()
  contadorVertical+=1

#Karel se devulve a la posición inicial para comenzar con el dibujo del mapa
karel.up()
karel.goto(-450,-450)
karel.down()


#funcion para darle coordenadas a karel con coordenadas del pllano cartesiano
def coordenadas(x,y,ka):
  ka.up()
  cordx=-450+(x*30)
  cordy=-450+(y*30)
  ka.goto(cordx,cordy)
  ka.down()

coordenadas(15,4,karel)

turtle.done()
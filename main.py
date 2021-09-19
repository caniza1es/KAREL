import turtle
#iniciando ventana
turtle.Screen()
turtle.title("KAREL")
turtle.setup(1000,1000)

#ancho=30
karel = turtle.Turtle()
karel.speed(0)
karel.sety(-450)

#Funcion para lineas horizontales/Verticales
def hacerLinea(grid,numlinea,modo):
  grid.pd()
  if modo == 'h': 
   grid.setx(-450)
   grid.write(numlinea)
   grid.setx(450)
  else:
   grid.sety(-450)
   grid.write(numlinea)
   grid.sety(450)
#Hacer lineas horizontales
contadorLi = 0
while contadorLi != 31:
  hacerLinea(karel,contadorLi,'h')
  karel.up()
  karel.sety(karel.ycor()+30)
  contadorLi+=1

#Karel vuelve a la posicion inicial
karel.goto(-450,-450)

#Hacer lineas verticales
contadorLi = 0
while contadorLi != 31:
  hacerLinea(karel,contadorLi,"")
  karel.up()
  karel.setx(karel.xcor()+30)
  contadorLi+=1

#funcion para ubicar a objetos con coordenadas del plano cartesiano
def coordenadas(x,y,ka):
  ka.goto(-450+(x*30),-450+(y*30))

coordenadas(15,15,karel)
turtle.done()
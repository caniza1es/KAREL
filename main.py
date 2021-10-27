import turtle
import lector
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

#funcion que ejecuta las intrucciones
def archivo_ejecucion(instruccion):
    if instruccion == "move;":
        karel.forward(30)
        for i in paredes:
          if  round(karel.xcor()) == round(i.turtlee.xcor()) and round(karel.ycor()) == round(i.turtlee.ycor()):
            print("karel ha chocado")
            return -1
    elif instruccion == "turnleft;":
        karel.left(90)
    elif instruccion in definiciones:
        for nLine in program[definiciones[definiciones.index(instruccion)+1]:definiciones[definiciones.index(instruccion)+2]]:
            archivo_ejecucion(nLine)
    elif instruccion == "pickbeeper;":
      for i in beepers:
        if round(karel.xcor()) == round(i.turtlee.xcor()) and round(karel.ycor()) == round(i.turtlee.ycor()):
          global mochila
          mochila += 1
          lector.coordenadas(-1, -1, i.turtlee)
          return
      print("no hay beepers que recoger")
      return -1
    elif instruccion == "putbeeper;":
      if mochila>0:
         for i in beepers:
             if i.turtlee.xcor() == -480:
                 i.turtlee.goto(karel.xcor(),karel.ycor())
                 mochila-=1
                 break;
      else:
        print("No tiene beepers para poner.")
        return -1

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

paredes = []
beepers = []
while True:
 try: 
   print("mapa:")
   pInicial = lector.parametros(paredes,beepers,karel)
   print("\n")
   break;
 except:
   print("error al cargar mapa")
   print("\n")
mochila = pInicial[2]
posxinicial = pInicial[0]
posyinicial = pInicial[1]

#se empieza a leer el programa
while True:
  mochila = pInicial[2]
  lector.coordenadas(posxinicial,posyinicial,karel)
  karel.seth(0)
  karel.speed(1)
  karel.color("red")
  karel.down()
  for i in beepers:
      lector.coordenadas(i.x, i.y, i.turtlee)
         
  try:
        print("codigo")
        program = lector.archivo_a_lista()
        print("\n")
        #se revisa PROGRAM
        if program[0] != "BEGINNING-OF-PROGRAM" or program[-1] != "END-OF-PROGRAM":
         print("error en programa")
        #se revisa EXECUTION junto a nuevas definiciones
        try:
            definiciones = lector.archivo_definiciones(program)
            if definiciones is None:
                "vuelve a pedir el archivo"
            else:
                try:#inicia la ejecucion, en caso de error es porque no logra indexar el turnoff
                   for linee in program[program.index("BEGINNING-OF-EXECUTION"):program.index("turnoff")]:
                       turnoff = archivo_ejecucion(linee)
                       if turnoff == -1:
                         break;
                   karel.up()
                   a = input("presione cualquier tecla para volver a parametros de lanzamiento")
                except:
                    print("error en turnoff")
        except:
            print("error en EXECUTION")
  except:
    print("saliendo..")
    exit()
        
turtle.done()
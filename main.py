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

karel.up()
paredes = []
paredesVerticales = lector.pedirParedesV()
for i in range(paredesVerticales):
  x = int(input("corx: "))
  y = int(input("cory: "))
  size = int(input("tamaño: "))
  for unidad in range(size):
    pared = lector.Beepers(x,y)
    pared.turtlee.color("black")
    paredes.append(pared)
    coordenadas(x,y,pared.turtlee)
    y+=1

paredesHorizontales = lector.pedirParedesH()
for i in range(paredesHorizontales):
  x = int(input("corx: "))
  y = int(input("cory: "))
  size = int(input("tamaño: "))
  for unidad in range(size):
    pared = lector.Beepers(x,y)
    pared.turtlee.color("black")
    paredes.append(pared)
    coordenadas(x,y,pared.turtlee)
    x+=1
beepers = []
numeroBeepers = lector.pedirBeepers()
for i in range(numeroBeepers):
  x = int(input("corx: "))
  y = int(input("cory: "))
  beep = lector.Beepers(x,y)
  beep.turtlee.speed(3)
  beepers.append(beep)
  coordenadas(x,y,beepers[i].turtlee)
  
mochila = int(input("beepers en mochila: "))
temp = mochila
for i in range(mochila):
  beep = lector.Beepers(-1, -1)
  beep.turtlee.speed(3)
  coordenadas(beep.x, beep.y, beep.turtlee)
  beepers.append(beep)



#funcion que ejecuta las intrucciones
def archivo_ejecucion(instruccion):
    if instruccion == "move;":
        karel.forward(30)
        for i in paredes:
          if  int(karel.xcor()) == i.turtlee.xcor() and int(karel.ycor()) == i.turtlee.ycor():
            print("karel ha chocado")
            return -1
    elif instruccion == "turnleft;":
        karel.left(90)
    elif instruccion in definiciones:
        for nLine in program[definiciones[definiciones.index(instruccion)+1]:definiciones[definiciones.index(instruccion)+2]]:
            archivo_ejecucion(nLine)
    elif instruccion == "pickbeeper;":
      for i in beepers:
        if int(karel.xcor()) == i.turtlee.xcor() and int(karel.ycor()) == i.turtlee.ycor():
          global mochila
          mochila += 1
          coordenadas(-1, -1, i.turtlee)
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


posxinicial = int(input("posicion x inicial: "))
posyinicial = int(input("pos y inicial: "))


#se empieza a leer el programa
while True:
  mochila = temp
  coordenadas(posxinicial,posyinicial,karel)
  karel.seth(0)
  karel.speed(1)
  karel.color("red")
  karel.down()
  for i in beepers:
      coordenadas(i.x, i.y, i.turtlee)
         
  try:
        program = lector.archivo_a_lista()
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
        print("No se encontro el archivo-saliendo.")
        exit()
        break
        
turtle.done()
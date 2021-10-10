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
def sacar_las_coordenadas(x,y):
  return (x,y)
def coordenadas(x,y,ka):
  ka.goto(-450+(x*30),-450+(y*30))

karel.up()
mochila = int(input("beepers en mochila: "))
temp = mochila
numeroBeepers = lector.pedirBeepers()
beepers = []
for i in range(numeroBeepers):
  x = int(input("corx: "))
  y = int(input("cory: "))
  beep = lector.Beepers(x,y)
  beepers.append(beep)
  coordenadas(x,y,beepers[i].turtlee)

#funcion que ejecuta las intrucciones
def archivo_ejecucion(instruccion):
    if instruccion == "move;":
        karel.forward(30)
    elif instruccion == "turnleft;":
        karel.left(90)
    elif instruccion in definiciones:
        for nLine in program[definiciones[definiciones.index(instruccion)+1]:definiciones[definiciones.index(instruccion)+2]]:
            archivo_ejecucion(nLine)
    elif instruccion == "pickbeeper;":
      #cx=karel.corx()
      #cy=karel.cory()
      for i in beepers:
        if karel.xcor() == i.turtlee.xcor() and karel.ycor() == i.turtlee.ycor() and i.turtlee.isvisible():
          global mochila
          mochila += 1
          i.turtlee.hideturtle()
          break;
    elif instruccion == "putbeeper;":
      if mochila>0:
        beeperPuesto = lector.Beepers(karel.xcor(),karel.ycor())
        beeperPuesto.turtlee.ht()
        beeperPuesto.turtlee.setx(karel.xcor())
        beeperPuesto.turtlee.sety(karel.ycor())
        beeperPuesto.turtlee.st()
        beeperPuesto.turtlee.shape("square")
        beeperPuesto.turtlee.color("green")
        beepers.append(beeperPuesto)
        mochila-=1
      else:
        print("No tiene beepers para poner.")
        #turnoff


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
                       archivo_ejecucion(linee)
                   karel.up()
                   a = input("")
                   
                except:
                    print("error en turnoff")
        except:
            print("error en EXECUTION")
  except:
        print("No se encontro el archivo-saliendo.")
        exit()
        break
        
turtle.done()
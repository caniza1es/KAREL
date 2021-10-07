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
  
coordenadas(20,20,karel)
karel.speed(1)
karel.color("red")
karel.down()
  
#funcion que ejecuta las intrucciones
def archivo_ejecucion(instruccion):
    if instruccion == "move;":
        karel.forward(90)
    elif instruccion == "turnleft;":
        karel.left(90)
    elif instruccion in definiciones:
        for nLine in program[definiciones[definiciones.index(instruccion)+1]:definiciones[definiciones.index(instruccion)+2]]:
            archivo_ejecucion(nLine)

#se empieza a leer el programa
while True:
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
                except:
                    print("error en turnoff")
        except:
            print("error en EXECUTION")
    except:
        print("No se encontro el archivo-saliendo.")
        exit()
        break
        
#ejecucion instruccion


turtle.done()
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
turtle.tracer(0)

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
def archivo_ejecucion(instruc):
    funciones = ["ITERATE","IF","WHILE"]
    instruccion = instruc.split()[0]
    if instruccion == "move;":
        karel.forward(30)
        for i in paredes:
          if  round(karel.xcor()) == round(i.turtlee.xcor()) and round(karel.ycor()) == round(i.turtlee.ycor()):
            print("karel ha chocado")
            karel.penup()
            return -1
    elif instruccion == "turnleft;":
        karel.left(90)
    elif instruccion in definiciones:
        ejecutar(indices[definiciones[definiciones.index(instruccion)+1]:definiciones[definiciones.index(instruccion)+2]])
    elif instruccion == "pickbeeper;":
      for i in beepers:
        if round(karel.xcor()) == round(i.turtlee.xcor()) and round(karel.ycor()) == round(i.turtlee.ycor()):
          global mochila
          mochila += 1
          lector.coordenadas(-1, -1, i.turtlee)
          return 0
      print("no hay beepers que recoger")
      return -1
    elif instruccion == "putbeeper;":
      if mochila>0:
         for i in beepers:
             if i.turtlee.xcor() == -480:
                 i.turtlee.goto(karel.xcor(),karel.ycor())
                 mochila-=1
                 break
      else:
        print("No tiene beepers para poner.")
        return -1
    elif instruccion in funciones:
      return anidar(instruc,funciones)
    elif instruccion == "END":
      return 0
    else:
      print(instruccion,"no es conocida")
      return -1
    return 0

def ejecutar(programa):
  t = 0
  for i in programa:
    if t > 0:
      t-=1
      continue
    print(i)
    t = archivo_ejecucion(i)
    if t == -1:
       return t
def conditional(mode):
   head = karel.heading()
   y = 0
   x = 0
   if mode == "front-is-blocked" or mode == "front-is-clear":
     if head == 0.0:
       x = 30
     elif head == 90.0:
       y = 30
     elif head == 180.0:
       x = -30
     elif head == 270.0:
       y = -30
   elif mode == "left-is-blocked" or mode == "left-is-clear":
     if head == 0.0:
       y = 30
     elif head == 90.0:
       x = -30
     elif head == 180.0:
       y = -30
     elif head == 270.0:
       x = 30
   elif mode == "right-is-blocked" or mode == "right-is-clear":
     if head == 0.0:
       y = -30
     elif head == 90.0:
       x = 30
     elif head == 180.0:
       y = 30
     elif head == 270.0:
       x = -30
   elif mode == "beepers-in-bag":
     if mochila>0:
       return True
     else:
       return False
   elif mode == "facing-north":
     if head == 90.0:
       return True
     return False
   elif mode == "facing-east":
     if head == 0.0:
       return True
     return False
   elif mode == "facing-west":
     if head == 180.0:
       return True
     return False
   elif mode == "facing-south":
     if head == 270.0:
       return True
     else:
       return False
   elif mode == "not-facing-north":
     if head == 90.0:
       return False
     return True
   elif mode == "not-facing-east":
     if head == 0.0:
       return False
     return True
   elif mode == "not-facing-west":
     if head == 180.0:
       return False
     return True
   elif mode == "not-facing-south":
     if head == 270:
       return False
     return True
   elif mode == "beeper-near":
     for i in beepers:
        if round(karel.xcor()) == round(i.turtlee.xcor()) and round(karel.ycor()) == round(i.turtlee.ycor()):
            return True
     return False
   if mode.split("-")[2] == "blocked":
     for i in paredes:
       if  round(karel.xcor()+x) == round(i.turtlee.xcor()) and round(karel.ycor()+y) == round(i.turtlee.ycor()):
         return True
     return False
   elif mode.split("-")[2] == "clear":
     for i in paredes:
       if  round(karel.xcor()+x) == round(i.turtlee.xcor()) and round(karel.ycor()+y) == round(i.turtlee.ycor()):
         return False
     return True
         

def anidar(inst,funcs):
  inicio = [int(inst.split()[-1])+1]
  final = []
  count = int(inst.split()[-1])+1
  while len(inicio) != len(final):
    if indices[count].split()[0] == "END":
      final.append(count)
    elif indices[count].split()[0] in funcs:
      inicio.append(count+1)
    count+=1
  if inst.split()[0] == "ITERATE":
    iterator = int(inst.split()[1])
    for j in range(iterator):
      t = ejecutar(indices[inicio[0]:final[-1]])
      if t == -1:
        return t
  elif inst.split()[0] == "IF":
    if conditional(inst.split()[1]):
      t = ejecutar(indices[inicio[0]:final[-1]])
      if t == -1:
        return t
  elif inst.split()[0] == "WHILE":
    while conditional(inst.split()[1]):
      t = ejecutar(indices[inicio[0]:final[-1]])
      if t == -1:
        return t 

  return final[-1]-inicio[0]

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

turtle.tracer(1)
while True:
 paredes = []
 beepers = []
 while True:
  try: 
    print("mapa:")
    turtle.tracer(0)
    pInicial = lector.parametros(paredes,beepers,karel)
    turtle.tracer(1)
    print("\n")
    break
  except:
    print("error al cargar mapa")
    print("\n")
 mochila = pInicial[2]
 posxinicial = pInicial[0]
 posyinicial = pInicial[1]
 #se empieza a leer el programa
 while True:
  mochila = pInicial[2]
  turtle.tracer(0)
  lector.coordenadas(posxinicial,posyinicial,karel)
  karel.seth(0)
  karel.speed(1)
  karel.down()
  turtle.tracer(1)
  for i in beepers:
      lector.coordenadas(i.x, i.y, i.turtlee)
  try:
        print("codigo")
        program = lector.archivo_a_lista()
        indices = lector.archivo_a_indices(program)
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
                   turnoff = ejecutar(indices[program.index("BEGINNING-OF-EXECUTION")+1:program.index("turnoff")])
                   karel.up()
                   a = input("presione cualquier tecla para volver a parametros de lanzamiento")
                except:
                    print("error en turnoff")
        except:
            print("error en EXECUTION")
  except:
    print("volviendo a mapa..")
    turtle.tracer(0)
    for i in paredes:
      i.turtlee.ht()
      del i
    for i in beepers:
      i.turtlee.ht()
      del i
    turtle.tracer(1)
    break
        
turtle.done()
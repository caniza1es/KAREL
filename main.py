import turtle

karel = turtle.Turtle()
programa = ["BEGINNING-OF-PROGRAM","turnleft;","move;","putbeeper;","move;"]

if programa[0] != "BEGINNING-OF-PROGRAMA":
  exit()

def exeInstruct(instruct):
  if instruct == "turnleft;":
    karel.left(90)
  elif instruct == "move;":
    karel.forward(50)
  elif instruct == "putbeeper;":
    karel.stamp()
  
#para crear el mapa
def grid(lineas, columnas):
  x=int(input("Ingrese la cantidad de lineas verticales quiere en su mapa: "))
  y=int(inp)




for i in programa:
  exeInstruct(i)


turtle.done()
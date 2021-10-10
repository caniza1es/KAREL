beepers={}
paredes=[] #lista de tuplas. Se tiene encuenta los extremos de las paredes

def poner_beeper(x,y,karel):
  karel.up()
  coordenadas(x,y,karel)
  stampid=karel.stamp()
  cord=sacar_las_coordenadas(x,y)
  beepers[cord]=stampid

def recoger_beeper(x,y,karel):
  cordenada_karel=(karel.corx(),karel.cory())
  if coordenada_karel in beepers.keys():
    karel.clearstamp(beepers[coordenada_karel])
    del beepers(coordenada_karel)
  else:
    pass
    #turnoff

def hacer_paredes(karel):
  karel.up()

  px=int(input("Ingrese la coordenada en x de donde quiere empezar su pared: "))
  py=int(input("Ingrese la coordenada en y de donde quiere empezar su pared: "))

  print("")

  karel.goto(px,py)

def chocar_con_pared(karel):
  


num_beepers=int(input("Ingrese la cantidad de beepers que quiere adicionar: "))

for y in range(num_beepers):
  beepx = int(input("Ingrese la coordenada en x del beeper: "))
  beepy = int(input("Ingrese la coordenada en y del beeper: "))
  poner_beeper(beepx, beepy, karel)


import turtle
class Objetos:
  def __init__(self,x,y,color):
    self.x = x
    self.y = y
    self.turtlee = turtle.Turtle()
    self.turtlee.shape("square")
    self.turtlee.color(color)
    self.turtlee.up()

#funcion para ubicar a objetos con coordenadas del plano cartesiano
def coordenadas(x,y,ka):
  ka.goto(-450+(x*30),-450+(y*30))

def parametros(pa_lista,be_lista,ka):
  map = archivo_a_lista()
  mochilaa = 0
  for i in map:
    par = i.split()
    if par[0] == "paredVertical" or par[0] == "paredHorizont":
      x = int(par[1])
      y = int(par[2])
      for unidad in range(int(par[3])):
        try:
          obj = Objetos(x,y,par[4])
        except:
          obj = Objetos(x,y,"black")
        obj.turtlee.speed(0)
        pa_lista.append(obj)
        coordenadas(x,y,obj.turtlee)
        if par[0] == "paredVertical":
          y+=1
        else:
          x+=1
    elif par[0] == "beeper":
      x = int(par[1])
      y = int(par[2])
      try:
        beep = Objetos(x,y,par[3])
      except:
        beep = Objetos(x,y,"green")
      beep.turtlee.speed(0)
      be_lista.append(beep)
      coordenadas(x,y,beep.turtlee)
    elif par[0] == "mochila":
      mochilaa = int(par[1])
      for i in range(mochilaa):
        try:
          beep = Objetos(-1,-1,par[2])
        except:
          beep = Objetos(-1,-1,"green")
        beep.turtlee.speed(0)
        be_lista.append(beep)
        coordenadas(-1,-1,beep.turtlee)
    elif par[0] == "karel":
      try:
        ka.color(par[3])
      except:
        ka.color("red")
      coordenadas(int(par[1]),int(par[2]),ka)
      return (int(par[1]),int(par[2]),mochilaa)
    else:
      return (15,15,mochilaa)

def archivo_a_lista():
	#convierte el archivo a una lista de strings sin espacios
	nombre = input("digite nombre archivo(junto a extension): ")
	archivo = open(nombre, "r")
	programa = []
	for line in archivo:
		programa.append(line.strip())
	archivo.close()
	return programa

def archivo_a_indices(programa):
  indices = []
  for i in range(len(programa)):
    msn = programa[i] + " " + "{0}".format(i)
    indices.append(msn)
  return indices


def archivo_definiciones(programa):
	definiciones = []  #lista en la que se guarda la instruccion junto al indice donde comeinza/termina
	for nInstruct in programa[1:programa.index("BEGINNING-OF-EXECUTION")]:  #si no se logra indexar carga el except en main
		if nInstruct.split()[0] == "DEFINE-NEW-INSTRUCTION" and nInstruct.split()[2] == "AS":  #en  caso de que no se cumpla la igualdad simplemente seguira derecho
			definiciones.append(nInstruct.split()[1] + ";")  #toma la posicion donde deberia estar la instruccion y la pasa a la lista junto ";"
			definiciones.append(programa.index(nInstruct) + 1)  #añade el inicio de la instruccion al lado del indice que guarda el nombre
			finDef = programa.index(nInstruct) + 1
			try:  #en caso de que no se encuntre end muestra error
				while programa[finDef] != "END;":
					finDef += 1
				if finDef in definiciones:
					print("error en ", nInstruct)
					return
				definiciones.append(finDef)  #añade el final de la instruccion al lado del indice que guarda el inicio de esta
			except:
				print("error en ", nInstruct)
				return
	return definiciones  #retorna la lista
	#para el uso se debe indexar la isntruccion en la lista de definiciones y sumarle 1 o 2 a este indice para acceder a los indices de su inicio o fin

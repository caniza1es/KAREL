def leer(linea):
  funcs = ["ITERATE","IF","WHILE"]
  if linea.split()[0] == "move;":
    print("moved")
  elif linea.split()[0] == "turn;":
    print("turned")
  elif linea.split()[0] in funcs:
    return anidar(linea,funcs)
  return 0

def anidar(inst,funcs):
  inicio = [int(inst.split()[-1])+1]
  final = []
  count = int(inst.split()[-1])+1
  while len(inicio) != len(final):
    if program[count].split()[0] == "END":
      final.append(count)
    elif program[count].split()[0] in funcs:
      inicio.append(count+1)
    count+=1
  if inst.split()[0] == "ITERATE":
    iterator = int(inst.split()[1])
    for j in range(iterator):
      ejecutar(program[inicio[0]:final[-1]])
      
  return final[-1]-inicio[0]
    
def interpretar(lista):
  for i in range(len(lista)):
    lista[i]+=" "+"{0}".format(i)
    
def ejecutar(lista):
  t = 0
  for i in lista:
    if t > 0:
      t -=1
      continue
    t = leer(i)
program = ["ITERATE 4 TIMES","ITERATE 4 TIMES","turn;","END","move;","END","move;"]
interpretar(program)
ejecutar(program)
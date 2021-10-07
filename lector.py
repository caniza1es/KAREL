def archivo_a_lista():
    #convierte el archivo a una lista de strings sin espacios
    nombre = input("digite nombre archivo/cualquier otra cosa para salir(junto a extension): ")
    archivo = open(nombre,"r")
    programa = []
    for line in archivo:
        programa.append(line.strip())
    archivo.close()
    return programa

def archivo_definiciones(programa):
    definiciones = []#lista en la que se guarda la instruccion junto al indice donde comeinza/termina
    for nInstruct in programa[1:programa.index("BEGINNING-OF-EXECUTION")]:#si no se logra indexar carga el except en main
          if nInstruct.split()[0] == "DEFINE-NEW-INSTRUCTION" and nInstruct.split()[2]=="AS":#en  caso de que no se cumpla la igualdad simplemente seguira derecho
              definiciones.append(nInstruct.split()[1]+";") #toma la posicion donde deberia estar la instruccion y la pasa a la lista junto ";"
              definiciones.append(programa.index(nInstruct)+1)#añade el inicio de la instruccion al lado del indice que guarda el nombre
              finDef = programa.index(nInstruct) + 1
              try:#en caso de que no se encuntre end muestra error
               while programa[finDef] != "END;":
                   finDef+=1
               if finDef in definiciones:
                   print("error en ",nInstruct)
                   return
               definiciones.append(finDef)#añade el final de la instruccion al lado del indice que guarda el inicio de esta
              except:
                  print("error en ",nInstruct)
                  return
    return definiciones#retorna la lista
    #para el uso se debe indexar la isntruccion en la lista de definiciones y sumarle 1 o 2 a este indice para acceder a los indices de su inicio o fin
    

# KAREL
interprete de Karel

#CREACION DE MAPAS
1. Para crear un mapa debe escribir en un archivo de texto diferente al de su codigo los parametros de lanzamiento 
   que quiere como se indica a continuacion.
   
   paredVertical x y z  -le indica al programa que debe crear una pared vertical en la pos (x,y) de tamaño z
   paredHorizont x y z  -le indica al programa que debe crear una pared horizontal en la pos(x,y) de tamaño z
   beeper x y           -le indica al programa que debe crear un beeper en la pos(x,y)
   mochila x            -le indica al programa la mochila de karel tiene x beepers en el inventario
   karel x y            -le indica al programa la pos inicial de karel en la pos(x,y)
   
   anotaciones:
   -el archivo de mapa siempre debe terminar indicando karel x y, en caso de que no se quiere cargar un mapa, simplemente digite el archivo de codigo karel
   -todas las instrucciones en el mapa pueden tener un parametro adicional que indique el color de dicho objeto. ej:
                                     
                                       paredVertical 15 16 4 blue
                                       beeper 12 13 yellow
                                       mochila 5 orange
                                       karel 2 3 cyan
   
   -pueden haber espacios pero no lineas en blanco

#CODIGO DE KAREL

instrucciones nativas:

move; -mueve a karel hacia donde este apuntando, en caso de chocarse con pared hay turnoff
turnleft; -gira a karel 90 grados a la izquierda
pickbeeper; -recoge un beeper si hay en su pos, de lo contrario hay turnoff
putbeeper;   -toma un beeper de la mochila y lo pone en la posicion de karel, en caso de mochila vacia hay turnoff


1. Su codigo debe empezar por "BEGINNING-OF-PROGRAM" y terminar en "END-OF-PROGRAM"
2. Para definir nuevas instrucciones, debe usar "DEFINE-NEW-INSTRUCTION nombreinstruccion AS" en las lineas posteriores indicar las instrucciones nativas
   o definiciones, un vez hecho eso, indique el fin de la definicion en una nueva linea con "END;"
3. Para indicar la seccion principal del programa, debe usar "BEGINNING-OF-EXECUTION" y terminarlo con "END-OF-EXECUTION"
4. Para indicar las instrucciones a leer, haga uso de las instrucciones nativas dentro de EXECUTION o llame una definicion con nombreinstruccion;
5.Una vez se haya terminado de llamar todas las instrucciones para su codigo en EXECUTION, debe usar "turnoff"

CODIGO EJEMPLO

                                    BEGINNING-OF-PROGRAM
                                    DEFINE-NEW-INSTRUCTION turnright AS
                                    turnleft;
                                    turnleft;
                                    turnleft;
                                    END;
                                    DEFINE-NEW-INSTRUCTION square AS
                                    ITERATE 4 TIMES
                                    turnright;
                                    move;
                                    END
                                    END;
                                    BEGINNING-OF-EXECUTION
                                    square;
                                    move;
                                    turnoff
                                    END-OF-EXECUTION
                                    END-OF-PROGRAM


ITERADOR: 

                                    ITERATE x times 
                                    bloque instrucciones
                                    END
          
-itera x veces el bloque de instrucciones

statements:

front-is-blocked --- front-is-clear       
right...                                                      
left...                                                       
                                                              
beepers-in-bag
beeper-near

facing-north --- not-facing-north
      -east...
      -west...
      -south...
      
                                                     

CONDICIONAL:

                                    IF statement          
                                    bloque instrucciones
                                    END
       
-en caso de que el statement se cumpla, se ejecuta el bloque de instrucciones

BUCLE CONDICIONADO: 

                                   WHILE statement      
                                   bloque instrucciones
                                   end
                                   
-mientras que el statement se cumpla, el bloque de instrucciones se ejecuta
                                                             

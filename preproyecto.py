
#variables
lista_de_articulos = []

salir = False
opcion = 0 


#funciones
def validarIngreso():
   n = input("Ingrese precio: ")
   if( n.isdigit()):
     return n
   else: return None
#bucle principal
while not (salir) :
 print(" =======MENU DE OPCIONES=======")
 print(" |1. INGRESE UN PRODUCTO")
 print(" |2. VER PRODUCTOS INGRESADOS")
 print(" |3. BUSCAR PRODUCTO(x nombre)")
 print(" |4. ELIMINAR UN PRODUCTO")
 print(" |5. SALIR")
 print(" ==============================")
 opcion = input("Ingrese una opcion->")
 if(opcion.isdigit()):
  opcion = int(opcion)
  if opcion < 6 and opcion > 0:
      match opcion:
        case 1:
          
          nombre = input("Ingrese el nombre: ") 
          categoria = input("Ingrese la categoria:")
          precio = validarIngreso()
          if(precio is None):
            print("El precio ingresado debe ser un numero")
            continue
          else:
            lista_de_articulos.append((nombre,categoria,precio))
          
        case 2:
            print("====PRODUCTOS EN LISTA====")
            for i in range(len( lista_de_articulos)):
              nombre,categoria,precio = lista_de_articulos[i]
              print(f"Indice: {i} Nombre: {nombre} Categoria: {categoria} Precio: {precio}")                    
        case 3:
            print("===BUSCAR UN PRODUCTO POR NOMBRE===")
            nombrebuscado = input("Ingrese el nombre del producto:") 
            
            nombrebuscado = nombrebuscado.strip().lower();
            resultado = []

            for nombre,categoria,precio in lista_de_articulos:       
              nombre = nombre.strip().lower()
              if( nombrebuscado in nombre):
                nuevo = (nombre,categoria,precio)
                resultado.append(nuevo)
              
            tam = len(resultado)
            if(tam >0 ):
             print(f"Se encontraron {tam} coincidencias")  
             print(resultado)  
            elif(tam == 0):                
                print("No se encontro el producto")  
        case 4:
            print("===ELIMINAR UN PRODUCTO===")
            resutado = []
            indicebuscado = input("Ingrese el indice del producto: ")
            if(indicebuscado.isdigit()):
              indicebuscado = int(indicebuscado)
              if( indicebuscado > len(lista_de_articulos)):
                print("No existe el indice de articulo")
              elif(indicebuscado >-1 and indicebuscado < len(lista_de_articulos)) :         
                lista_de_articulos.pop(indicebuscado)
                print("Producto eliminado")
                  
        case 5: salir=True

  else: print("Ingrese una opcion valida!(1 al 5)") 
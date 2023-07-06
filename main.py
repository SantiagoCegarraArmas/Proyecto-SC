from endpoint import *
from registrarproductos import *
from registrarcleintes import *
from gestionventas import *
from guardartxt import *

def main():

  endpoint = endpointjson()
  db = {"productos":{ },"Clientes":{ },"Ventas":{ }}
  db = recive_data_text("base.txt", db)
  db = productos(endpoint,db)
  
  print(db)
  
  while True:
    
    print("""
    Bienvenido a Zanahoria shopping.
    Indique lo que desea hacer:
    1. Gestionar productos
    2. Gestionar ventas
    3. Gestionar clientes
    4. Gestionar pagos
    5. Gestionar envíos
    6. Indicadores de gestión (estadísticas)
    7. Salir 
    """)
    while True:
      try:
        option = int(input("--->"))
        if option not in range(1,8):
           raise Exception 
        break
      except:
        print("Ingrese una opción válida (1-7)")
  

    if option == 1:
      menuproductos(db)
      load_data_txt("base.txt", db)
    elif option == 2:
      menuventas(db)
      load_data_txt("base.txt", db)
    elif option == 3:
      menuClientes(db)
      load_data_txt("base.txt", db)
    elif option == 4:
      pass
    elif option == 5:
      menuenvios(db)
      load_data_txt("base.txt", db)
    elif option == 6:
      pass
    else:
      print("Gracias por preferirnos. Hasta luego.")
     
      break
    
      
    






main()   
    
  

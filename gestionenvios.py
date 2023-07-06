from Envios import *



def menuenvios(db):
  def menuventas(db):
    print("""
    Que desea realizar
    1.Registrar Envío
    2.Buscar Envíos
    3.Regresar
    """)
    while True:
      try:
        option = int(input("--->"))
        if option not in range(1, 5):
          raise Exception
        break
      except:
        print("Ingrese una opción válida (1-4)")
  
      if option == "1":
        db = registrarenvio(db)
      elif option == 2:
        buscarenvío(db)
      else:
        break

def registrarenvio(db):
  MotorizadoDatos={ }
  
  print(
    "A continuación deberá ingresar los datos del envio que desea agregar al sistema."
  )
  order = input("Indique el número de orden del envío ")
  while True:
    serenvio = input("Indique el servicio de envío deseado (MRW, Zoom, Delivery.):  ")
    if serenvio== "MRW":
      metodoenvio = "MRW"
      break
    if serenvio == "ZOOM":
      metodoenvio = "ZOOM"
      break
    if serenvio == "Deliviry":
      metodoenvio = "Delivery"
      break
    else:
      print("Error. Ingrese un método de envío válido")

  if metodoenvio == "Delivery":
    print("Como el servicio de envio es un delivery, deberá agregar los datos del motorizado a continuación: ")
    Nombremoto = input("Nombre del motorizado: ")
    while True:
      Cedulamoto = Input("Cédula del motorizado: ")
      if not Cedulamoto.isnumeric():
        print("Error. La cédula del motorizado solo puede contener caracteres numéricos.")
      else:
        MotorizadoDatos[Cedulamoto] = Nombremoto
        break
  
  while True:
    price = input("Indique el precio del producto: ")
    if not price.isnumeric():
      print("Error. el precio solo puede ser numérico")
    else:
      break
  


  Envio = Envios(order,metodoenvio,MotorizadoDatos,price)
  db["Envios"][order] = Envio

  return db

def buscarenvío(db):

  while True:
    print("""
      Indique el tipo de búsqueda
      1.Cliente
      2.Regresar
      """)
    while True:
      try:
        option = int(input("--->"))
        if option not in range(1, 3):
          raise Exception
        break
      except:
        print("Ingrese una opción válida (1-2)")

    if option == 1:
      busquedaporcliente(db)
    else:
      break


def busquedaporcliente(db):
  clienteinput = input("Ingrese el dni del Cliente para encontrar su venta ")
  encontrado = False
  for key,Envios in db["Envios"].items():
    dni = db["Ventas"][Envios.order].dni
    if clienteinput == dni:
      encontrado = True
      Envios.printenvio()

  if not encontrado:
    print("No existen ningun cliente con esa identificación!")


from Clientes import *


def menuClientes(db):

  while True:
    print(""" 
      ¿Qué desea hacer?
    1.Registrar un Cliente.
    2.Buscar un Cliente.
    3.Modificar los datos de un Cliente existente.
    4.Eliminar Cliente.
    5.Volver al menú principal.
    """)
    while True:
      try:
        option = int(input("--->"))
        if option not in range(1, 6):
          raise Exception
        break
      except:
        print("Ingrese una opción válida (1-5)")

    if option == 1:
      registrarcliente(db)
    elif option == 2:
      buscarclientes(db)
    elif option == 3:
      modificarcliente(db)
    elif option == 4:
      eliminarcliente(db)
    else:
      break


def registrarcliente(db):
  print(
    "A continuación deberá ingresar los datos del Cliente que desea agregar al sistema."
  )
  name = input("Indique el nombre completo del Cliente: ")
  while True:
    tipo = input("Indique si el Cliente es Natural(N) o Jurídico(J): ")
    if tipo != "N" and tipo != "J":
      print("El Cliente debe ser Natural (N) o Jurídico (J) ")
    else:
      break
  while True:
    dni = input("Indique la Cédula de Identidad o Rif del Cliente: ")
    if not dni.isnumeric():
      print("La cédula o RIF debe estar constituido por números solamente!")
    else:
      break
  while True:
    correo = input("Indique el correo del Cliente: ")
    if "@" not in correo or ".com" not in correo:
      print(
        "El corréo del Cliente debe contener un @ y debe contener un .com al final."
      )
    else:
      break
  direnv = input("Indique la Dirección del Cliente ")
  while True:
    tel = input("Ingrese el número del telefono del Cliente")
    if not tel.isnumeric():
      print("El Número celular del cliente debe contener sólamente números!.")
    else:
      break

  cliente = Clientes(name, tipo, dni, correo, direnv, tel)

  db["Clientes"][dni] = cliente
  print("""
  ¡El Cliente se registró exitosamente!.
  """)
  return db


def buscarclientes(db):

  while True:
    print("""
      Indique el tipo de búsqueda
      1.Por Cédula o Rif
      2.Por Correo
      3.Regresar
      """)
    while True:
      try:
        option = int(input("--->"))
        if option not in range(1, 4):
          raise Exception
        break
      except:
        print("Ingrese una opción válida (1-3)")

    if option == 1:
      busquedapordni(db)
    elif option == 2:
      busquedaporcorreo(db)
    else:
      break


def busquedapordni(db):
  dninput = input("Ingrese el dni del Cliente que desea Encontrar: ")
  encontrado = False
  for key, Clientes in db["Clientes"].items():
    dni = Clientes.dni
    if dninput == dni:
      encontrado = True
      Clientes.printclient()

  if not encontrado:
    print("No existen ningun cliente con esa identificación!")


def busquedaporcorreo(db):
  correoinput = input("Ingrese el correo del Cliente que desea Encontrar: ")
  encontrado = False
  for key, Clientes in db["Clientes"].items():
    correo = Clientes.correo
    if correoinput == correo:
      encontrado = True
      Clientes.printclient()

  if not encontrado:
    print("No existen ningun cliente con esa identificación!")


def eliminarcliente(db):
  for key, clientes in db["Clientes"].items():
    clientes.printclient()
  while True:
    try:
      cliente = input("Ingrese la Cédula del cliente que desea eliminar: ")
      if cliente not in db["Clientes"]:
        raise Exception
      break
    except:
      print("Ingrese un nombre válido.")
  originalname = db["Clientes"][cliente].dni
  db["Clientes"].pop(originalname)

  print("Se ha eliminado el Cliente seleccionado.")

  return db


def modificarcliente(db):
  for key, clientes in db["Clientes"].items():
    clientes.printclient()
  while True:
    try:
      clientinho = input("Ingrese la cédula del cliente que desea modificar: ")
      if clientinho not in db["Clientes"]:
        raise Exception
      break
    except:
      print("Ingrese un nombre válido.")
  while True:
    try:
      keynha = input(
        "Ingrese la caracteristica que quiere modificar del cliente (nombre, tipo, DNI, correo, dirección o teléfono): "
      )
      if keynha not in [
          "nombre", "tipo", "DNI", "correo", "dirección", "teléfono"
      ]:
        raise Exception
      break
    except:
      print("Ingrese una característica del producto válida. ")

  if keynha == "nombre":
    NuevoName = input(f"Introduzca el nuevo nombre para {clientinho}: ")
    db["Clientes"][clientinho].NombreCompleto = NuevoName
  elif keynha == "tipo":
    while True:
      Nuevotipo = input("Introduzca el nuevo tipo de Cliente, solo N o J: ")
      if Nuevotipo != "N" and Nuevotipo != "J":
        print("El Cliente debe ser Natural (N) o Jurídico (J) ")
      else:
        db["Clientes"][clientinho].tipo= Nuevotipo
      break
  elif keynha == "DNI":
    while True:
      Nuevadni = input("Ingrese la nueva dni del cliente: ")
      if not Nuevadni.isnumeric():
        print("El dni del cliente debe ser solo numérico! ")

      else:
        originaldni = db["Clientes"][clientinho].dni
        db["Clientes"][clientinho].dni = Nuevadni
        db["Clientes"][Nuevadni]=db["Clientes"][clientinho]
        db["Clientes"].pop(originaldni)
      break
  elif keynha == "correo":
    while True:  
      Nuevocorreo = input("Introduzca el nuevo correo del cliente: ")
      if "@" not in Nuevocorreo or ".com" not in Nuevocorreo:
        print("El correo del cliente debe contener almenos un @ y un .com! ")
      else:
        db["Clientes"][clientinho].correo = Nuevocorreo
        break
  elif keynha == "dirección":
    Nuevadir = input("Ingrese la nueva dirección del Cliente")
    db["Clientes"][clientinho].direnv = Nuevadir
  elif keynha == "teléfono":
    
    while True:
      Nuevotel = input("Introduzca el nuevo número telefónico del Cliente: ")
      if not Nuevotel.isnumeric():
        print("El numero telefónico del Cliente debe ser solo numérico")
      else:
        db["Clientes"][clientinho].tel = Nuevotel
        break 

  print("Se modificó el producto seleccionado.")

  return db
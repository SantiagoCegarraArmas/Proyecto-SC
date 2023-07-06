from Productos import Producto


def productos(endpoint, db):
  for productos in endpoint:
    name = productos["name"]
    description = productos["description"]
    price = productos["price"]
    category = productos["category"]
    quantity = productos["quantity"]

    producto = Producto(name, description, price, category, quantity)

    db["productos"][name] = producto
  return db


def menuproductos(db):

  while True:
    print(""" 
      ¿Qué desea hacer?
    1.Agregar Producto.
    2.Buscar Producto.
    3.Modificar los datos de un producto existente.
    4.Eliminar Producto.
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
      db = agregarproducto(db)
    elif option == 2:
      buscarproducto(db)
    elif option == 3:
      db = modificarproducto(db)
    elif option == 4:
      db = eliminarproducto(db)
    else:
      break


def agregarproducto(db):
  print(
    "A continuación deberá ingresar los datos del producto que desea agregar al sistema."
  )
  name = input("Indique el nombre del producto: ")
  description = input("Escriba una descripción breve del producto: ")
  price = input("Indique el precio del producto: ")
  category = input("Indique la categoría del producto: ")
  quantity = input("Indique la cantidad disponible del producto: ")

  producto = Producto(name, description, price, category, quantity)

  db["productos"][name] = producto
  print("""
  ¡Su producto se agrego exitosamente!.
  """)
  return db

def buscarproducto(db):
  while True:
    print("""
    Indique el tipo de búsqueda
    1.Por nombre 
    2.Por precio
    3.Por Categoría
    4.Por Disponibilidad en el inventario
    5.Regresar
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
      busquedapornombre(db)
    elif option == 2:
      busquedaporprecio(db)
    elif option == 3:
      busquedaporcategoria(db)
    elif option == 4:
      busquedainventario(db)
    else:
      break


def busquedapornombre(db):
  name = input("Introduzca el nombre del producto: ")
  if name not in db["productos"]:
    print("El producto no existe. Recuerda colocar las mayúsculas necesarias.")
  else:
    for key, producto in db["productos"].items():
      if name == key:
        producto.printproduct()
        break


def busquedaporprecio(db):
  price = input("Introduzca el precio exacto del producto: ")
  if not price.isnumeric():
    print("Error! ingrese un valor numérico! ")
  else:
    encontrado = False
    for key, producto in db["productos"].items():
      preciop = producto.price
      if preciop == int(price):
        encontrado = True
        producto.printproduct()

    if not encontrado:
      print("No existe ningun producto con ese precio!")


def busquedaporcategoria(db):
  category = input(
    "Ingrese el nombre exacto de la categoría de el/los productos a encontrar: "
  )
  encontrado = False
  for key, producto in db["productos"].items():
    categoriaproducto = producto.category
    if category == categoriaproducto:
      encontrado = True
      producto.printproduct()

  if not encontrado:
    print("No existen ningun producto en esa categoría!")


def busquedainventario(db):
  quantity = input(
    "Introduzca la cantidad disponible en el inventario de el/ los producto/s: "
  )
  if not quantity.isnumeric():
    print("Error! ingrese un valor numérico!")
  else:
    encontrado = False
    for key, producto in db["productos"].items():
      quantyp = producto.quantity
      if quantyp == int(quantity):
        encontrado = True
        producto.printproduct()
  if not encontrado:
    print("No existe producto con esa cantidad en el inventario!.")


def modificarproducto(db):
  for key,product in db["productos"].items():
    product.printproduct()
  while True:
    try:
      productinho = input("Ingrese el nombre del producto que desea modificar: ")
      if productinho not in db["productos"]:
        raise Exception 
      break
    except:
      print("Ingrese un nombre válido.")
  while True:
    try:
      keynha = input("Ingrese la caracteristica que quiere modificar del producto (nombre, precio, descripción, cantidad disponible o categoría): ")
      if keynha not in ["nombre","descripción","precio","cantidad disponible","categoría"]:
        raise Exception 
      break
    except:
      print("Ingrese una característica del producto válida. (nombre, precio, descripción, cantidad disponible o categoría) ")

  if keynha == "nombre":
    NuevoName = input(f"Introduzca el nuevo nombre para {productinho}: ")
    originalname = db["productos"][productinho].name
    db["productos"][productinho].name = NuevoName
    db["productos"][NuevoName]=db["productos"][productinho]
    db["productos"].pop(originalname)
  elif keynha == "precio":
    Nuevoprice = input(f"Introduzca el nuevo precio para {productinho}: ")
    db["productos"][productinho].price = Nuevoprice
  elif keynha == "descripción":
    Nuevadescription = input(f"Introduzca la nueva descripción para {productinho}: ")
    db["productos"][productinho].description = Nuevadescription
  elif keynha == "cantidad disponible":
    Nuevoquantity = input(f"Introduzca la nueva cantidad disponible para {productinho}: ")
    db["productos"][productinho].quantity = Nuevoquantity
  else:
    Nuevacategoria = input(f"Introduzca la nueva categoria del producto {productinho}: ")
    db["productos"][productinho].category = Nuevacategoria

  print("Se modificó el producto seleccionado.")

  
  return db

def eliminarproducto(db):
  for key,product in db["productos"].items():
    product.printproduct()
  while True:
    try:
      productinho = input("Ingrese el nombre del producto que desea eliminar: ")
      if productinho not in db["productos"]:
        raise Exception 
      break
    except:
      print("Ingrese un nombre válido.")
  originalname = db["productos"][productinho].name
  db["productos"].pop(originalname)

  print("Se ha eliminado el producto seleccionado.")

  return db
  
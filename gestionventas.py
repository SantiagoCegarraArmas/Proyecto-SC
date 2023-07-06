from Ventas import *
from Productos import *
import random

def menuventas(db):
  print("""
  Que desea realizar
  1.Registrar Venta
  2.Generar factura
  3.Buscar Venta
  4.Regresar
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
      db = venta(db)
    elif option == 2:
      factura(db)
    elif option == 3:
      buscarventa(db)
    else:
      break

def venta(db): 
  inputmenu = input("""
  Ingrese la cédula o rif del cliente: 
  """)
  encontrado = False
  for key,Clientes in db["Clientes"].items(): 
    if inputmenu == key:
      encontrado = True
  if encontrado:
    db = registrarventa(db,inputmenu)
  else:
    print ("El cliente no está registrado!")

def registrarventa(db,dni):
  productoslista = { }
  for key,product in db["productos"].items():
    product.printproduct()
  while True:
    while True:
      prodvent = input("Escoja el producto que desea comprar: ")

      
      if prodvent not in db["productos"]:
        print("El producto no existe! ")
      else:
        break
    while True:
      cantidadprod = input("Ingrese la cantidad que desea comprar del producto: ")
      if not cantidadprod.isnumeric:
        print("Error. Indique una cantidad numérica. ")
      else:
        productoslista[prodvent] == cantidadprod
        
        break
        
    
    pregunta = input("Desea añadir otro producto? Si / No")
    if pregunta == "Si":
      pass
    if pregunta == "No":
      break
    else:
      print("Error. Si/No")
  while True:  
    option = input("¿Qué metodo de pago va a utilizar?: PdV, PM, Zelle, Cash")
    if option == "PdV":
      metodopago = "PdV"
      break
    elif option == "PM":
      metodopago = "PM"
      break
    elif option == "Zelle":
      metodopago = "Zelle"
      break
    elif option == "Cash":
      metodopago = "Cash"
      break
    else:
      print("Error. Ingrese un método de pago válido. ")
  while True:
    option2 = input("¿Qué metodo de envío solicitará? (MRW, Zoom, Delivery)")
    if option2 == "MRW":
      metodoenvio = "MRW"
      break
    if option2 == "ZOOM":
      metodoenvio = "ZOOM"
      break
    if option2 == "Deliviry":
      metodoenvio = "Delivery"
      break
    else:
      print("Error. Ingrese un método de envío válido")
  subtotal = 0
  for key,producto in db["productos"].items():
    for ventaproducto,cantidad in productoslista.items():
      if key == ventaproducto:
        subtotal += producto.price * cantidad
        break
  if db["Clientes"]["dni"].tipo == "J":
    descuento = subtotal * 0.05
  else:
    descuento = 0
  iva = subtotal * 0.16
  if metodopago == "cash" or metodopago == "Zelle":
    IGTF = subtotal * 0.03
  else:
    IGTF = 0
  total = subtotal - descuento + iva + IGTF
  
  Venta = Ventas(dni,productoslista,metodopago,metodoenvio,total,subtotal,iva,IGTF)

  order = random_number()
  
  db["Ventas"][order] = Venta



def factura(db):

  for key,Ventas in db["Ventas"].iterm():
    Ventas.printfactura()
    
def random_number():
  try:
    random_number = random.randint(1000000, 9999999)
    return random_number
  except Exception as e:
    print(f"Error: {e}")
    return None  
  

def buscarventa(db):

  while True:
    print("""
      Indique el tipo de búsqueda
      1.Cliente
      2.Monto total
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
      busquedaporcliente(db)
    elif option == 2:
      busquedapormonto(db)
    else:
      break


def busquedaporcliente(db):
  clienteinput = input("Ingrese el dni del Cliente para encontrar su venta ")
  encontrado = False
  for key,Ventas in db["Ventas"].items():
    dni = Ventas.cliente
    if clienteinput == dni:
      encontrado = True
      Ventas.printfactura()

  if not encontrado:
    print("No existen ningun cliente con esa identificación!")


def busquedapormonto(db):
  montoinput = input("Ingrese el monto total de la Venta que desea Encontrar: ")
  encontrado = False
  for key, Ventas in db["Ventas"].items():
    monto = Ventas.total
    if montoinput == monto:
      encontrado = True
      Ventas.printfactura()

  if not encontrado:
    print("No existen ningun cliente con esa identificación!")


  
  



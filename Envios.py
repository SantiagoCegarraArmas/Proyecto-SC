class Envios():
  def __init__(self,order,serenvio,delivery,costoserv,):
    self.serenvio = serenvio
    self.delivery = delivery
    self.costoserv = costoserv
    self.order = order

def printenvio(self):
  print(f""" 
  Orden de la compra: {self.order}
  Servicio de envío: {self.serenvio}
  Datos Del Motorizado en caso de delivery: {self.delivery}
  Costo del servicio: {self.costoserv}

  """)
  
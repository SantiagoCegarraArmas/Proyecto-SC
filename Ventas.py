
class Ventas():

  def __init__(self, cliente, producto, metodopago, metodoenvio, total,
               subtotal, iva, IGTF, descuento,order):
    self.cliente = cliente
    self.producto = producto 
    self.metodopago = metodopago
    self.metodoenvio = metodoenvio
    self.total = total
    self.subtotal = subtotal
    self.iva = iva
    self.IGTF = IGTF
    self.descuento = descuento  
    self.order = order
    
def printfactura(self):
  print(f"""
  Productos : {self.productoslista}
  Subtotal: {self.subtotal}
  Descuento: {self.descuento}
  IVA: {self.iva}
  IGTF: {self.IGTF}
  Método de pago: {self.metodopago}
  Método de envio: {self.metodoenvio}
  
  TOTAL: {self.total}
  
  Orden de compra: {self.order}
  
  
  
  """)


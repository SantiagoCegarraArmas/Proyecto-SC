class Producto():
  def __init__(self,name,description,price,category,quantity):
    self.name = name
    self.description = description
    self.price = price
    self.category = category
    self.quantity = quantity

  def printproduct(self):
    print(f"""
    Nombre : {self.name}
    Descripción : {self.description}
    Precio : {self.price}
    Categoría : {self.category}
    Disponibilidad : {self.quantity}
    
    """)
  
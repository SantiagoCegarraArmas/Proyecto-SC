class Clientes():
  def __init__(self,NombreCompleto,tipo,dni,correo,direnv,tel):
    self.NombreCompleto = NombreCompleto
    self.tipo = tipo
    self.dni = dni
    self.correo = correo
    self.direnv = direnv
    self.tel = tel

  def printclient(self):
    print(f"""
    Nombre : {self.NombreCompleto}
    Tipo de cliente : {self.tipo}
    Cedula de identidad o Rif : {self.dni}
    Correo : {self.correo}
    Dirección del envío : {self.direnv}
    Número de teléfono : {self.tel}
    """)
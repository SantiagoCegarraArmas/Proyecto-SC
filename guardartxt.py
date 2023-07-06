import pickle
import os


def recive_data_text(name_txt, db):
  """
  Parametro: La funcion recibe por parametro el diccionario db(dict) y un archivo.txt.
  Return: La funcion retorna el diccionario con los datos serializados en el archivo.txt.
  """

  binary_read = open(name_txt, 'rb')  # Se abre el archivo

  if os.stat(name_txt).st_size != 0:  # Se comprueba que no este vacio
    db = pickle.load(
      binary_read)  # Si no esta vacio se extraen los datos en el diccionario

  binary_read.close()  # Se cierra el archivo

  return db


def load_data_txt(name_txt, db):
  """
  Parametro: La funcion recibe por parametro el archivo de texto y el diccionario db(dict).
  Return: La funcion no retorna ningun valor, se encarga de serializar los datos contenidos en el diccionario en el archivo de texto.
  """
  # Se abre el archivo para hacer la escritura binaria
  binary_write = open(name_txt, 'wb')

  db = pickle.dump(
    db,
    binary_write)  #Se extraen los daos del diccionarioy se guardan en el txt

  binary_write.close()  # Se cierra el archivo

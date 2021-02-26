import urllib.request
import urllib.response
import requests
import json




class Person:
  def __init__(self, people):
    self.people = people

  def buscar(self):
    self.people_encode = json.loads(self.people)
    self.people_separado = self.people_encode["users"]
    self.busqueda = input("nombre: ")
    self.people_separado
    for p in self.people_separado:
      if self.busqueda.lower() in p["nombre"].lower():
        print("si")
        print(p)
      # if ('"nombre":', self.busqueda) in self.people_separado:
      #   print("si")


#  def add_person(self):
#    #self.new_person = input("introduzca nombre, apellido y edad separados por comas: ")
#    nuevo_usuario_nombre = input ("Agregue el nombre del nuevo usuario: ")
#    nuevo_usuario_apellido = input ("Agregue el apellido del nuevo usuario: ")
#    nuevo_usuario_edad = input ("Agregue la edad del nuevo usuario: ")
#
#
#    with open("data.json", "r") as archivo:
#      archivo_str=archivo.read()
#      archivo_dict=json.loads(archivo_str)
#    with open ("data.json", "w")as archivo_escribible:
#      archivo_dict["users"].append({"nombre":nuevo_usuario_nombre,"apellido":nuevo_usuario_apellido,"edad":nuevo_usuario_edad})
#      json.dump(archivo_dict, archivo_escribible)
#      print("Nuevo usuario generado")


  def add_person(self):
    self.nuevo_usuario_nombre = input ("Agregue el nombre del nuevo usuario: ")
    self.nuevo_usuario_apellido = input ("Agregue el apellido del nuevo susuario: ")
    self.nuevo_usuario_edad = input ("Agregue la edad del nuevo usuario: ")

    url = urllib.request.urlopen("http://localhost:8080/")
    
    archivo_str = url.read()
    self.archivo_dict = json.loads(archivo_str)
    self.archivo_dict["users"].append({"nombre":self.nuevo_usuario_nombre,"apellido":self.nuevo_usuario_apellido,"edad":self.nuevo_usuario_edad})
    requests.post("http://localhost:8080/", self.archivo_dict)
    print("Nuevo usuario generado")

  def borrar_2(self):
    self.people_encode = json.loads(self.people)
    self.people_separado = self.people_encode["users"]
    self.busqueda = input("nombre: ")
    self.people_separado
    for p in self.people_separado:
      if self.busqueda.lower() in p["nombre"].lower():
        print(p)

  def editar(self):
    f = urllib.request.urlopen("http://localhost:8080/")
    file = urllib.request.urlopen("http://localhost:8080/")
    self.people_encode = json.loads(f.read())
    data = json.loads(file.read())
    self.people_separado = self.people_encode["users"]
    self.busqueda = input("nombre persona a editar: ")
    self.people_separado
    for p in self.people_separado:
      if self.busqueda.lower() in p["nombre"].lower():
        new_data = {}
        editar = input("editar: ")
        if editar == "nombre":
          self.editar_nombre = input("cambiar nombre: ")
          new_data[p['nombre']] = {self.editar_nombre}
          data.update(new_data)
        if editar == "apellido":
          self.editar_apellido = input("cambiar apellido: ")
        if editar == "edad":
          self.editar_edad = input("cambiar edad: ")
        json.dump(data, file)
        break
    else:
      print("no se encontró")
      

f = urllib.request.urlopen("http://localhost:8080/")
read = Person(f.read())
p1 = Person(read)

respuesta = input("que quiere hacer: ")
if respuesta == ("buscar"):
  p1.buscar()
if respuesta == ("print"):
  p1.print_a()
if respuesta == ("agregar"):
  p1.add_person()
if respuesta == ("borrar"):
  p1.borrar_2()
if respuesta == ("editar"):
  p1.editar()
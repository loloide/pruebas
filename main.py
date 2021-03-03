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


  def add_person(self):
    self.nuevo_usuario_nombre = input ("Agregue el nombre del nuevo usuario: ")
    self.nuevo_usuario_apellido = input ("Agregue el apellido del nuevo susuario: ")
    self.nuevo_usuario_edad = input ("Agregue la edad del nuevo usuario: ")

    url = urllib.request.urlopen("http://localhost:8080/")
    
    archivo_str = url.read()
    self.archivo_dict = json.loads(archivo_str)
    payload = {"nombre":self.nuevo_usuario_nombre,"apellido":self.nuevo_usuario_apellido,"edad":self.nuevo_usuario_edad}
    r = requests.post("http://localhost:8080/", data=payload)


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
    self.people_encode = json.loads(f.read())
    self.people_separado = self.people_encode["users"]
    self.busqueda = input("nombre persona a editar: ")
    self.people_separado
    for p in self.people_separado:
      if self.busqueda.lower() in p["nombre"].lower():
        print(p)
        editar = input("editar: ")
        if editar == "nombre":
          self.editar_nombre = input("cambiar nombre: ")
          p['nombre'] = {self.editar_nombre}
          payload = p
          f = requests.post("http://localhost:8080/", data=payload)
        if editar == "apellido":
          self.editar_apellido = input("cambiar apellido: ")
          p['apellido'] = {self.editar_apellido}
          payload = p
          f = requests.post("http://localhost:8080/", data=payload)
        if editar == "edad":
          self.editar_edad = input("cambiar edad: ")
          p['edad'] = {self.editar_edad}
          payload = p
          f = requests.post("http://localhost:8080/", data=payload)
        break
    else:
      print("no se encontró")

      

f = urllib.request.urlopen("http://localhost:8080/")
p1 = Person(f.read())


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
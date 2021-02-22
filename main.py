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
    print(self.people_separado)
    for p in self.people_separado:
      if self.busqueda.lower() in p["nombre"].lower():
        print("si")
        print(p)
      # if ('"nombre":', self.busqueda) in self.people_separado:
      #   print("si")


  def selec_cosa(self):
    separadas = self.selected_person.split(",")
    if len(separadas) <4:
      print("no tiene allias")
    seleccionada = input("selecciona la caracteristica: ")

    if seleccionada == ("name"):
      seleccionada = 0
    if seleccionada == ("lastname"):
      seleccionada = 1
    if seleccionada == ("age"):
      seleccionada = 2
    if seleccionada == ("allias"):
      seleccionada = 3

    self.final = separadas[int(seleccionada)]

  def print_cosa(self):
    print(self.final)

  def add_person(self):
    #self.new_person = input("introduzca nombre, apellido y edad separados por comas: ")
    nuevo_usuario_nombre = input ("Agregue el nombre del nuevo usuario: ")
    nuevo_usuario_apellido = input ("Agregue el apellido del nuevo usuario: ")
    nuevo_usuario_edad = input ("Agregue la edad del nuevo usuario: ")


    with open("data.json", "r") as archivo:
      archivo_str=archivo.read()
      archivo_dict=json.loads(archivo_str)
      with open ("data.json", "w")as archivo_escribible:
        archivo_dict["users"].append({"nombre":nuevo_usuario_nombre,"apellido":nuevo_usuario_apellido,"edad":nuevo_usuario_edad})
        json.dump(archivo_dict, archivo_escribible)
        print("Nuevo usuario generado")


  def borrar(self):
     #<------------INTENTO 2------------------->
    with open("data.json", "r") as archivo:
      archivo_str=archivo.read()
      archivo_dict=json.loads(archivo_str)

      self.people_separado = archivo_dict["users"]
      self.busqueda = input("nombre: ")
      for i in self.people_separado:
        if ("nombre:", self.busqueda):
            self.existe_persona = True
        if self.existe_persona == True:
          
         with open('data.json') as data_file:
          data = json.load(data_file)

        for element in data:
            if 'nombre: ' in element:
                del element['users']





            print ("eliminado")    

#<------------INTENTO 1-------------->
      # self.borrar = input("elemento a borrar: ")
      # with open("data.json", "r") as archivo:
      #   archivo_str=archivo.read()
      #   archivo_dict=json.loads(archivo_str)
      # if ("nombre"== self.borrar):
      #   with open('data.json') as data_file:
      #     data = json.load(data_file)
      #     for element in data: 
      #       del element['users']
      #       print("eliminado")

 




f = urllib.request.urlopen("http://localhost:8080/")
read = f.read()
p1 = Person(read)

#print(read)


respuesta = input("que quiere hacer: ")
if respuesta == ("buscar"):
  p1.buscar()
#  p1.selec_cosa
#  p1.print_cosa()
if respuesta == ("agregar"):
  p1.add_person()
if respuesta == ("borrar"):
  p1.borrar()
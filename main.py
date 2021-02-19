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
    for i in self.people_separado:
      if ("nombre:", self.busqueda):
        print("encontrado")


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
    nuevo_usuario = input ("agregue al nuevo usuario ")


    with open("data.json", "a") as archivo:
      json.dump(nuevo_usuario, archivo)
      print("nuevo usuario generado")


    #  f.write("\n")
    #   f.write(self.new_person)
    # print("se agregó " ,self.new_person)
    #r = requests.post('http://localhost:8080/', json={"key": "value"})
    

  def borrar(self):
    self.borrar = input("elemento a borrar: ")
    #person = self.people.split("\n")
    person.remove(self.borrar)
    with open("data.json", "w") as t:
      for p in person:
        t.write(p)
        t.write("\n")
      print("borrado")



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
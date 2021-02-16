import urllib.request
import urllib.response

class Person:
  def __init__(self, people):
    self.people = people

  def buscar_person(self):
    self.person = self.people.split("\n")
    largo = len(self.person)
    print("hay", largo, "personas")
    selectperson = input("selecciona la persona: ")
    self.selected_person = self.person[int(selectperson)]

  def print_person(self):
    print(self.selected_person)

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

  def buscar(self):
    self.person = self.people.split("\n")
    print(self.person)
    self.busqueda = input("buscar: ")

  def buscar_if(self):
    if self.busqueda.lower() in self.person:
      print("se encontró", self.busqueda)

  def add_person(self):
    self.new_person = input("introduzca nombre, apellido y edad separados por comas: ")
    with open("text.txt", "a") as f:
      f.write("\n")
      f.write(self.new_person)
    print("se agregó " ,self.new_person)

  def borrar(self):
    self.borrar = input("elemento a borrar: ")
    person = self.people.split("\n")
    person.remove(self.borrar)
    with open("text2", "w") as t:
      for p in person:
        t.write(p)
        t.write("\n")
    print("borrado")


f = urllib.request.urlopen("http://localhost:8080")
p1 = Person(f.read())

print(f)


respuesta = input("que quiere hacer: ")
if respuesta == ("buscar por nombre"):
  p1.buscar()
  p1.buscar_if()
if respuesta == ("buscar"):
  p1.buscar_person()
  p1.print_person()
#  p1.selec_cosa
#  p1.print_cosa()
if respuesta == ("agregar"):
  p1.add_person()
if respuesta == ("borrar"):
  p1.borrar()
import urllib.request


class Person:
  def __init__(self, people):
    self.people = people

  def print_person(self):
    self.person = self.people.split("\n")
    largo = len(self.person)
    print("hay", largo, "personas")
    selectperson = input("selecciona la persona: ")
    self.selected_person = self.person[int(selectperson)]
    print(self.selected_person)

  def print_cosa(self):
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
    print(self.final)

  def buscar(self):
    self.person = self.people.split("\n")
    print(self.person)
    self.busqueda = input("buscar: ")
    if self.busqueda.lower() in self.person:
      print("se encontró", self.busqueda)

  def add_person(self):
    self.new_person = input("introduzca nombre, apellido y edad separados por comas: ")
    f.write(self.new_person)


with open("text.txt", "r") as f:
  p1 = Person(f.read())


def borrar_persona():
  with urllib.request.urlopen("https://run.mocky.io/v3/ab743856-d98d-44f8-bd1d-e916e883bd5c") as f:
    mybytes = Person(f.read())
  borrar = input("elemento a borrar: ")
  person = people.split("\n")
  person.remove(borrar)
  with open("text2", "w") as t:
    for p in person:
      t.write(p)
      t.write("\n")
  print("borrado")
  

respuesta = input("que quiere hacer: ")
if respuesta == ("buscar por nombre"):
  p1.buscar()
if respuesta == ("buscar"):
  p1.print_person()
  p1.print_cosa()
if respuesta == ("agregar"):
  p1.add_person()
if respuesta == ("borrar"):
  borrar_persona()
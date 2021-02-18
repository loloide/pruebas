import urllib.request
import urllib.response
import json

class Person:
    def __init__(self, people):
        self.people = json.loads(people)

    def buscar(self):
        self.separated = self.people["users"]
        self.person = self.separated.split("{")
        print(self.person)


f = urllib.request.urlopen("http://localhost:8080/")
read = f.read()
p1 = Person(read)

p1.buscar()
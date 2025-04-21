# clases



class Programmer:
    surname: str = None
    def __init__(self, name: str, age: int, languages: list) -> None:
        self.name = name
        self.age = age
        self.languages = languages

    def print_info(self):
        print(f"Nombre: {self.name}| Apellido: {self.surname} | Edad: {self.age} | Lenguajes: {', '.join(self.languages)}")


my_programmer = Programmer(name="Yin", age=27, languages=["Python", "JavaScript"])

my_programmer.print_info()
my_programmer.surname= "alizo"
my_programmer.print_info()

#ejercicio 
class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def count(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)

lista = stack()
lista.push("A")
lista.push("B")
lista.push("C")
lista.print_stack()
print(lista.count())
lista.pop()
lista.pop()
lista.pop()
lista.pop()
lista.print_stack()


#ejercicio pilas y colas
#pila/stack (LIFO)
stack = []

stack.append("1") #push
stack.append("2")
stack.append("3")
print(stack) #["1", "2", "3"]

#pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1] #.pop eliminar y devolver el último
print(stack_item) #3

stack_item = stack.pop() #.pop eliminar y devolver el último
print(stack_item) #3

#cola/queue (FIFO)
queue = []

#enqueue
queue.append("1") #push
queue.append("2")
queue.append("3")

print(queue) #["1", "2", "3"]

#dequeue
dequeue_item = queue[0] #.pop eliminar y devolver el primero
del queue[0] #.pop eliminar y devolver el primero
print(dequeue_item) #1
print(queue.pop(0)) #1
print(queue) #["2", "3"]


# Definición de la clase Pila
class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

    def esta_vacia(self):
        return len(self.items) == 0

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")

#definición de la clase Cola
class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")

    def esta_vacia(self):
        return len(self.items) == 0

    def frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            raise IndexError("La cola está vacía")
        


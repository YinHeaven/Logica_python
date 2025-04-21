
#ejercicio

def countdown(n):
    if n >= 0:
        print(n)
        countdown(n-1)
    


countdown(10)

#ejercicio2
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))  # 120

# extra (el ejercicio que querias hacer de un nuemro regresandoce hasta
#  0 y sumar sus digitos es el fibonacci pero invertido)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(10))  # 55


import random

def generar_lista(tamano, minimo=0, maximo=1000):
    return [random.randint(minimo, maximo) for _ in range(tamano)]

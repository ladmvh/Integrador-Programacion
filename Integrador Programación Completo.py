# Trabajo Integrador - Programación I
# Autor: Franco Cuello
# Tema: Algoritmos de Búsqueda y Ordenamiento en Python

import random
import time

# ----------- Funciones de ordenamiento -----------

def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insercion(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor
    return lista

# ----------- Funciones de búsqueda -----------

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# ----------- Función para generar una lista aleatoria -----------

def generar_lista(tamano, valor_max=1000):
    return [random.randint(0, valor_max) for _ in range(tamano)]

# ----------- Programa principal -----------

if __name__ == "__main__":
    tamano_lista = 1000
    valor_buscado = random.randint(0, 1000)
    lista_original = generar_lista(tamano_lista)
    print(f"Valor a buscar: {valor_buscado}\n")

    # Búsqueda Lineal
    inicio = time.time()
    resultado = busqueda_lineal(lista_original, valor_buscado)
    fin = time.time()
    print("Búsqueda Lineal:")
    print(f"Resultado: {'Encontrado en posición ' + str(resultado) if resultado != -1 else 'No encontrado'}")
    print(f"Tiempo: {fin - inicio:.6f} segundos\n")

    # Ordenamiento Burbuja
    lista_burbuja = lista_original.copy()
    inicio = time.time()
    ordenada_burbuja = burbuja(lista_burbuja)
    fin = time.time()
    print("Ordenamiento Burbuja:")
    print(f"Primeros 10 elementos ordenados: {ordenada_burbuja[:10]}")
    print(f"Tiempo: {fin - inicio:.6f} segundos\n")

    # Ordenamiento Inserción
    lista_insercion = lista_original.copy()
    inicio = time.time()
    ordenada_insercion = insercion(lista_insercion)
    fin = time.time()
    print("Ordenamiento por Inserción:")
    print(f"Primeros 10 elementos ordenados: {ordenada_insercion[:10]}")
    print(f"Tiempo: {fin - inicio:.6f} segundos\n")

    # Búsqueda Binaria (sobre lista ordenada)
    lista_ordenada = sorted(lista_original)
    inicio = time.time()
    resultado_binaria = busqueda_binaria(lista_ordenada, valor_buscado)
    fin = time.time()
    print("Búsqueda Binaria:")
    print(f"Resultado: {'Encontrado en posición ' + str(resultado_binaria) if resultado_binaria != -1 else 'No encontrado'}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")

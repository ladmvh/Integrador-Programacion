from busqueda import busqueda_lineal, busqueda_binaria
from ordenamiento import burbuja, insercion
from datos import generar_lista
import time
import random

if __name__ == "__main__":
    tamano_lista = 1000
    valor_buscado = random.randint(0, 1000)
    lista_original = generar_lista(tamano_lista)
    print(f"Valor a buscar: {valor_buscado}\\n")

    # Búsqueda Lineal
    inicio = time.time()
    resultado = busqueda_lineal(lista_original, valor_buscado)
    fin = time.time()
    print("Búsqueda Lineal:")
    print(f"Resultado: {'Encontrado en posición ' + str(resultado) if resultado != -1 else 'No encontrado'}")
    print(f"Tiempo: {fin - inicio:.6f} segundos\\n")

    # Ordenamiento Burbuja
    lista_burbuja = lista_original.copy()
    inicio = time.time()
    ordenada_burbuja = burbuja(lista_burbuja)
    fin = time.time()
    print("Ordenamiento Burbuja:")
    print(f"Primeros 10 elementos ordenados: {ordenada_burbuja[:10]}")
    print(f"Tiempo: {fin - inicio:.6f} segundos\\n")

    # Ordenamiento Inserción
    lista_insercion = lista_original.copy()
    inicio = time.time()
    ordenada_insercion = insercion(lista_insercion)
    fin = time.time()
    print("Ordenamiento por Inserción:")
    print(f"Primeros 10 elementos ordenados: {ordenada_insercion[:10]}")
    print(f"Tiempo: {fin - inicio:.6f} segundos\\n")

    # Búsqueda Binaria
    lista_ordenada = sorted(lista_original)
    inicio = time.time()
    resultado_binaria = busqueda_binaria(lista_ordenada, valor_buscado)
    fin = time.time()
    print("Búsqueda Binaria:")
    print(f"Resultado: {'Encontrado en posición ' + str(resultado_binaria) if resultado_binaria != -1 else 'No encontrado'}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")

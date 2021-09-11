# busqueda lineal
def busqueda(lista,dato):
    for elem in lista:
        if elem == dato:
            return f"Encontrado: {elem}"

# prueba        
lista = [10,30,35,44,67,88]
print(busqueda(lista,44))

# ordenamiento por insercion 
def ordenamiento(lista):
    for i in range(1,len(lista)):
        actual = lista[i]
        aux = i 
        while aux > 0 and lista[aux-1] > actual:
            lista[aux] = lista[aux-1]
            aux = aux-1
        lista[aux] = actual
    return lista

# prueba
lista = [10,4,67,99,1,54,12,27,33]
print(ordenamiento(lista)) 
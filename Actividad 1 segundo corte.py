def suma(lista, nivel=0):
    print("   " * nivel + f"suma({lista})")

    if len(lista) == 0:
        return 0
    
    return lista[0] + suma(lista[1:], nivel + 1)

numeros = [1, 2, 3, 4]
resultado = suma(numeros)
print("\nLa suma es:", resultado)

def contar(lista, nivel=0):
    print("   " * nivel + f"contar({lista})")

    if lista == []:
        return 0

    return 1 + contar(lista[1:], nivel + 1)

items = ["a", "b", "c", "d"]
resultado = contar(items)
print("\nCantidad de elementos:", resultado)

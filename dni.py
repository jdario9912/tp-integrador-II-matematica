from itertools import combinations


def es_conjunto_pitagorico(conjunto):
    digitos = [int(d) for d in conjunto]
    for a, b, c in combinations(digitos, 3):
        cuadrados = sorted([a**2, b**2, c**2])
        if cuadrados[0] + cuadrados[1] == cuadrados[2]:
            return True
    return False


def es_conjunto_perfecto(conjunto):
    numeros = [int(x) for x in conjunto]
    cantidad = len(numeros)
    suma = sum(numeros)

    if cantidad != suma:
        return False

    for n in numeros:
        if n == 0 or cantidad % n != 0:
            return False

    return True


def ingresar_dnis():
    count = 0
    dnis = []
    while count < 2:
        dni = input("Ingresá un DNI: ").strip()
        if dni.isdigit() and len(dni) >= 1:
            dnis.append(dni)
            count += 1
        else:
            print("DNI inválido. Ingresá solo números.")
    return dnis


def diferencia_conjuntos(conjunto1, conjunto2):
    return sorted(set(conjunto1) - set(conjunto2))


def mostrar_conjunto_formateado(conjunto):
    texto = ""
    for indice, elemento in enumerate(conjunto):
        texto = f"{texto} {int(elemento)} {'' if indice + 1 == len(conjunto) else ','}"
    return f"{{{texto}}}"


def mostrar_operaciones_conjuntos(conjuntos):
    if len(conjuntos) < 2:
        print("\nSe necesitan al menos dos DNIs para comparar conjuntos.")
        return

    union = set.union(*conjuntos)
    interseccion = set.intersection(*conjuntos)
    diferencia_simetrica = set.symmetric_difference(conjuntos[0], conjuntos[1])

    print("\nOperaciones entre conjuntos:")
    print(f"Unión: {mostrar_conjunto_formateado(sorted(union))}")
    print(f"Intersección: {mostrar_conjunto_formateado(sorted(interseccion))}")
    print(
        f"Diferencia (DNI 1 - DNI 2): {mostrar_conjunto_formateado(diferencia_conjuntos(conjuntos[0], conjuntos[1]))}"
    )
    print(
        f"Diferencia (DNI 2 - DNI 1): {mostrar_conjunto_formateado(diferencia_conjuntos(conjuntos[1], conjuntos[0]))}"
    )
    print(
        f"Diferencia simétrica (DNI 1 vs DNI 2): {mostrar_conjunto_formateado(sorted(diferencia_simetrica))}"
    )

    if interseccion:
        print(f"Dígito compartido: {mostrar_conjunto_formateado(interseccion)}")
    for i, c in enumerate(conjuntos):
        if len(c) > 6:
            print(f"DNI {i + 1}: Diversidad numérica alta")


def contar_frecuencias(dni):
    frec = {str(i): 0 for i in range(10)}
    for dig in dni:
        frec[dig] += 1
    return frec


def suma_digitos(dni):
    return sum(int(d) for d in dni)


def obtener_conjuntos_digitos(dnis):
    return [set(dni) for dni in dnis]


def main():
    print("=== Procesador de DNIs ===")
    # dnis = ingresar_dnis()
    dnis = ["15937591", "34567890"]
    if not dnis:
        print("No se ingresaron DNIs.")
        return

    conjuntos = obtener_conjuntos_digitos(dnis)

    for i, dni in enumerate(dnis):
        print(f"\nDNI {i + 1}: {dni}")
        print(
            f"Conjunto de dígitos únicos: {mostrar_conjunto_formateado(sorted(conjuntos[i]))}"
        )
        print(f"Suma de dígitos: {suma_digitos(dni)}")
        frec = contar_frecuencias(dni)
        print("Frecuencia de dígitos:")
        for d in sorted(frec):
            if frec[d] > 0:
                print(f"  Dígito {d}: {frec[d]} vez/veces")
        if es_conjunto_pitagorico(conjuntos[i]):
            print("Es pitagórico")
        else:
            print("No es pitagórico")
        if es_conjunto_perfecto(conjuntos[i]):
            print("Es un conjunto perfecto")
        else:
            print("No es un conjunto perfecto")

    mostrar_operaciones_conjuntos(conjuntos)


if __name__ == "__main__":
    main()

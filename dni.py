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


def obtener_conjuntos_digitos(dnis):
    return [set(dni) for dni in dnis]


def diferencia_conjuntos(conjunto1, conjunto2):
    return sorted(set(conjunto1) - set(conjunto2))


def mostrar_operaciones_conjuntos(conjuntos):
    if len(conjuntos) < 2:
        print("\nSe necesitan al menos dos DNIs para comparar conjuntos.")
        return

    union = set.union(*conjuntos)
    interseccion = set.intersection(*conjuntos)
    diferencia_simetrica = set.symmetric_difference(conjuntos[0], conjuntos[1])

    print("\nOperaciones entre conjuntos:")
    print(f"Unión: {sorted(union)}")
    print(f"Intersección: {sorted(interseccion)}")
    print(
        f"Diferencia (DNI 1 - DNI 2): {diferencia_conjuntos(conjuntos[0], conjuntos[1])}"
    )
    print(
        f"Diferencia (DNI 2 - DNI 1): {diferencia_conjuntos(conjuntos[1], conjuntos[0])}"
    )
    print(f"Diferencia simétrica (DNI 1 vs DNI 2): {sorted(diferencia_simetrica)}")

    if interseccion:
        print(f"Dígito compartido: {interseccion}")
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


def main():
    print("=== Procesador de DNIs ===")
    dnis = ingresar_dnis()
    if not dnis:
        print("No se ingresaron DNIs.")
        return

    conjuntos = obtener_conjuntos_digitos(dnis)

    for i, dni in enumerate(dnis):
        print(f"\nDNI {i + 1}: {dni}")
        print(f"Conjunto de dígitos únicos: {sorted(conjuntos[i])}")
        print(f"Suma de dígitos: {suma_digitos(dni)}")
        frec = contar_frecuencias(dni)
        print("Frecuencia de dígitos:")
        for d in sorted(frec):
            if frec[d] > 0:
                print(f"  Dígito {d}: {frec[d]} vez/veces")

    mostrar_operaciones_conjuntos(conjuntos)


if __name__ == "__main__":
    main()

from datetime import datetime

# from itertools import product


def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def ingresar_anios():
    anios = []
    while True:
        entrada = input("Ingresá un año de nacimiento (ENTER para terminar): ").strip()
        if entrada == "":
            break
        if entrada.isdigit():
            anios.append(int(entrada))
        else:
            print("Entrada inválida. Ingresá solo números.")
    return anios


def contar_pares_impares(anios):
    pares = sum(1 for a in anios if a % 2 == 0)
    impares = len(anios) - pares
    return pares, impares


# esta no la quiero usar
# def edades_actuales(anios):
#     anio_actual = datetime.now().year
#     return [anio_actual - a for a in anios]


def edad_actual(anio):
    anio_actual = datetime.now().year
    return anio_actual - anio


# por ahora no la uso
# def producto_cartesiano(conjunto1, conjunto2):
#     return list(product(conjunto1, conjunto2))


def mostrar_anios_ingresados(anios):
    frase = "Años ingresados: "
    for anio in anios:
        frase = f"{frase} {anio}"
    print(frase)


def main():
    print("=== Análisis de años de nacimiento ===")
    # anios = ingresar_anios()
    anios = [1988, 2002]

    if not anios:
        print("No se ingresaron años.")
        return

    mostrar_anios_ingresados(anios)

    pares, impares = contar_pares_impares(anios)
    print(f"\nNacidos en años pares: {pares}")
    print(f"Nacidos en años impares: {impares}")

    if all(a > 2000 for a in anios):
        print("Grupo Z")

    for anio in anios:
        if es_bisiesto(anio):
            print(f"Tenemos un año especial: {anio}")

    # if any(es_bisiesto(a) for a in anios):
    #     print(f"Tenemos un año especial: {a}")

    # edades = edades_actuales(anios)
    # print(f"\nEdades actuales: {edades}")

    # pc = producto_cartesiano(set(anios), set(edades))
    print(f"\nProducto cartesiano (año, edad):")

    for anio in anios:
        print(f"({anio},  {edad_actual(anio)})")


if __name__ == "__main__":
    main()

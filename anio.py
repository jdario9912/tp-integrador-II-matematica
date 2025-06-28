from datetime import datetime


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


def edad_actual(anio):
    anio_actual = datetime.now().year
    return anio_actual - anio


def mostrar_anios_ingresados(anios):
    frase = "Años ingresados: "
    for anio in anios:
        frase = f"{frase} {anio}"
    print(frase)


def main():
    print("=== Análisis de años de nacimiento ===")
    # anios = ingresar_anios()
    anios = [1988, 2004]

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

    print(f"\nProducto cartesiano (año, edad):")

    for anio in anios:
        print(f"({anio},  {edad_actual(anio)})")


if __name__ == "__main__":
    main()

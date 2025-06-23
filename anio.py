from datetime import datetime
from itertools import product


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


def edades_actuales(anios):
    anio_actual = datetime.now().year
    return [anio_actual - a for a in anios]


def producto_cartesiano(conjunto1, conjunto2):
    return list(product(conjunto1, conjunto2))


def main():
    print("=== Análisis de años de nacimiento ===")
    # anios = ingresar_anios()
    anios = anios = [1992, 2001, 1988, 2000, 1996, 2003, 2004, 1999]

    if not anios:
        print("No se ingresaron años.")
        return

    pares, impares = contar_pares_impares(anios)
    print(f"\n🔢 Nacidos en años pares: {pares}")
    print(f"🔢 Nacidos en años impares: {impares}")

    if all(a > 2000 for a in anios):
        print("👾 Grupo Z")

    if any(es_bisiesto(a) for a in anios):
        print("🎉 Tenemos un año especial")

    edades = edades_actuales(anios)
    print(f"\n📆 Edades actuales: {edades}")

    pc = producto_cartesiano(set(anios), set(edades))
    print(f"\n✖️ Producto cartesiano (año x edad):")
    for par in pc:
        print(f"  {par}")


if __name__ == "__main__":
    main()

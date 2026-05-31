# ============================================
# GESTIÓN DE PRODUCTOS - Con datetime y Colorama
# ============================================

from colorama import init, Fore
from datetime import datetime

init(autoreset=True)


# --- FUNCIÓN 1: Agregar producto ---
def agregar_producto():
    nombre = input(Fore.WHITE + "  Ingresá el nombre del producto: ")

    while nombre == "":
        print(Fore.YELLOW + "  ⚠️  El nombre no puede estar vacío.")
        nombre = input(Fore.WHITE + "  Ingresá el nombre del producto: ")

    precio_texto = input(Fore.WHITE + "  Ingresá el precio del producto: $")

    while not precio_texto.isdigit():
        print(Fore.YELLOW + "  ⚠️  El precio debe ser un número entero válido.")
        precio_texto = input(Fore.WHITE + "  Ingresá el precio del producto: $")

    precio = int(precio_texto)
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")  # 👈 captura fecha y hora del momento

    producto = {"nombre": nombre, "precio": precio, "fecha": fecha}
    return producto


# --- FUNCIÓN 2: Mostrar productos ---
def mostrar_productos(lista):
    if len(lista) == 0:
        print(Fore.YELLOW + "\n  📋 No hay productos cargados todavía.")
    else:
        print(Fore.CYAN + "\n  📋 Productos cargados:")
        print(Fore.CYAN + "  " + "-" * 45)
        contador = 1
        for producto in lista:
            print(Fore.CYAN +  f"  {contador}. {producto['nombre']}")
            print(Fore.WHITE + f"     💲 Precio: ${producto['precio']}")
            print(Fore.WHITE + f"     🕐 Agregado: {producto['fecha']}")
            print(Fore.CYAN + "  " + "-" * 45)
            contador += 1


# --- FUNCIÓN 3: Eliminar producto ---
def eliminar_producto(lista, nombre):
    for producto in lista:
        if producto["nombre"] == nombre:
            lista.remove(producto)
            return True

    return False


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

productos = []

while True:
    print(Fore.MAGENTA + "\n  ╔══════════════════════════════╗")
    print(Fore.MAGENTA +   "  ║    MENÚ DE PRODUCTOS         ║")
    print(Fore.MAGENTA +   "  ╚══════════════════════════════╝")
    print(Fore.WHITE +     "  1. Agregar producto")
    print(Fore.WHITE +     "  2. Mostrar productos")
    print(Fore.WHITE +     "  3. Eliminar producto")
    print(Fore.WHITE +     "  4. Salir")
    print(Fore.MAGENTA +   "  ──────────────────────────────")

    opcion = input(Fore.WHITE + "  Elegí una opción: ")

    if opcion == "1":
        nuevo = agregar_producto()
        productos.append(nuevo)
        print(Fore.GREEN + f"\n  ✅ '{nuevo['nombre']}' fue agregado correctamente.")

    elif opcion == "2":
        mostrar_productos(productos)

    elif opcion == "3":
        nombre = input(Fore.WHITE + "\n  Ingresá el nombre del producto a eliminar: ")
        resultado = eliminar_producto(productos, nombre)

        if resultado == True:
            print(Fore.GREEN + f"  🗑️  '{nombre}' fue eliminado correctamente.")
        else:
            print(Fore.YELLOW + f"  ⚠️  '{nombre}' no existe en la lista.")

    elif opcion == "4":
        print(Fore.MAGENTA + "\n  👋 ¡Hasta luego!\n")
        break

    else:
        print(Fore.RED + "  ❌ Opción inválida. Elegí entre 1 y 4.")
# Proyecto: App para gestionar el inventario del vivero "El Girasol Mareado"

def agregar_producto():
    global id_siguiente
    print("🛒 Ingresá los datos del nuevo producto:")
    nombre = input("Nombre del producto: ")
    try:
        stock = int(input("Stock inicial: "))
        precio = float(input("Precio unitario: "))
    except ValueError:
        print("Error: Asegurate de ingresar números válidos para el stock y el precio.")
        return
    
    nuevo_producto = {
        "id": id_siguiente,
        "nombre": nombre,
        "stock": stock,
        "precio": precio
    }
    listado_productos.append(nuevo_producto)
    id_siguiente += 1
    print(f"✅ Producto '{nombre}' agregado exitosamente.")

def ver_productos():
    if not listado_productos:
        print("No hay productos en el inventario.")
        return
    print("\nProductos en inventario 📝:")
    for producto in listado_productos:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Stock: {producto['stock']}, Precio: ${producto['precio']:.2f}")

def buscar_producto():
    nombre_a_buscar = input(" 🔍 Ingresá el nombre del producto a buscar: ").lower()
    encontrados = [p for p in listado_productos if nombre_a_buscar in p["nombre"].lower()]
    
    if encontrados:
        print("\nProductos encontrados:")
        for producto in encontrados:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Stock: {producto['stock']}, Precio: ${producto['precio']:.2f}")
    else:
        print("No se encontró ningún producto con ese nombre.")

def modificar_stock_producto():
    try:
        id_usuario = int(input("🏷️ Ingresá el ID del producto para modificar el stock: "))
    except ValueError:
        print("Error: Ingresá un número válido.")
        return

    for producto in listado_productos:
        if producto["id"] == id_usuario:
            try:
                nuevo_stock = int(input(f"Stock actual ({producto['stock']}): Ingresá el nuevo stock: "))
                producto["stock"] = nuevo_stock
                print(f"✅ Stock actualizado: {producto['nombre']} ahora tiene {producto['stock']} unidades.")
            except ValueError:
                print("Error: Ingresá un número válido.")
            return
    print("No se encontró un producto con ese ID.")

def actualizar_precio_producto():
    try:
        id_usuario = int(input("💲 Ingresá el ID del producto para actualizar el precio: "))
    except ValueError:
        print("Error: Ingresá un número válido.")
        return

    for producto in listado_productos:
        if producto["id"] == id_usuario:
            try:
                nuevo_precio = float(input(f"Precio actual (${producto['precio']:.2f}): Ingresá el nuevo precio: "))
                producto["precio"] = nuevo_precio
                print(f"✅ Precio actualizado: {producto['nombre']} ahora cuesta ${producto['precio']:.2f}.")
            except ValueError:
                print("Error: Ingresá un número válido.")
            return
    print("No se encontró un producto con ese ID.")

def reporte_bajo_stock():
    try:
        cantidad_minima = int(input("📉 Ingresá el stock mínimo para considerar crítico: "))
    except ValueError:
        print("Error: Ingresá un número válido.")
        return

    productos_bajo_stock = [p for p in listado_productos if p["stock"] <= cantidad_minima]
    
    if not productos_bajo_stock:
        print("No hay productos con stock crítico.")
    else:
        print("\nProductos con stock crítico:")
        for producto in productos_bajo_stock:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Stock: {producto['stock']}")

def borrar_producto():
    try:
        id_usuario = int(input("🗑️ Ingresá el ID del producto que querés eliminar: "))
    except ValueError:
        print("Error: Ingresá un número válido.")
        return

    for producto in listado_productos:
        if producto["id"] == id_usuario:
            print(f"Producto encontrado: {producto['nombre']}")
            confirmar = input("¿Estás seguro que querés eliminar este producto? (S/N): ").lower()
            if confirmar == "s":
                listado_productos.remove(producto)
                print("Producto eliminado con éxito.🗑️")
            return
    print("No se encontró un producto con ese ID.")

# Variables globales
id_siguiente = 4
listado_productos = [
    {"id": 1, "nombre": "Potus", "stock": 5, "precio": 10.5},
    {"id": 2, "nombre": "Ficus", "stock": 7, "precio": 28.0},
    {"id": 3, "nombre": "Caléndula", "stock": 5, "precio": 3.0}
]

# Menú principal
opcion = ""

while opcion != "0":
    print("""
    Menú Principal - 🌻 Bienvenido al Vivero El Girasol Mareado 🌻
    1. Agregar producto 🛒
    2. Ver productos 📝
    3. Buscar producto 🔍
    4. Modificar stock 🏷️
    5. Actualizar precio 💲
    6. Reporte de bajo stock 📉
    7. Eliminar producto 🗑️
    0. Salir 👋
    """)
    opcion = input("Elegí una opción: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        modificar_stock_producto()
    elif opcion == "5":
        actualizar_precio_producto()
    elif opcion == "6":
        reporte_bajo_stock()
    elif opcion == "7":
        borrar_producto()
    elif opcion == "0":
        print("¡Gracias por usar la app!👋 ¡Vuelva pronto!")
    else:
        print("Opción no válida, intentá nuevamente.")

contacto = {
    "nombre": input("Ingrese el nombre: "),
    "telefono": int(input("Ingrese el número de teléfono: ")),
    "email": input("Ingrese el correo electrónico: "),
    "edad": int(input("Ingrese la edad: "))
}
print("-" * 30)
print("Menu de opcones")
print("1. Mostrar Ficha")
print("2. Editar dato")
print("3. Salir")
print("-" * 30)
while True:
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        print("Nombre:", contacto["nombre"])
        print("Teléfono:", contacto["telefono"])
        print("Correo electrónico:", contacto["email"])
        print("Edad:", contacto["edad"])
        break
    elif opcion == 2:
        dato = input ("Ingrese el campo que desea editar (nombre, telefono, email, edad): ")
        if dato == "nombre":
            contacto["nombre"] = input("Ingrese el nuevo nombre: ")
            print("Nombre actualizado :", contacto["nombre"])
        elif dato == "telefono":
            contacto["telefono"] = int(input("Ingrese el nuevo número de teléfono: "))
            print("Número de teléfono actualizado a:", contacto["telefono"])
        elif dato == "email":
            contacto["email"] = input("Ingrese el nuevo correo electrónico: ")
            print("Correo electrónico actualizado a:", contacto["email"])
        elif dato == "edad":
            contacto["edad"] = int(input("Ingrese la nueva edad: "))
            print("Edad actualizada a:", contacto["edad"])
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")
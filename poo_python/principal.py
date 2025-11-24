from datos.conexion import leer_datos, insertar_datos
from datos.consultas import consulta_select, consulta_insert
from modelos.aerolinea import Aerolinea
from modelos.avion import Avion
from modelos.pasajero import Pasajero
from prettytable import PrettyTable
from datetime import datetime


def obtener_datos_aerolineas():
    lista_aerolineas = []
    tabla_aerolineas = PrettyTable()
    tabla_aerolineas.field_names = ["N°", "Nombre", "Web"]

    campos = "id_aerolinea,nombre_aerolinea,web_aerolinea"
    tabla = "aerolineas"
    consulta = consulta_select(campos, tabla)

    if consulta:
        resultado = leer_datos(consulta)
        if resultado:
            for data in resultado:
                aerolinea = Aerolinea(data[0], data[1], data[2])  # type: ignore
                lista_aerolineas.append(aerolinea)
        if len(lista_aerolineas) > 0:
            for objeto in lista_aerolineas:
                tabla_aerolineas.add_row(
                    [
                        objeto._id_aerolinea,
                        objeto._nombre_aerolinea,
                        objeto._web_aerolinea,
                    ]
                )
        print(tabla_aerolineas)


def formatear_avion(objeto: Avion):
    if objeto._tipo_avion == 1:
        tipo = "Carga"
        capacidad = f"{objeto._capacidad_avion} Ton"
    else:
        tipo = "Pasajeros"
        capacidad = f"{objeto._capacidad_avion} Pasajeros"
    return tipo, capacidad


def obtener_datos_aviones():
    lista_aviones = []
    tabla_aviones = PrettyTable()
    tabla_aviones.field_names = ["N°", "Código", "Tipo", "Capacidad"]

    campos = "id_avion,cod_avion,tipo_avion,capacidad_avion"
    tabla = "aviones"
    consulta = consulta_select(campos, tabla)

    if consulta:
        resultado = leer_datos(consulta)
        if not resultado:
            print("No se han encontrado datos de aviones.")
            return
        lista_aviones = [Avion(*data[:4]) for data in resultado]

        for objeto in lista_aviones:
            tipo, capacidad = formatear_avion(objeto)
            tabla_aviones.add_row(
                [objeto._id_avion, objeto._cod_avion, tipo, capacidad]
            )

        print(tabla_aviones)


def obtener_datos_pasajeros():
    lista_pasajeros = []
    tabla_pasajeros = PrettyTable()
    tabla_pasajeros.field_names = ["N°", "Nombre", "Pasaporte", "Fecha Nacimiento"]

    campos = "id_pasajero,nombre_pasajero,num_pasaporte,fecha_nacimiento"
    tabla = "pasajeros"
    consulta = consulta_select(campos, tabla)

    if consulta:
        resultado = leer_datos(consulta)
        if resultado:
            for data in resultado:
                pasajero = Pasajero(data[0], data[1], data[2], data[3])  # type: ignore
                lista_pasajeros.append(pasajero)

        if len(lista_pasajeros) > 0:
            for objeto in lista_pasajeros:
                tabla_pasajeros.add_row(
                    [
                        objeto._id_pasajero,
                        objeto._nombre_pasajero,
                        objeto._num_pasaporte,
                        objeto._fecha_nacimiento,
                    ]
                )
        print(tabla_pasajeros)


def crear_pasajero():
    campos = "nombre_pasajero,num_pasaporte,fecha_nacimiento"
    tabla = "pasajeros"
    nombre_usuario = input("Ingrese Nombre Pasajero: ")
    numero_pasaporte = input("Ingrese Número Pasaporte: ")
    fecha_nacimiento = input("Ingrese Fecha Nacimiento (YYYY-MM-dd): ")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    datos = (nombre_usuario.title(), numero_pasaporte, fecha_nacimiento)
    consulta = consulta_insert(campos, tabla)
    insertar_datos(consulta, datos)


def opciones_menu():
    print()
    print("Menú Principal")
    print("==============")
    print("[1] Gestion Aerolíneas.")
    print("[2] Gestion Asientos.")
    print("[3] Gestion Aviones.")
    print("[4] Gestion Localidades.")
    print("[5] Gestion Pasajeros.")
    print("[6] Gestion Reservas.")
    print("[7] Gestion Vuelos.")
    print("[0] Salir.")


def menu_aerolioneas():
    print()
    print("Menú Aerolíneas")
    print("===============")
    print("[1] Listado Aerolíneas.")
    print("[2] Agregar Aerolínea.")
    print("[3] Modificar Aerolínea.")
    print("[4] Eliminar Aerolínea.")
    print("[0] Volver al menú principal.")


def menu_aviones():
    print()
    print("Menú Aviones")
    print("============")
    print("[1] Listado Aviones.")
    print("[2] Agregar Avión.")
    print("[3] Modificar Avión.")
    print("[4] Eliminar Avión.")
    print("[0] Volver al menú principal.")


def menu_pasajeros():
    print()
    print("Menú Pasajeros")
    print("==============")
    print("[1] Listado Pasajeros.")
    print("[2] Agregar Pasajero.")
    print("[3] Modificar Pasajero.")
    print("[4] Eliminar Pasajero.")
    print("[0] Volver al menú principal.")


def menu_principal():
    print("Sistema de Gestión de Aerolínea")
    print("===============================")
    while True:
        opciones_menu()
        opcion = input("Seleccione su opción [0-7]: ")
        if opcion == "1":
            while True:
                menu_aerolioneas()
                opcion_aerolinea = input("Seleccione su opción [0-4]: ")
                if opcion_aerolinea == "1":
                    obtener_datos_aerolineas()
                elif opcion_aerolinea == "2":
                    pass
                elif opcion_aerolinea == "3":
                    pass
                elif opcion_aerolinea == "4":
                    pass
                elif opcion_aerolinea == "0":
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción incorrecta, intente nuevamente...")
        elif opcion == "2":
            pass
        elif opcion == "3":
            while True:
                menu_aviones()
                opcion_avion = input("Seleccione su opción [0-4]: ")
                if opcion_avion == "1":
                    obtener_datos_aviones()
                elif opcion_avion == "2":
                    pass
                elif opcion_avion == "3":
                    pass
                elif opcion_avion == "4":
                    pass
                elif opcion_avion == "0":
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción incorrecta, intente nuevamente...")
        elif opcion == "4":
            pass
        elif opcion == "5":
            while True:
                menu_pasajeros()
                opcion_pasajero = input("Seleccione su opción [0-4]: ")
                if opcion_pasajero == "1":
                    obtener_datos_pasajeros()
                elif opcion_pasajero == "2":
                    crear_pasajero()
                elif opcion_pasajero == "3":
                    pass
                elif opcion_pasajero == "4":
                    pass
                elif opcion_pasajero == "0":
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción incorrecta, intente nuevamente...")
        elif opcion == "6":
            pass
        elif opcion == "7":
            pass
        elif opcion == "0":
            print("Saliendo de sistema...")
            break
        else:
            print("Opción incorrecta, intente nuevamente...")


menu_principal()

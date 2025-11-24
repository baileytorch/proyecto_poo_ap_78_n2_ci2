from datos.conexion import leer_datos, insertar_datos
from datos.consultas import consulta_select, consulta_insert

from negocio.negocio_aerolineas import obtener_datos_aerolineas
from negocio.negocio_aviones import obtener_datos_aviones
from negocio.negocio_pasajeros import obtener_datos_pasajeros,crear_pasajero


def opciones_menu():
    print()
    print('Menú Principal')
    print('==============')
    print('[1] Gestion Aerolíneas.')
    print('[2] Gestion Asientos.')
    print('[3] Gestion Aviones.')
    print('[4] Gestion Localidades.')
    print('[5] Gestion Pasajeros.')
    print('[6] Gestion Reservas.')
    print('[7] Gestion Vuelos.')
    print('[0] Salir.')


def menu_aerolioneas():
    print()
    print('Menú Aerolíneas')
    print('===============')
    print('[1] Listado Aerolíneas.')
    print('[2] Agregar Aerolínea.')
    print('[3] Modificar Aerolínea.')
    print('[4] Eliminar Aerolínea.')
    print('[0] Volver al menú principal.')


def menu_aviones():
    print()
    print('Menú Aviones')
    print('============')
    print('[1] Listado Aviones.')
    print('[2] Agregar Avión.')
    print('[3] Modificar Avión.')
    print('[4] Eliminar Avión.')
    print('[0] Volver al menú principal.')


def menu_localidades():
    print()
    print('Menú Localidades')
    print('============')
    print('[1] Listado Localidades.')
    print('[2] Agregar Localidad.')
    print('[3] Modificar Localidad.')
    print('[4] Eliminar Localidad.')
    print('[0] Volver al menú principal.')


def menu_pasajeros():
    print()
    print('Menú Pasajeros')
    print('==============')
    print('[1] Listado Pasajeros.')
    print('[2] Agregar Pasajero.')
    print('[3] Modificar Pasajero.')
    print('[4] Eliminar Pasajero.')
    print('[0] Volver al menú principal.')


def menu_principal():
    print('Sistema de Gestión de Aerolínea')
    print('===============================')
    while True:
        opciones_menu()
        opcion = input('Seleccione su opción [0-7]: ')
        if opcion == '1':
            while True:
                menu_aerolioneas()
                opcion_aerolinea = input('Seleccione su opción [0-4]: ')
                if opcion_aerolinea == '1':
                    obtener_datos_aerolineas()
                elif opcion_aerolinea == '2':
                    pass
                elif opcion_aerolinea == '3':
                    pass
                elif opcion_aerolinea == '4':
                    pass
                elif opcion_aerolinea == '0':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opción incorrecta, intente nuevamente...')
        elif opcion == '2':
            pass
        elif opcion == '3':
            while True:
                menu_aviones()
                opcion_avion = input('Seleccione su opción [0-4]: ')
                if opcion_avion == '1':
                    obtener_datos_aviones()
                elif opcion_avion == '2':
                    pass
                elif opcion_avion == '3':
                    pass
                elif opcion_avion == '4':
                    pass
                elif opcion_avion == '0':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opción incorrecta, intente nuevamente...')
        elif opcion == '4':
            while True:
                menu_localidades()
                opcion_localidad = input('Seleccione su opción [0-4]: ')
                if opcion_localidad == '1':
                    pass
                elif opcion_localidad == '2':
                    pass
                elif opcion_localidad == '3':
                    pass
                elif opcion_localidad == '4':
                    pass
                elif opcion_localidad == '0':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opción incorrecta, intente nuevamente...')
        elif opcion == '5':
            while True:
                menu_pasajeros()
                opcion_pasajero = input('Seleccione su opción [0-4]: ')
                if opcion_pasajero == '1':
                    obtener_datos_pasajeros()
                elif opcion_pasajero == '2':
                    crear_pasajero()
                elif opcion_pasajero == '3':
                    pass
                elif opcion_pasajero == '4':
                    pass
                elif opcion_pasajero == '0':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opción incorrecta, intente nuevamente...')
        elif opcion == '6':
            pass
        elif opcion == '7':
            pass
        elif opcion == '0':
            print('Saliendo de sistema...')
            break
        else:
            print('Opción incorrecta, intente nuevamente...')


menu_principal()

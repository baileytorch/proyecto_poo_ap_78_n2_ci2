from interfaces.opciones_menu import opciones_menu, menu_aerolioneas, menu_aviones, menu_localidades, menu_pasajeros
from negocio.negocio_aerolineas import obtener_datos_aerolineas
from negocio.negocio_aviones import obtener_datos_aviones
from negocio.negocio_pasajeros import obtener_datos_pasajeros, crear_pasajero,modificar_pasajero


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
                    modificar_pasajero()
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

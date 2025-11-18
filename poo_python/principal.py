from datos.conexion import leer_datos
from modelos.aerolinea import Aerolinea
from modelos.avion import Avion
from prettytable import PrettyTable


def obtener_datos_aerolineas():
    lista_aerolineas = []
    tabla_aerolineas = PrettyTable()
    tabla_aerolineas.field_names = ['N°', 'Nombre', 'Web']
    consulta = 'SELECT id_aerolinea,nombre_aerolinea,web_aerolinea FROM aerolineas'
    resultado = leer_datos(consulta)
    if resultado:
        for data in resultado:
            aerolinea = Aerolinea(data[0], data[1], data[2])  # type: ignore
            lista_aerolineas.append(aerolinea)
    if len(lista_aerolineas) > 0:
        for objeto in lista_aerolineas:
            tabla_aerolineas.add_row(
                [objeto._id_aerolinea, objeto._nombre_aerolinea, objeto._web_aerolinea])
    print(tabla_aerolineas)


def obtener_datos_aviones():
    lista_aviones = []
    tabla_aviones = PrettyTable()
    tabla_aviones.field_names = [
        'N°', 'Código', 'Tipo', 'Capacidad']
    consulta = 'SELECT id_avion,cod_avion,tipo_avion,capacidad_avion FROM aviones'
    resultado = leer_datos(consulta)
    if resultado:
        for data in resultado:
            avion = Avion(
                data[0], data[1], data[2], data[3])  # type: ignore
            lista_aviones.append(avion)
            
    if len(lista_aviones) > 0:
        for objeto in lista_aviones:
            tipo = ''
            capacidad=''
            if objeto._tipo_avion == 1:
                tipo='Carga'
                capacidad=f'{objeto._capacidad_avion} Ton'
            else:
                tipo='Pasajeros'
                capacidad=f'{objeto._capacidad_avion} Pasajeros'
            tabla_aviones.add_row(
                [objeto._id_avion, objeto._cod_avion, tipo, capacidad])
    print(tabla_aviones)


def ejecucion_metodos():
    obtener_datos_aerolineas()
    obtener_datos_aviones()


ejecucion_metodos()

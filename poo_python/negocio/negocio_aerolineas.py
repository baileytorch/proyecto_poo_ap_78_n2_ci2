from prettytable import PrettyTable
from datos.consultas import consulta_select
from datos.conexion import leer_datos
from modelos.aerolinea import Aerolinea

def obtener_datos_aerolineas():
    lista_aerolineas = []
    tabla_aerolineas = PrettyTable()
    tabla_aerolineas.field_names = ['N°', 'Nombre', 'Web']

    campos = 'id_aerolinea,nombre_aerolinea,web_aerolinea'
    tabla = 'aerolineas'
    consulta = consulta_select(campos, tabla)
    
    if consulta:
        resultado = leer_datos(consulta)
        if resultado:
            for data in resultado:
                aerolinea = Aerolinea(
                    data[0], data[1], data[2])  # type: ignore
                lista_aerolineas.append(aerolinea)
        if len(lista_aerolineas) > 0:
            for objeto in lista_aerolineas:
                tabla_aerolineas.add_row(
                    [objeto._id_aerolinea, objeto._nombre_aerolinea, objeto._web_aerolinea])
        print(tabla_aerolineas)
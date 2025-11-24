from prettytable import PrettyTable
from datos.consultas import consulta_select,consulta_insert
from datos.conexion import leer_datos,insertar_datos
from modelos.pasajero import Pasajero
from datetime import datetime

def obtener_datos_pasajeros():
    lista_pasajeros = []
    tabla_pasajeros = PrettyTable()
    tabla_pasajeros.field_names = ['N°', 'Nombre', 'Pasaporte', 'Fecha Nacimiento']
    
    campos = 'id_pasajero,nombre_pasajero,num_pasaporte,fecha_nacimiento'
    tabla = 'pasajeros'
    consulta = consulta_select(campos, tabla)
    
    if consulta:
        resultado = leer_datos(consulta)
        if resultado:
            for data in resultado:
                pasajero = Pasajero(
                    data[0], data[1], data[2], data[3])  # type: ignore
                lista_pasajeros.append(pasajero)

        if len(lista_pasajeros) > 0:
            for objeto in lista_pasajeros:
                tabla_pasajeros.add_row(
                    [objeto._id_pasajero, objeto._nombre_pasajero, objeto._num_pasaporte, objeto._fecha_nacimiento])
        print(tabla_pasajeros)


def crear_pasajero():
    campos = 'nombre_pasajero,num_pasaporte,fecha_nacimiento'
    tabla = 'pasajeros'
    nombre_usuario = input('Ingrese Nombre Pasajero: ')
    numero_pasaporte = input('Ingrese Número Pasaporte: ')
    fecha_nacimiento = input('Ingrese Fecha Nacimiento (YYYY-MM-dd): ')
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    datos = (nombre_usuario.title(), numero_pasaporte, fecha_nacimiento)
    consulta = consulta_insert(campos,tabla)
    insertar_datos(consulta, datos)
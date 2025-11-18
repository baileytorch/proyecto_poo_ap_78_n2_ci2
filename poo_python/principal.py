from datos.conexion import leer_datos
from modelos.aerolinea import Aerolinea

def obtener_datos_aerolineas():
    consulta = 'SELECT id_aerolinea,nombre_aerolinea,web_aerolinea FROM aerolineas'
    resultado = leer_datos(consulta)
    lista_aerolineas = []
    if resultado:
        for data in resultado:
            aerolinea = Aerolinea(data[0],data[1],data[2]) # type: ignore
            lista_aerolineas.append(aerolinea)
    if len(lista_aerolineas)>0:
        for objeto in lista_aerolineas:
            print(f'Id: {objeto._id_aerolinea} | Nombre: {objeto._nombre_aerolinea} | Web: {objeto._web_aerolinea}')
        
obtener_datos_aerolineas()
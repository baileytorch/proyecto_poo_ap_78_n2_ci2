from datos.consultas import consulta_insert
from datos.conexion import insertar_datos
from interfaces.interface_usuarios import solicitar_data_usuario

def crear_usuario():
    campos = 'nombre_usuario,contrasena,habilitado'
    tabla = 'usuarios'
    nombre, contrasena = solicitar_data_usuario('crear')  # type: ignore
    if nombre != '' and contrasena != '':
        datos = (nombre.title(), contrasena)
        consulta = consulta_insert(campos, tabla)
        insertar_datos(consulta, datos, 'crear')
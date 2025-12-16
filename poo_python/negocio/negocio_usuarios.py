from datos.consultas import consulta_insert
from datos.conexion import insertar_datos
from interfaces.interface_usuarios import solicitar_data_usuario
import bcrypt

def crear_usuario():
    campos = 'nombre_usuario,contrasena,habilitado'
    tabla = 'usuarios'
    nombre, contrasena = solicitar_data_usuario('crear')  # type: ignore
    if nombre != '' and contrasena != '':
        contrasena_encriptada = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
        datos = (nombre.title(), contrasena_encriptada)
        consulta = consulta_insert(campos, tabla)
        insertar_datos(consulta, datos, 'crear')
import requests
from prettytable import PrettyTable

def obtener_users_api(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        # print(respuesta.json())
        tabla_usuarios = PrettyTable()
        tabla_usuarios.field_names= ['Id','Nombre','Email']
        usuarios = respuesta.json()
        for usuario in usuarios:
            tabla_usuarios.add_row([usuario['id'],usuario['name'],usuario['email']])
        print(tabla_usuarios)
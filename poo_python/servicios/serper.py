import requests
import json

def busqueda_serper(url):
    busqueda = input('Qué desea buscar?...')
    
    buscar_google = json.dumps({
    "q": busqueda,
    "gl": "cl"
    })
    
    headers = {
    'X-API-KEY': '68020f011b6756a004d4aaf937b8a12ad58adad1',
    'Content-Type': 'application/json'
    }

    respuesta = requests.post(url, headers=headers, data=buscar_google)

    if respuesta.status_code == 200:
        print(respuesta.json())
    elif respuesta.status_code == 403:
        print('Usuario NO autorizado, revise sus credenciales.')
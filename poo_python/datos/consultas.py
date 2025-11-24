def consulta_select(campos, tabla):
    if campos != "" and tabla != "":
        consulta = f"SELECT {campos} FROM {tabla}"
        return consulta


def consulta_insert(campos, tabla):
    if campos != "" and tabla != "":
        consulta = f"INSERT INTO {tabla} ({campos}) VALUES ("
        lista_campos = campos.split(",")
        for _ in range(len(lista_campos)):
            consulta = consulta + "%s,"
        consulta = consulta[:-1]
        consulta = consulta + ")"
        return consulta

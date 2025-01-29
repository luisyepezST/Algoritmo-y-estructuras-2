class Commit:
    # Constructor de la clase Commit
    def __init__(self, id, lista, commit_anterior, mensaje):
        # Inicializa el atributo id
        self.id = id
        # Inicializa el atributo lista
        self.lista = lista
        # Inicializa el atributo commit_anterior
        self.commit_anterior = commit_anterior
        # Inicializa el atributo mensaje
        self.mensaje = mensaje

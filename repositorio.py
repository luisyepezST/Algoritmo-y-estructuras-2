from archivo import Archivo
from commit import Commit
from rama import Rama

class Repositorio:
    # Constructor de la clase Repositorio
    def __init__(self):
        # Crea la rama principal "main" sin un commit anterior
        master = Rama("main", None)
        # Diccionario para almacenar las ramas del repositorio
        self.ramas = {"main": master}
        # Inicializa el contador de commits
        self.id_commit = 0
        # Almacena el commit más reciente
        self.commit_resiente = None
        # Establece la rama actual como "main"
        self.rama_actual = "main"
        print("Precione Enter")
        input("git init")
        print("Fue creada la rama main")
    
    # Método para crear una nueva rama
    def crear_rama(self, nombre):
        #Comprobar que no sea una cadena vacia 
        if nombre=="":
            print("No ingresó ningún nombre")
        else:
            bandera=0
            for i in self.ramas:
                if nombre == i:
                    print("Ya hay una rama llamada así")
                    bandera=1
            if bandera==0:   
                # Crea una nueva instancia de Rama
                rama = Rama(nombre, self.commit_resiente)
                # Agrega la nueva rama al diccionario de ramas
                self.ramas[nombre] = rama
                print()
                print(f"Se creó una nueva rama {nombre}")
                

    # Método para cambiar la rama actual
    def cambiar_rama(self, nombre):
        bandera=0
        for i in self.ramas:
            if nombre == i:
                print()
                print(f"La rama {nombre} fue cambiada correctamente")
                self.rama_actual = nombre
                self.commit_resiente = self.ramas[self.rama_actual].commit_reciente
                bandera=1
        if bandera==0:
            print()
            print(f"La rama {nombre} no existe")
         
    # Método para hacer un commit
    def hacer_un_commit(self, texto):
        # Convierte el texto en una lista de caracteres
        comando = [i for i in texto]
        # Cuenta la cantidad de puntos en el texto, para saber si se escribio el nombre de un archivo
        cantidad = comando.count(".")
        # Divide el texto en palabras
        comando = texto.split(" ")
        lista_de_archivo = []
        bandera = 0
        print("Ingrese un comentario")
        # Verifica si se ingresó un nombre de archivo
        if cantidad == 0:
            print("No se ingresó el nombre del archivo")
        else:
            mensaje = input("git commit -m ")
            # Agrega cada archivo a la lista de archivos
            for i in comando:
                lista_de_archivo.append(Archivo(i, "Contenido"))
            # Crea un nuevo commit y lo asigna a la rama actual
            self.commit_resiente = Commit(self.id_commit, lista_de_archivo, self.commit_resiente, mensaje)
            self.ramas[self.rama_actual].commit_reciente = self.commit_resiente
            # Incrementa el contador de commits
            self.id_commit += 1
            print("Se realizó  correctamente el commit")

    # Método para mostrar el historial de commits
    def historial_commit(self):
        print()
        commit = self.ramas[self.rama_actual].commit_reciente
        print(f"Head -> {self.rama_actual}")
        print()
        # Recorre la cadena de commits hacia atrás para imprimir el historial 
        while commit != None:
            print(f"commit id ={commit.id}")
            print(f"{commit.mensaje}")
            commit = commit.commit_anterior
            print()
        print()

    # Método para unir dos ramas
    def unir(self, nombre):
        bandera = 0
        contador = -1
        commit_principal = self.ramas[self.rama_actual].commit_reciente
        commit_secundario = self.ramas[nombre].commit_reciente
        acomodador = []
        while bandera == 0:
            contador += 1
            if contador != 0:
                commit_principal = commit_principal.commit_anterior

            commit_secundario = self.ramas[nombre].commit_reciente

            # Compara los commits de ambas ramas
            while commit_secundario != None:
                if commit_principal.id == commit_secundario.id:
                    bandera = 1
                commit_secundario = commit_secundario.commit_anterior
        if contador!=0:
            commit_principal = self.ramas[self.rama_actual].commit_reciente
            commit_secundario = self.ramas[nombre].commit_reciente
            # Agrega los commits de la rama principal al acomodador
            for i in range(contador):
                acomodador.append(commit_principal)
                commit_principal = commit_principal.commit_anterior
            acomodador.reverse()
            # Une los commits de ambas ramas
            acomodador[0].commit_anterior = commit_secundario
            for i in range(contador - 1):
                acomodador[i + 1].commit_anterior = acomodador[i]
            # Actualiza el commit más reciente de la rama actual
            self.ramas[self.rama_actual].commit_reciente = acomodador[len(acomodador) - 1]
            # Agrega un commit que referencia al merge
            self.id_commit+=1
            self.ramas[self.rama_actual].commit_reciente = Commit(self.id_commit,self.ramas[self.rama_actual].commit_reciente.lista,self.ramas[self.rama_actual].commit_reciente,"Merge")
        else:
            commit_secundario = self.ramas[nombre].commit_reciente
            self.ramas[self.rama_actual].commit_reciente=commit_secundario
            # Establece el nuevo commit de la rama fucionada 
            self.commit_resiente=commit_secundario
        print("Se realizo el merge correctamente")


                         
                         
                

               
               
                   
                   


            
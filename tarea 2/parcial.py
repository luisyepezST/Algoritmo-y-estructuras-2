import json  # Importa el módulo json para trabajar con archivos JSON
import os  # Importa el módulo os para interactuar con el sistema operativo
from datetime import datetime  # Importa la clase datetime para manejar fechas y horas

class HistorialDescargas:
    def __init__(self):
        # Inicializa listas para almacenar descargas completadas, en cola y todas las descargas
        self.historial_completadas = []
        self.cola_descargas = []
        self.descargas = []

    def cargar_descargas_desde_json(self, archivo_json):
        # Carga las descargas desde un archivo JSON
        self.historial_completadas = []
        self.cola_descargas = []
        self.descargas = []
        with open(archivo_json, 'r') as file:
            datos = json.load(file)  # Carga los datos del archivo JSON
            for descarga_data in datos:
                # Crea un objeto Descarga a partir de cada entrada en el JSON
                descarga = Descarga(
                    url=descarga_data['url'],
                    tamano=descarga_data['tamano'],
                    fecha_inicio=descarga_data['fecha_inicio'],
                    estado=descarga_data['estado']
                )
                # Clasifica las descargas en completadas o en cola
                if descarga.estado == 'completada':
                    self.historial_completadas.append(descarga)
                    self.descargas.append(descarga)
                else:
                    self.cola_descargas.append(descarga)
                    self.descargas.append(descarga)
        print()
        print("Descargas cargadas correctamente desde el archivo JSON.")

    def mostrar_descargas(self):
        # Muestra las descargas en cola y las completadas
        print("\nDescargas en la cola (pendientes y en progreso):")
        for descarga in self.cola_descargas:
            print(f"{descarga.url} {descarga.tamano} {descarga.fecha_inicio} {descarga.estado}")

        print("\nDescargas completadas:")
        for descarga in self.historial_completadas:
            print(f"{descarga.url} {descarga.tamano} {descarga.fecha_inicio} {descarga.estado}")
        

class Descarga:
    def __init__(self, url, tamano, fecha_inicio, estado):
        # Inicializa un objeto Descarga con sus atributos
        self.url = url
        self.dominio = (((url.split("//"))[1]).split("/"))[0]  # Extrae el dominio de la URL
        self.tamano = tamano
        self.fecha_inicio = fecha_inicio
        self.fecha_hora = datetime.strptime(self.fecha_inicio, "%Y-%m-%d %H:%M:%S")  # Convierte la fecha de inicio a un objeto datetime
        self.estado = estado

class Reporte:
    def __init__(self, historialDescargas):
        # Inicializa el objeto Reporte con el historial de descargas
        self.historialDescargas = historialDescargas

    def dividir(self, lista):
        # Divide la lista en menor, pivote y mayor según el tamaño
        pivote = lista[0].tamano
        mayor = []
        menor = []
        for i in range(len(lista)):
            if lista[i].tamano < pivote:
                menor.append(lista[i])
            if lista[i].tamano > pivote:
                mayor.append(lista[i])
            if lista[i].tamano == pivote and i != 0:
                mayor.append(lista[i])

        return menor, lista[0], mayor

    def quicksort(self, lista):
        # Implementa el algoritmo de ordenamiento QuickSort
        if len(lista) < 2:
            return lista
        
        menor, pivote, mayor = self.dividir(lista)
        return list(self.quicksort(mayor)) + [pivote] + list(self.quicksort(menor))

    def mergesort(self, lista):
        # Implementa el algoritmo de ordenamiento MergeSort
        if len(lista) == 1:
            return lista
        
        divisor = len(lista) // 2
        lista_1 = lista[divisor:]  # Divide la lista en dos mitades
        lista_2 = lista[:divisor]

        lista_derecha = self.mergesort(lista_1)  # Ordena la mitad derecha
        lista_izquierda = self.mergesort(lista_2)  # Ordena la mitad izquierda

        return self.acomodador(lista_derecha, lista_izquierda)

    def acomodador(self, lista_derecha, lista_izquierda):
        # Combina dos listas ordenadas en una sola lista ordenada
        nueva_lista = []
        while len(lista_derecha) > 0 and len(lista_izquierda) > 0:
            if lista_derecha[0].fecha_hora > lista_izquierda[0].fecha_hora: 
                nueva_lista.append(lista_izquierda[0])
                lista_izquierda.pop(0)
            else:
                nueva_lista.append(lista_derecha[0])
                lista_derecha.pop(0)

        while len(lista_derecha) > 0:
            nueva_lista.append(lista_derecha[0])
            lista_derecha.pop(0)
        
        while len(lista_izquierda) > 0:
            nueva_lista.append(lista_izquierda[0])
            lista_izquierda.pop(0)

        return nueva_lista

    def heapify(self, lista, n, i):
        # Ajusta la lista para mantener la propiedad del heap
        largest = i  
        left = 2 * i + 1    
        right = 2 * i + 2    

        if left < n and lista[left].fecha_hora < lista[largest].fecha_hora:
            largest = left

        if right < n and lista[right].fecha_hora < lista[largest].fecha_hora:
            largest = right

        if largest != i:
            lista[i], lista[largest] = lista[largest], lista[i]  # Intercambia elementos
            self.heapify(lista, n, largest)

    def heap_sort(self, lista, fecha, dominio):
        # Implementa el algoritmo de ordenamiento HeapSort
        n = len(lista)
        fecha = datetime.strptime(fecha, "%Y-%m-%d %H:%M")  # Convierte la fecha a un objeto datetime
        listaT = []
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(lista, n, i)  # Construye el heap

        for i in range(n - 1, 0, -1):
            lista[i], lista[0] = lista[0], lista[i]  # Intercambia el elemento más grande con el último
            self.heapify(lista, i, 0)
        lista = lista[::-1]  # Invierte la lista para obtener el orden correcto

        # Filtra las descargas según la fecha y el dominio
        for i in range(len(lista)):
            if (lista[i].fecha_hora > fecha) and (dominio == lista[i].dominio):
                listaT.append(lista[i])
        listaT = self.quicksort(listaT)  # Ordena la lista filtrada
        listaT = listaT[::-1]  # Invierte la lista para mostrar en orden descendente
        print()
        for i in range(len(listaT)):
            print(f"{listaT[i].url} {listaT[i].tamano} {listaT[i].fecha_inicio} {listaT[i].estado}")

    def shell_sort(self, lista, estado, intervalo=None):
        # Implementa el algoritmo de ordenamiento ShellSort
        if intervalo is None:
            intervalo = len(lista) // 2 
        if intervalo < 1:
            # Muestra las descargas con el estado especificado
            for i in lista:
                if i.estado == estado:
                    print(f"{i.url} {i.tamano} {i.fecha_inicio} {i.estado}")
            return

        for i in range(intervalo, len(lista)):
            temp = lista[i]
            j = i
            while j >= intervalo and (len(lista[j - intervalo].url) > len(temp.url)):
                lista[j] = lista[j - intervalo]  # Desplaza los elementos
                j -= intervalo
            lista[j] = temp

        self.shell_sort(lista, estado, intervalo // 2)  # Llama recursivamente con un intervalo reducido

    def agregar(self):
        # Agrega una nueva descarga
        url = input("ingrese la url")
        tamano = int(input("tamaño"))
        año = input("ingrese el año :")
        mes = input("ingrese el mes :")
        dias = input("ingrese el dias :")
        hora = input("ingrese la hora :")
        minutos = input("ingrese los minutos :")
        segundos = input("ingrese los segundos :")
        if int(año) > 2025 or int(mes) > 12 or int(dias) > 31 or int(hora) > 23 or int(minutos) > 59 or int(segundos) > 59:
            print("Formato incorrecto")
            return 0
        else:
            fecha_inicio = f"{año}-{mes}-{dias} {hora}:{minutos}:{segundos}"
        estado = input("ingrese el estado :")
        descarga = {"url": url, "tamano": tamano, "fecha_inicio": fecha_inicio, "estado": estado}
        if os.path.exists("descargas.json"):
            with open("descargas.json", 'r') as archivo:
                datos = json.load(archivo)  # Carga los datos existentes
        datos.append(descarga)  # Agrega la nueva descarga
        with open("descargas.json", 'w') as archivo:
            json.dump(datos, archivo, indent=4)  # Guarda los datos actualizados

        self.historialDescargas.cargar_descargas_desde_json("descargas.json")  # Recarga el historial

    def modificar(self):
        # Modifica una descarga existente
        if os.path.exists("descargas.json"):
            with open("descargas.json", 'r') as archivo:
                datos = json.load(archivo)  # Carga los datos existentes
        cont = 0
        for i in datos:
            texto = f"{cont} {i['url']} {i['tamano']} {i['fecha_inicio']} {i['estado']}"
            cont += 1
            print(texto)  # Muestra las descargas existentes
        modificar = int(input("ingrese el registro que desee modificar"))  # Solicita el índice a modificar
        url = input("ingrese la url")
        tamano = int(input("tamaño"))
        año = input("ingrese el año :")
        mes = input("ingrese el mes :")
        dias = input("ingrese el dias :")
        hora = input("ingrese la hora :")
        minutos = input("ingrese los minutos :")
        segundos = input("ingrese los segundos :")
        if int(año) > 2025 or int(mes) > 12 or int(dias) > 31 or int(hora) > 23 or int(minutos) > 59 or int(segundos) > 59:
            print("Formato incorrecto")
            return 0
        else:
            fecha_inicio = f"{año}-{mes}-{dias} {hora}:{minutos}:{segundos}"
        estado = input("ingrese el estado :")
        descarga = {"url": url, "tamano": tamano, "fecha_inicio": fecha_inicio, "estado": estado}
        datos[modificar] = descarga  # Actualiza la descarga seleccionada
        with open("descargas.json", 'w') as archivo:
            json.dump(datos, archivo, indent=4)  # Guarda los datos actualizados
        self.historialDescargas.cargar_descargas_desde_json("descargas.json")

    def mostrar(self, lista):
        # Muestra una lista de descargas
        for descarga in lista:
            print(f"{descarga.url} {descarga.tamano} {descarga.fecha_inicio} {descarga.estado}")

    def menu(self):
        # Muestra el menú principal y maneja la interacción del usuario
        bandera = 0
        print()
        while bandera == 0:
            try:
                print()
                print("1) lista de las descargas completadas de forma descendente por tamaño")
                print("2) Listar las descargas que no han sido completadas de forma ascendente ")
                print("3) Listar las descargas a partir de una fecha")
                print("4) Listar las descargar de forma descendente por la longitud de su url")
                print("5) Agregar una nueva descarga")
                print("6) Modificar una descarga")
                print("7) Historial de las descargas")
                print("0) Salir")
                
                opcion = int(input("ingrese la opcione que desee :"))  # Solicita al usuario que elija una opción
                print()
                
                if opcion == 1:
                    # Ordena y muestra las descargas completadas
                    self.historialDescargas.historial_completadas = self.quicksort(self.historialDescargas.historial_completadas)
                    self.mostrar(self.historialDescargas.historial_completadas)
                    self.historialDescargas.cargar_descargas_desde_json("descargas.json")

                elif opcion == 2:
                    # Ordena y muestra las descargas en cola
                    self.historialDescargas.cola_descargas = self.mergesort(self.historialDescargas.cola_descargas)
                    self.mostrar(self.historialDescargas.cola_descargas)
                    self.historialDescargas.cargar_descargas_desde_json("descargas.json")
                elif opcion == 3:
                    # Solicita una fecha y muestra las descargas posteriores a esa fecha
                    año = input("ingrese el año :")
                    mes = input("ingrese el mes :")
                    dias = input("ingrese el dias :")
                    hora = input("ingrese la hora :")
                    minutos = input("ingrese los minutos :")
                    dominio = input("ingrese el dominio al que desea acceder :")
                    if int(año) > 2025 or int(mes) > 12 or int(dias) > 31 or int(hora) > 23 or int(minutos) > 59:
                        print("Formato incorrecto")
                    else:
                        fecha = f"{año}-{mes}-{dias} {hora}:{minutos}"
                        self.heap_sort(self.historialDescargas.descargas, fecha, dominio)
                    
                elif opcion == 4:
                    # Solicita un estado y ordena las descargas por la longitud de la URL
                    estado = input("ingrese el estado ")
                    self.shell_sort(self.historialDescargas.descargas, estado)
                elif opcion == 5:
                    # Llama al método para agregar una nueva descarga
                    self.agregar()
                elif opcion == 6:
                    # Llama al método para modificar una descarga existente
                    self.modificar()
                elif opcion == 7:
                    # Muestra el historial de descargas
                    self.historialDescargas.mostrar_descargas()
                elif opcion == 0:
                    # Finaliza el proceso
                    print("Fin del proceso")
                    bandera = 1
            except Exception as e:
                # Maneja errores de entrada
                print(f" Dato ingresado erroneo, error de tipo : {e}")

# Inicializa el historial de descargas y carga los datos desde el archivo JSON
historial = HistorialDescargas()
historial.cargar_descargas_desde_json("descargas.json")
repo = Reporte(historial)  # Crea un objeto Reporte
repo.menu()  # Inicia el menú

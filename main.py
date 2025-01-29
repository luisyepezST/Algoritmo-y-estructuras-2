from repositorio import Repositorio  # Importa la clase Repositorio desde el módulo repositorio

class Main:
    def __init__(self):     
        # Inicializa una instancia de la clase Repositorio
        self.repositorio = Repositorio()

    def menu(self):
        bandera = 0  # Variable de control para el bucle del menú
        print()
        while bandera == 0:  # Bucle que se ejecuta hasta que se cambie la bandera
            try:
                print()
                # Muestra las opciones del menú
                print("1) Hacer un commit")
                print("2) Crear nueva rama")
                print("3) Cambiar de rama")
                print("4) Historial de commit")
                print("5) Juntar")
                print("0) Salir")
                
                # Solicita al usuario que elija una opción
                opcion = int(input("git  "))  # Convierte la entrada a un entero
                print()
                
                # Maneja las diferentes opciones del menú
                if opcion == 1:
                    print("Ingrese los archivos que va a guardar")
                    # Llama al método hacer_un_commit del repositorio con los archivos ingresados
                    self.repositorio.hacer_un_commit(input("git add "))
                elif opcion == 2:
                    print("Ingrese el nombre de la rama que quiere crear")
                    # Llama al método crear_rama del repositorio con el nombre de la nueva rama
                    self.repositorio.crear_rama(input("git branch "))
                elif opcion == 3:
                    print("Ingrese el nombre de la rama a la que quiere cambiar")
                    # Llama al método cambiar_rama del repositorio con el nombre de la rama destino
                    self.repositorio.cambiar_rama(input("git checkout "))
                elif opcion == 4:
                    print("Presione enter para ver el historial de commit de la rama")
                    input("git log")  # Espera a que el usuario presione enter
                    # Llama al método historial_commit del repositorio para mostrar el historial
                    self.repositorio.historial_commit()
                elif opcion == 5:
                    print("Ingrese el nombre de la rama que desea fusionar con su rama actual")
                    # Llama al método unir del repositorio con el nombre de la rama a fusionar
                    self.repositorio.unir(input("git merge "))
                elif opcion == 0:
                    print("Fin del proceso")  # Mensaje de despedida
                    bandera = 1  # Cambia la bandera para salir del bucle
            except Exception as e:
                # Captura y muestra cualquier error que ocurra durante la ejecución
                print(f" Dato ingresado erroneo, error de tipo : {e}")

# Crea una instancia de la clase Main y llama al método menu para iniciar el programa
main = Main()
# Ejecuta la funcion menu
main.menu()




    

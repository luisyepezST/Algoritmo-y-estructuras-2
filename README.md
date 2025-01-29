# Modelo de un sistema Git simulado con programación modular




Estudiante: Luis Yepez

Materia: Algoritmo y estructuras 2




## Descripción de la tarea




Modelar un sistema simplificado de Git utilizando programación orientada a objetos.

(POO) y programación modular en Python. El objetivo es implementar clases que

Representan los principales componentes de un sistema Git: Repositorio, commit, rama y

Archivo. Se debe dividir la funcionalidad en módulos separados según las

responsabilidades.




## Clases implementadas




- Archivo

- Commit

- Rama

- Repositorio

- Main




## Módulos del proyecto




- archivo.py: Contendrá la clase Archivo.

- commit.py: Contendrá la clase Commit.

- rama.py: Contendrá la clase Rama.

- repositorio.py: Contendrá la clase Repositorio.

- main.py: Contendrá el código principal para probar el sistema.




## Instrucciones de uso




1. Presione Enter para iniciar el repositorio.

2. Al iniciar el repositorio se creará una rama llamada main de manera automática.  

3. Para escoger una opción del menú, escriba el número que tienen en la parte izquierda.

4. Si desea hacer un commit, solo debe presionar 1 y darle a enter. Después le pedirá que ingrese el nombre de los archivos que desea añadir, por ejemplo index.html, y después debe presionar enter y agregarle un comentario al commit.

5. Si desea crear una nueva rama, debe presionar el número 2 y enter; después escriba el nombre que le quiere dar a la nueva rama y presione enter para ejecutar la orden.

7. Si desea cambiar de rama, presione el número 3 y Enter;después ingrese el nombre de la rama a la que quiere cambiar y presione Enter para ejecutar la orden.

8. Si desea consultar el historial de la rama, presione el número 4 y enter.

9. Si desea unir la rama en la que está posicionado con otra rama, presione el botón 5 y Enter;después ingrese el nombre de la rama que desea unir y presione Enter para ejecutar la orden.

10. Para terminar la ejecución del código, ingrese el número 0 y presione enter para ejecutar la orden.
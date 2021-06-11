# File-Gestor
Autor: Saúl Valdelvira Iglesias
Versión: 2.1 (27/05/2021)

Esta es una pequeña aplicación que hice en Python.
Su principal objetivo es realizar pequeñas tareas relacionadas con el explorador como: cambiar refactorizar los nombres de muchos archivos a la vez, cifrar y descifrar archivos, clasificar carpetas, etc.
Necesito advertirte de que este NO es un proyecto profesional y que más bien es un desafío personal, ya que soy un principiante en programación y quería familiarizarme con Python. Para eso, te pido que lo uses con precaución. 

Para comenzar elija una ruta sobre la que trabajar.
Después se montrará un menú con todas las opciones posibles, elija la que quiera ejecutar.

Aquí abajo se resumen por lo alto todas ellas:

-Refactorizar el contenido: elija una cadena de texto y el programa la eliminará
    del nombre de todos los archivos del fichero, o bien la sustituirá por otra
    cadena que elijas
    Ejemplo: Tengo un fichero con tres archivos (hola.zip, amanecer.txt, trabajo.jpg)
                si ejecuto esta función y le digo que borre la cadena "a", los nombres
                de estos archivos pasarán a ser: hol.zip, mnecer.txt y trbjo.jpg

                En cambio si elijo cambiar la cadena "a" por "je" los nuevos nombres 
                serán: holje.zip, jemjenecer.txt y trjebjejo.jpg 

    NOTA: la refactorización NO afecta a las extensiones de los archivos
    NOTA: Todas las operaciones que incluyan refactorizar ficheros (cambiar nombres, mover
          de sitio, etc) serán guardadas en un archivo temporal de forma que el usuario pueda
          recuperar TODOS los cambios hechos en la sesion. Este archivo se eliminará al final 
          de la sesión 

-Numeralizar el contenido: Introduce un nombre común y el programa irá nombrando todos
    los archivos en el fichero con ese nombre + un identificador númerico

    Ejemplo: si tengo un fichero con 3 archivos y llamo a esta función, pasándole la 
    cadena "hola"; los nuevos nombres de los archivos serán: hola1, hola2 y hola3

-Asignar nombres desde fichero (.txt): pedirá por consola un archivo .txt, del que 
    cogerá sus líneas e ira asignando a cada archivo una de ellas, en orden

-Organizar episodios de una serie: Es una herramienta que permite organizar una carpeta 
    que contenga episodios de una serie. Puede añadirles el título o el nombre de la 
    y seguidamente puede organizarlos, etiquetándolos con el numero de temporada y de
    episodio (*nombre serie* *título capitulo* S2E23)
     NOTA: Las opciónes de añadir el título y el nombre de la serie son opcionales

-Resumir el contenido (.txt): Resume el contenido del fichero y lo guarda en un archivo llamado "resumen.txt"
    NOTA: el proceso puede hacerse recursivo (a elección) de forma que no solo resumiria el propio fichero, 
    sino que tambíen todas las subcarpetas dentro del mismo

-Clasificar el contenido: Clasifica los archivos del fichero en carpetas, en función de su extensión. 
    Creará una carpeta para cada tipo de extención (.txt, .jpg, etc...) y en ellas meterá todos los 
    archivos que coincidan con dicha extensión

-Eliminar contenido: Permite eliminar el contenido del fichero. Puede ser un archivo concreto (cuyo nombre hay 
    que expecificar, INCLUIDA LA EXTENSIÓN. Para eliminar carpetas simplemente especificar el nombre de la misma,
    ya que estas no tienen extensión)

    NOTA: todas los elementos eliminados, ya sea archivos como ficheros con todo su contenido, son automáticamente 
    reciclados. El usuario tiene la opción de restaurar esos archivos. Además, los archivos reciclados son eliminados
    cuando se cumplan 30 días de su eliminación (antes de ello se avisará al usuario, quien tendra la opción de rescatarlos
    en caso de querer conservarlos)

-Terminar: Simplemente finaliza el programa, pero antes guarda la sesión, es decir el fichero de trabajo activo en el momento. 
    De esta forma el usuario tendra la opción de volver a ese fichero una vez que vuelva a iniciar una nueva sesión

-Cambiar de localización: Cambia el fichero de trabajo

-Directorio actual: Imprime por pantalla el fichero de trabajo actual

-Mostrar el contenido: Muestra por pantalla un resumen del fichero actual. Funciona de forma similar al metodo de resumen, pero 
    en este caso en vez de guardarlo en un archivo, lo muestra en el terminal.

-Restaurar cambios: Restaura los cambios realizados. 
    Cuenta con 3 opciones: 
        -De la sesión: Deshará todos los cabios realizados unicamente en esta sesión (cambios de nombre, de ubicación, 
		refactorizaciones, etc..) todos estos cambios se guardan en un archivo de Backup, que se eliminará al 
		final de la sesión
        -Restauración personalizada: Elije un archivo .bck con los cambios específicos que quieras revertir

        -De la papelera de reciclaje: Retsuara TODOS los archivos eliminados que se conserven en la papelera

        NOTA: si hubiere cualquier problema en la restauración , se creará un archivo expecial con la fecha y hora de la 
	      restauración como nombre y de extensión .bck en la raiz del programa. Desde ahí podrás revisar los posibles errores que 
	      impiden la restauracíon y volver a intentar una restauración personalizada (Estos archivos NO se borrar como Gestor.bck)


# File-Gestor
Autor: Saúl Valdelvira Iglesias
Versión: 2.1 (27/05/2021)

#SPANISH 
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
		refactorizaciones, etc..) todos estos cambios se guardan en un archivo de Backup, que se eliminará al final de la sesión
        -Restauración personalizada: Elije un archivo .bck con los cambios específicos que quieras revertir
	-De la papelera de reciclaje: Retsuara TODOS los archivos eliminados que se conserven en la papelera

        NOTA: si hubiere cualquier problema en la restauración , se creará un archivo expecial con la fecha y hora de la 
	      restauración como nombre y de extensión .bck en la raiz del programa. Desde ahí podrás revisar los posibles errores que 
	      impiden la restauracíon y volver a intentar una restauración personalizada (Estos archivos NO se borrar como Gestor.bck)

#ENGLISH
# File-Manager
Author: Saúl Valdelvira Iglesias
Version: 2.1 (05/27/2021)

This is a small application that I made in Python.
Its main purpose is to perform small explorer-related tasks such as: change, refactor many file names at once, encrypt and decrypt files, classify folders, etc.
I need to warn you that this is NOT a professional project and rather a personal challenge as I am a programming beginner and wanted to get familiar with Python. For that, I ask you to use it with caution.

To get started choose a route to work on.
Then a menu will be displayed with all the possible options, choose the one you want to execute.

All of them are summarized here below:

-Refactor the content: choose a text string and the program will delete it
    the name of all the files in the file, or it will replace it with another
    chain you choose
    
    Example: I have a file with three files (hello.zip, sunrise.txt, work.jpg)
             if I run this function and tell it to delete the string "a", the names
             these files will become: hol.zip, mnecer.txt and trbjo.jpg
On the other hand, if I choose to change the string "a" to "heh" the new names
             they will be: slack.zip, jemjenecer.txt and trjebjejo.jpg

    NOTE: refactoring does NOT affect file extensions
    NOTE: All operations that include refactoring files (renaming, moving
          site, etc) will be saved in a temporary file so that the user can
          recover ALL the changes made in the session. This file will be deleted at the end
          of the session

-Number the content: Enter a common name and the program will name all of them
    the files in the file with that name + a numeric identifier

    Example: if I have a file with 3 files and I call this function, passing it the
    string "hello"; the new names of the files will be: hello1, hello2 and hello3

-Assign names from file (.txt): it will ask the console for a .txt file, of which
    it will take its lines and assign to each file one of them, in order

-Organize episodes of a series: It is a tool that allows you to organize a folder
    containing episodes of a series. You can add the title or name of the
    and then you can organize them, labeling them with the number of season and of
    episode (* series name * * chapter title * S2E23)
     NOTE: The options to add the title and the name of the series are optional

-Summarize the content (.txt): It summarizes the content of the file and saves it in a file called "summary.txt"
    NOTE: the process can be made recursive (by choice) so that not only would it summarize the file itself,
    but also all the subfolders within it

-Classify the content: Classify the files in the file into folders, depending on their extension.
    It will create a folder for each type of extension (.txt, .jpg, etc ...) and in them it will put all the
    files matching that extension

-Eliminate content: Allows you to delete the content of the file. It can be a specific file (whose name is
    to specify, INCLUDING THE EXTENSION. To delete folders simply specify the name of the same,
    since these have no extension)

    NOTE: all deleted items, whether files or files with all their content, are automatically
    recycled. The user has the option to restore those files. Also, the recycled files are deleted
    When 30 days have elapsed since their elimination (before that, the user will be notified, who will have the option to rescue them
    in case you want to keep them)

-Finish: It simply ends the program, but first saves the session, that is, the currently active work file.
    In this way, the user will have the option to return to that file once they start a new session.

-Change location: Change the work file

-Current directory: Prints the current work file on the screen

-Show content: Displays a summary of the current file on the screen. It works similar to the summary method, but
    in this case instead of saving it to a file, it displays it in the terminal.

-Restore changes: Restores the changes made.
    You have 3 options:
        -Of the session: It will undo all changes made only in this session (name changes, location changes,
refactorings, etc ...) all these changes are saved in a Backup file, which will be deleted at the end of the session
        -Custom Restore: Choose a .bck file with the specific changes you want to revert
-From the recycle bin: Retsuara ALL the deleted files that are kept in the trash

        NOTE: if there is any problem in the restoration, an special file will be created with

import os
from os import path, error
from posixpath import abspath
import shutil
from util import *

'''
Programa para gestionar los archivos de un fichero
@author Saúl Valdelvira Iglesias
@version 2.1
'''

this_location=os.getcwd()
session= os.getcwd() + os.sep + "Gestor.ses"
logger_filename= os.getcwd() + os.sep + "Gestor.log"
file_filename= os.getcwd() + os.sep + "Gestor.bck"
recycling_bin=os.getcwd() + os.sep + "RECYCLYING BIN"
version_history=os.getcwd() + os.sep + "VERSION HISTORY" 
encryptor_key=os.getcwd() + os.sep + "key.key"
security_folder=os.getcwd() + os.sep + "SECURITY COPY"


def main():
    set_up()
    a=-1
    while(a!="0"):
        print_options()
        a= input("Elección: ")
        try:
            process(a)
        except error as e:
            Logger.log("Error al procesar la opción [" + a +"]: "+ repr(e))
            print("\nHa ocurrido un error al procesar la operación, repita la petición")
        except Exception as e:
            Logger.log("Error al procesar la opción [" + a +"]: " + repr(e))
            print("\nHa ocurrido una excepción al procesar la operación, repita la petición")

#START UP
def set_up():
    if(os.path.exists(session)):
        print("Recuperar sesión anterior?")
        if(ask_if_yes()):
            recover_session()
        else:
            check_reciclying_bin()
            check_version_history()
            set_directory()
    else:
        check_reciclying_bin()
        check_version_history()
        set_directory()
    
    Logger.filename=logger_filename
    File.filename=file_filename
    File.clean()
    Encryptor.key=encryptor_key
    if(path.exists(encryptor_key)==False):
        Encryptor.write_key()

def set_directory():
    location=input("\nRuta de la carpeta en la que trabajar: ")

    #si la cadena introducida tiene comillas, se las quita para que no las duplique ( "" ruta "" -> "ruta")
    location = clean_input_paths(location)

    #cambia la direccion del proyecto al fichero especificado como parámetro(en el que se necesite cambiar algo)
    try:
        os.chdir(location)
    except:
        print("La ruta indicada no es válida")
        set_directory()

def check_reciclying_bin():
    if(path.exists(recycling_bin)):
        for f in os.listdir(recycling_bin):
            this_file=recycling_bin + os.sep + f
            if not os.listdir(this_file):
                os.rmdir(this_file)
            else:
                i=time_passed(f, "%Y-%m-%d")
                
            if(i.days>=30):
                print("\nLa carpeta de reciclaje " + f +" va a ser eliminada")  
                print("Estás seguro de que quieres eliminarla? (esta acción no se puede deshacer)")    
                if(ask_if_yes()):
                    shutil.rmtree(this_file)
            elif(i.days>=25):
                print("La carpeta de reciclaje " + f +" va a ser eliminada pronto")

def check_version_history():
    if(path.exists(version_history)==False):
        return
        
    for f in os.listdir(version_history):
        this_file=version_history + os.sep + f
        if not os.listdir(this_file):
            os.rmdir(this_file)
        else:
            for v in os.listdir(this_file):
                if(v!="versions.bck"):
                    name=list(path.splitext(v))
                    date=name[0].split(" ")

                    i=time_passed(date[1], "%Y-%m-%d")

                    if(i.days>=30):
                        os.remove(this_file + os.sep + v)

        if(os.listdir(this_file)== ["versions.bck"]):
            shutil.rmtree(this_file)
            
#LOOP
def print_options():
    print("\nOPCIONES")
    print("1-Refactorizar el contenido")
    print("2-Numeralizar el contenido")
    print("3-Asignar nombres desde fichero (.txt)")
    print("4-Organizar episodios de una serie")
    print("5-Resumir el contenido (.txt)")
    print("6-Clasificar el contenido")
    print("7-Eliminar contenido")
    print("8-Editar archivo")
    print("9-Abrir archivo")
    print("10-Encriptar/Desencriptar archivo")
    print("11-Salvaguardar archivos")
    print("0-Terminar")
    print("*-Cambiar de localización")
    print("?-Directorio actual")
    print("/-Mostrar el contenido")
    print("!-Restaurar cambios")
    print("help-Abre el fichero README.txt")
    print("")

def process(a):
    if(a=="0"):
        end_session()
        return
    elif(a=="1"):
        refactor()
    elif(a=="2"):
        numeralise()
    elif(a=="3"):
        name_asigner()
    elif(a=="4"):
        show_organizer()
    elif(a=="5"):
        sumarize()
    elif(a=="6"):
        clasify()
    elif(a=="7"):
        delete()
    elif(a=="8"):
        file_editor()
    elif(a=="9"):
        launch_file()
    elif(a=="10"):
        encrypt_decrypt()
    elif(a=="11"):
        security_copy()
    elif(a=="*"):
        set_directory()
    elif(a=="?"):
        print(os.getcwd())
        return
    elif(a=="/"):
        show_resume()
        return
    elif(a=="!"):
        restore()
    elif(a=="help"):
        show_readme()
        return
    else:
        print("Opción inválida")
        return
    print("\nLa operación se ha realizado exitosamente")

#SESSION METHODS
def recover_session():
    f=open(session, "r")
    ses=f.readline().replace("\n", "")
    if path.exists(ses)==False:
        print("\nNo se ha podido recuperar la sesión")
        set_directory()
    f.close()

def end_session():
    File.clean()
    f=open(session, "w")
    f.write(os.getcwd() + "\n")
    f.close()

#REPLACEMENT/RECICLYING
def replace(old, new):
    new=check_existance(new)
    File.back_up(old, new, None)
    os.replace(old, new)

def recycle(f):
    bin=recycling_bin + os.sep + File.get_date_for_file() 
    if(os.path.exists(recycling_bin)==False):
        os.mkdir(recycling_bin)
        os.mkdir(bin)
    elif(os.path.exists(bin)==False):
        os.mkdir(bin)
    recycled= bin + os.sep + path.basename(f)
    recycled=check_existance(recycled)
    File.back_up(path.abspath(f), recycled, bin + os.sep + "recicles.bck")
    os.replace(path.abspath(f), recycled)

def save_version(f):
    if(is_folder(f)): return

    f_verisons=version_history + os.sep + path.basename(f) 
    if(os.path.exists(version_history)==False):
        os.mkdir(version_history)
        os.mkdir(f_verisons)
    elif(os.path.exists(f_verisons)==False):
        os.mkdir(f_verisons)

    just_name=path.splitext(path.basename(f))

    saved= f_verisons + os.sep + just_name[0] +" "+ File.get_date_and_time_for_file() + just_name[1]
    saved=check_existance(saved)
    File.back_up(path.abspath(f), saved, f_verisons + os.sep + "versions.bck")
    shutil.copy(path.abspath(f), saved)

#REFACTORING
def refactor():
    sub_folders=False
    print(" ")
    print("Que fragmento de los nombres de TODOS los ficheros deseas cambiar(por ejemplo algún símbolo molesto)")
    print(" ")
    not_needed= input("Introduce aquí la cadena a cambiar: ")
    print("")

    print("Quieres borrar el fragmento del nombre o editarlo?")
    option = input("(d) borrar, (c) cambiar: ")
    if(option=="d"):
        sustitute=""
    elif(option=="c"):
        sustitute=input("Por que quieres sustituir el fragmento: ")
    else:
        raise InvalidArgumentException("La opción elegida no coincide con d ni c")

    print("Quieres que el cambio también se aplique a las sub-carpetas?")
    if(ask_if_yes()):
        sub_folders=True

    args= [not_needed, sustitute, sub_folders]

    folders=refactorize_folder(args)
    if(sub_folders):
        recursivity(folders, refactorize_folder, args)

def refactorize_folder(args):
    not_needed=args[0]
    sustitute=args[1]
    sub_folders=args[2]
    folders=[]
    for f in os.listdir():

        if(path.splitext(f)[1]==""):
            if(sub_folders):
                folders.append(path.abspath(f))

        if(f.find(not_needed)!=-1):
            archivo = path.abspath(f)
            sustitution= f.replace(not_needed, sustitute)

            if(len(sustitution)>0):
                nuevo_archivo= list(os.path.split(path.abspath(f)))
                nuevo_archivo[1] = os.sep + sustitution

                nuevo_archivo= "".join(nuevo_archivo)
                #sustituye el viejo nombre del archivo por el nuevo(en caso de que el nuevo nombre no sea vacío)
                replace(archivo, nuevo_archivo)
            else:
                print("\nHa habido un problema al refactorizar algunos de los archivos")          
                Logger.log("Error en la refactorización: el nuevo nombre para '" + archivo + "' es una cadena vacía")

    return folders

#NUMERALIZING
def numeralise():
    #Le das un nombre y pone nombre + *numero* en orden
    common = input("Introduce el nombre común: ")
    a=0
    for f in os.listdir():

        sustitution=common + str(a) #el nuevo nombre es el nombre común + a
        name=change_name(f, sustitution)
        nuevo_archivo= change_path(f, name)

        archivo = path.abspath(f).split("/")
        archivo= "".join(archivo)

        #sustituye el viejo nombre del archivo por el nuevo
        replace(archivo, nuevo_archivo)
        a=a+1

#NAME ASIGNER  
def name_asigner():
    source=input("Donde se encuentra el index de nombres (debe ser un .txt):  ")
    source=clean_input_paths(source)
    i=0
    f= open(source, "r")
    l=f.readlines() #guarda todas las lineas en una lista
    for f in os.listdir() :
        name=(str(l[i]).replace("\n", "")) #asigna al nombre la linea en l[i] quitándole el salto de linea para que no de error
        name = change_name(f, name)

        archivo = path.abspath(f)

        nuevo_archivo=change_path(f, name)


        replace(archivo, nuevo_archivo)
        i=i+1
    f.close()

#SHOW ORGANNIZER
def show_organizer():
    print("Quieres incluir los títulos de los episodios?")
    w_titles=ask_if_yes()
    if(w_titles):
        source=input("Donde se encuentra el index de nombres (debe ser un .txt):  ")
        source=clean_input_paths(source)
        file= open(source, "r")
        l=file.readlines()

    
    print("\nQuieres incluir el nombre de la serie?")
    w_name=ask_if_yes()
    if(w_name):
        serie=input("Nombre de la serie: ")
    temp=input("Temporada: ")
    number_ep=input("Número de episodios: ")
    ep=0

    

    for f in os.listdir() :

        if((ep+1)<10):
            episode="0"+str(ep+1)
        else:
            episode=str(ep+1)

        if(w_titles):
            if(w_name):
                name= serie + " S" + str(temp) + "E" + episode + "  " + (str(l[ep]).replace("\n", ""))
            else:
                name= "S" + str(temp) + "E" + episode + "  " + (str(l[ep]).replace("\n", ""))
        else:
            if(w_name):
                name= serie + " S" + str(temp) + "E" + episode
            else:
                name= "S" + str(temp) + "E" + episode


        name = change_name(f, name)

        archivo = path.abspath(f).split("/")
        archivo="".join(archivo)

        nuevo_archivo=change_path(f, name)


        replace(archivo, nuevo_archivo)
        ep=ep+1
    if(w_titles):
        file.close()
    
#RESUME CONTENT
def sumarize():
    print("El resumen se guardará en la siguiente ruta:")
    print("\t" + os.getcwd())
    destination=os.getcwd()
    print("\nQuieres que se haga un resumen de las subcarpetas también?: ")  
    sub_folders=ask_if_yes()

    print("\nDeseas incluir la ruta en el resumen?:")
    route=ask_if_yes()

    atr=[destination,sub_folders,route]
    folders=write_sumary(atr)
    if(sub_folders):
        atr[0]=os.getcwd
        recursivity(folders, write_sumary, atr)
            
def write_sumary(atr):
    if(atr[0]==os.getcwd):
        destination=os.getcwd() + "\\resumen.txt"
    else:
        destination=atr[0] + "\\resumen.txt"

    sub_folders=atr[1]
    route=atr[2]
    final=[]
    longest_n=0
    longest_ext=0
    folders=[]


    for f in os.listdir():
        name=list(os.path.splitext(f))
        stat_info=os.stat(f)

        fldr=name[1]==""

        result=list()
        result.append(name[0])
        if(fldr):
            result.append("folder")
            if(sub_folders):
                folders.append(str(os.path.abspath(f) + os.sep))
        
        else:
            result.append(name[1])
        result.append(byte_conversor.pretty_size(stat_info.st_size))
        
        #si el tamaño del nombre o extension es mayor, se guarda. Así al final sabremos el nombre más largo 
        if(len(name[0])>longest_n):
            longest_n=len(name[0])
        if(len(result[1])>longest_ext):
            longest_ext=len(result[1])

        final.append(result)
        
    if(len(final)>0):
        gap=calculate_gap(longest_n-6)
        gap2=calculate_gap(longest_ext-4)
        archive=open(destination, "w")
        if(route):
            archive.write("Ruta: " + os.getcwd() + "\n")

        archive.write("Nombre" + gap + "   Tipo " +gap2+   "  Tamaño\n")
        for l in final:
            #calcula los espacios que hay que dejar en medio, en función del tamaño de cada elemento
            gap=calculate_gap(longest_n-len(l[0]))
            gap2=calculate_gap(longest_ext - len(l[1]))
            archive.write(l[0]+gap+"   "+l[1]+gap2+ "   " + l[2] + "\n")

        archive.close()


    
    return folders

#CLASIFIER
'recorre el fichero y clasifica en sub-carpetas los archivos por extension (carpeta con los mp4, otra con los .txt, etc...)'
def clasify():
    types=[]
    l=[]
    for f in os.listdir():
        type=os.path.splitext(f)[1]
        if(type!=""): #asi no clasifica las carpetas
            if(types.__contains__(type)==False):
                types.append(type) #registra esta extension en la lista
                new=[type, f] #todas las listas tienen en su primera posición el tipo de archivo al que representan 
                l.append(new) #añade la lista, la lista para la nueva extensión
            else:
                for element in l:
                    if(element[0]==type): #busca la lista para esa extensión y le añade el archivo
                        element.append(f)

    for type in l:
        fldr=type[0] 

        #intenta crear el fichero y si ya existe, simplemente avisa por pantalla 
        try:
            os.mkdir(fldr)
        except:
            Logger.log("La carpeta " + fldr + " ya existía previamente")

        i=1
        repeated=1
        while(i<len(type)):
            #cambia la ruta del archivo de "fichero/archivo" a "fichero/carpeta/archivo"
            file=list(os.path.split(path.abspath(str(type[i]))))
            name=file[1]
            file[1]= os.sep + fldr

            #si en la carpeta destino ya existe un archivo con el mismo nombre, le añade [index] al final
            if(contains_file("".join(file), name)):
                name=list(os.path.splitext(name))
                name[0]=name[0] + " [" + str(repeated) + "]"
                name="".join(name)
                repeated=repeated+1
            
            file.append(os.sep + name)
            file="".join(file)   

            replace(path.abspath(str(type[i])), file)

            i=i+1

#RESTORE CHANGES
def restore():
    filename=str()
    print("Deseas restaurar los cambios de esta sesión, desde un archivo personalizado, desde la papelera de reciclaje, o desde el historial de versiones?")
    option=input("(a)Está sesión, (b)Restauración personalizada, (c)papelera de reciclaje, (d)historial de versiones, (s)copia de seguridad : ")
    if(option=="b"):
        filename=clean_input_paths(input("\nDonde se encuentra el archivo .bck?: "))
        print("\nEstás seguro de que quieres restaurar TODOS los cambios en este archivo de guardado?")  
        if(ask_if_yes()==False): return
        recall_backup(filename)
    elif(option=="a"):
        filename=File.filename
        print("\nEstás seguro de que quieres restaurar TODOS los cambios hechos en esta sesión?")
        if(ask_if_yes()==False): return
        recall_backup(filename)
    elif(option=="c"):
        print("Seguro que quieres recuperar TODA la papelera de reciclaje?")
        if(ask_if_yes()==False): return
        un_recycle()
    elif(option=="d"):
        recover_versions()
    elif(option=="s"):
        recover_security()
    else:
        raise InvalidArgumentException("ERROR [" + Logger.HERE(False) + "] El parámetro especificado no concide con a, b , c o d")

def recall_backup(filename):
    bck=File.filename
    File.filename=filename
    f=open(filename, "r")
    l=f.readlines()
    l=list(reversed(l))
    line_number=1
    correct=True
    errors=[]
    for line in l:
        line=str(line).split("\t")

        try:
            old=line[1].replace("\n", "")
            new=line[0]
            new=check_existance(new)
            os.replace(old, new)
        except:
            correct=False
            errors.append(str(new + "\t" + old + "\n"))
            Logger.log("Error en el Backup, Linea " + str(line_number) + ": No se ha podido recuperar")
        
        line_number=line_number+1
    
    f.close()
    if(correct):
        File.clean()
    else:
        print("Ha ocurrido un error, puede que la restauración haya sido insatisfactoria")
        print("El archivo Gestor.bck se conservará para una posible futura restauración")
        File.save_file(str(this_location + os.sep + "Gestor " + File.get_date_and_time_for_file()) + ".bck", errors)
        File.clean()
    File.filename=bck

def un_recycle():
    dir=os.getcwd()
    os.chdir(recycling_bin)
    for f in os.listdir():
        filename=recycling_bin + os.sep + f + os.sep + "recicles.bck"
        recall_backup(filename)
        os.rmdir(f)
    os.chdir(dir)

def recover_versions():
    archive=input("De que archivo quieres recuperar las versiones anteriores? (incluir extensión): ")
    folder=version_history + os.sep + archive

    print("\nVERSIONES DISPONIBLES:")
    dir=os.getcwd()
    os.chdir(folder)
    show_resume()
    os.chdir(dir)

    name=list(os.path.splitext(archive))

    print("\nQue versión quieres recuperar (introducir fecha y hora igual que en las versiones anteriormente mostradas, separadas por un espacio)")
    vers=name[0] + " " + input("\t Formato:YYYY-MM-DD HH_MM      Ejemplo: 2021-05-27 23_14: ") + name[1]
    while(path.exists(folder + os.sep + vers)==False):
        print("\nLa entrada es incorrecta, recuerda usar el formato especificado, y que la verison elegida esté en la lista")
        vers=name[0] + " " + input("\t Formato:YYYY-MM-DD HH_MM      Ejemplo: 2021-05-27 23_14: ") + name[1]

    f=open(folder + os.sep + "versions.bck" , "r")
    lines=f.readlines()
    f.close()

    filtered=[]
    for l in lines:
        l=l.split("\t")
        name=os.path.split(l[1])[1].replace("\n", "")
        if(name==vers):
            old=l[1].replace("\n", "")
            new=l[0]
            os.replace(old, new)
        else:
            filtered.append("".join(l))

    f=open(folder + os.sep + "versions.bck" , "w")
    f.writelines(filtered)
    f.close()

def recover_security():
    archive=input("De que carpeta quieres recuperar la copia de seguridad? (introducir ruta): ")
    folder=security_folder + os.sep + str(path.abspath(archive)).split(os.sep)[-2]

    print("\nVERSIONES DISPONIBLES:")
    dir=os.getcwd()
    os.chdir(folder)
    show_resume()
    os.chdir(dir)


    print("\nQue versión quieres recuperar (introducir fecha y hora igual que en las versiones anteriormente mostradas, separadas por un espacio)")
    vers=input("\t Formato:YYYY-MM-DD     Ejemplo: 2021-05-27: ")
    while(path.exists(folder + os.sep + vers)==False):
        print("\nLa entrada es incorrecta, recuerda usar el formato especificado, y que la verison elegida esté en la lista")
        vers=input("\t Formato:YYYY-MM-DD      Ejemplo: 2021-05-27: ")


    print("Quieres desencriptar los archivos?")
    if(ask_if_yes()):
        decrypt=True
        if path.exists(folder+os.sep+"key.key"):
            key=encryptor_key

    f=open(folder + os.sep + vers + os.sep + "security_copy.bck" , "r")
    lines=f.readlines()
    f.close()

    filtered=[]
    for l in lines:
        l=l.split("\t")
        name=os.path.split(l[1])[1].replace("\n", "")
        if(name==vers):
            old=l[1].replace("\n", "")
            new=l[0]

            if(decrypt==True):
                if(is_folder(l[1].replace("\n", ""))):
                    folders=decrypt_folder()
                    recursivity(folders, decrypt_folder, None)
                else:
                    Encryptor.decrypt(l[1].replace("\n", ""), Encryptor.load_key(key))

            os.replace(old, new)
        else:
            filtered.append("".join(l))

    f=open(folder + os.sep + "versions.bck" , "w")
    f.writelines(filtered)
    f.close()

#RESUME
def show_resume():
    final=[]
    longest_n=0
    longest_ext=0
    for f in os.listdir():
        name=list(os.path.splitext(f))
        stat_info=os.stat(f)

        fldr=name[1]==""

        result=list()
        result.append(name[0])
        if(fldr):
            result.append("folder")
        else:
            result.append(name[1])
        result.append(byte_conversor.pretty_size(stat_info.st_size))
        
        if(len(name[0])>longest_n):
            longest_n=len(name[0])
        if(len(result[1])>longest_ext):
            longest_ext=len(result[1])
        
        final.append(result)

    gap=""
    gap=calculate_gap(longest_n-6)
    gap2=calculate_gap(longest_ext-4)

    print("\nNombre" + gap + "   Tipo " + gap2 +   "  Tamaño\n")
    for l in final:
        gap=calculate_gap(longest_n-len(l[0]))
        gap2=calculate_gap(longest_ext - len(l[1]))
        print(l[0]+gap+"   "+l[1]+gap2+ "   " + l[2])

#DELETE
def delete():
    print("Quieres eliminar un archivo concreto, o todo el contenido de un fichero")
    if(input("(u)n archivo, (t)odos: ")=="u"):
        file=input("Nombre del fichero a eliminar: ")
        print("\nQuieres que también se elimine de las subcarpetas?:")
        sub_folders=ask_if_yes()
        folders=delete_folder(file)
        if(sub_folders):
            recursivity(folders, delete_folder, file)
    else:
        print("Que fichero quieres vaciar?: ")
        if(input("(e)ste, (o)tro: ")=="e"):
            print("Seguro que quieres borrar TODO lo que contenga este fichero? ("+ str(len(os.listdir(os.getcwd()))) + " elementos): ")
            if(ask_if_yes()==False):return
            empty_folder(os.getcwd())
        else:
            file=clean_input_paths(input("Donde está ese fichero: "))
            print("Seguro que quieres borrar TODO lo que contenga este fichero? ("+ str(len(os.listdir(file))) + " elementos): ")
            if(ask_if_yes()==False):return
            empty_folder(file)

def empty_folder(loc):
    dir=os.getcwd()
    os.chdir(loc)

    for f in os.listdir():
        recycle(f)
    
    os.chdir(dir)

def delete_folder(file):
    folders=[]
    for f in os.listdir():
        fldr=os.path.splitext(f)[1]==""

        if(fldr):
            folders.append(os.path.abspath(f))

        if(f==file):
            if(fldr):
                print("\nSe ha encontrado una coincidencia con la carpeta " + f)
                print("Estás seguro de que quieres eliminarla?:")
                if(ask_if_yes()):
                    folders.remove(os.path.abspath(f))
                    recycle(f)
            else:
                recycle(f) 
            
    return folders

#/help
def show_readme():
    readme=this_location + os.sep + "README.txt"
    os.startfile(readme)
    
#FILE EDITOR
def file_editor():

    file=clean_input_paths(input("Archivo que abrir(Recuerda incluir la extensión): "))
    while(path.exists(file)==False):
        print("El archivo no se encuentra en el fichero de trabajo actual (" + os.getcwd() + ")")
        file=clean_input_paths(input("Recuerda incluir la extensión e incluir la ruta completa si se encuentra fuera del fichero de trabajo actual: "))
    
    print("\nQuieres refactorizar un archivo de texto (.txt) o abrir otro tipo de archivo?")
    print("NOTA: también puedes abrir un .txt en su aplicacion nativa para editarlo manualmente si elijes la opcion 'o' ")
    
    type=input("(t)exto, (o)tro tipo: ")
    if(type=="t"):
        if(check_extension(file, ".txt")==False):
            raise InvalidExtensionException(".txt", path.splitext(path.basename(file))[1])
        text_refactor(file)
    elif(type=="o"):
        external_edition(file)
    else:
        raise InvalidArgumentException("Opción inválida: " + type + ". Debe ser 't' u 'o'")
    
def text_refactor(name):
    print(" ")
    print("Que fragmentos del archivo deseas cambiar?")
    not_needed= input("Introduce aquí la cadena a cambiar:")

    print("\nQuieres borrar el fragmento o editarlo?")
    option = input("(d) borrar, (c) cambiar: ")
    if(option=="d"):
        sustitute=""
    elif(option=="c"):
        sustitute=input("Por que quieres sustituirlo?: ")
    else:
        raise InvalidArgumentException("La opción elegida no coincide con d ni c")

    file=open(path.abspath(name), "r")
    lines=file.readlines()
    file.close()
    save_version(path.abspath(name))
    result=[]
    for l in lines:
        result.append(l.replace(not_needed, sustitute))
    file=open(path.abspath(name), "w")
    file.writelines(result)
    file.close()

def external_edition(file):
    save_version(path.abspath(file))
    os.startfile(path.abspath(file))

#OPEN FILE
def launch_file():
    file=clean_input_paths(input("Que archivo quieres abrir?: "))
    while(path.exists(file)==False):
        print("\nEl archivo no se ha encontrado, ingresa otra vez el nombre o la ruta")
        file=clean_input_paths(input("Que archivo quieres abrir?: "))

    os.startfile(path.abspath(file))

#ENCRIPTION
def encrypt_decrypt():
    print("Quieres encriptar o desencriptar un archivo?: ")
    if(input("(e)ncriptar, (d)esencriptar: ")=="e"):
        encrypt()
    else:
        decrypt()
    
def encrypt():
    print("\nAVISO! Este proceso utiliza una llave única alojada en la ruta: " + encryptor_key)
    print("Asegurate de no perder ni modificar ese archivo, o es podible que sea imposible recuperar el archivo más adelante")
    
    print("Quieres encriptar un archivo o todo la carpeta?")
    if(input("(u)n archivo, (t)oda la carpeta: ")=="u"):
        file=clean_input_paths(input("Archivo que encriptar: "))

        while(path.exists(path.abspath(file))==False):
            print("\nNo se ha encontrado el archivo, intentalo de nuevo. ")
            print("Recuerda que si el archivo no pertenece a la carpeta de trabajo actual debes introducir la ruta completa")
            file=clean_input_paths(input("Archivo que encriptar: "))

        key=Encryptor.load_key()
        Encryptor.encrypt(file, key)
    else:
        folders=encrypt_folder()
        recursivity(folders, encrypt_folder, None)

def encrypt_folder():

    folders=[]
    for f in os.listdir():
        if(is_folder(path.abspath(f))):
            folders.append(path.abspath(f))
        else:
            Encryptor.encrypt(path.abspath(f), Encryptor.load_key())

    return folders

def decrypt():
    print("\nAVISO! Este proceso requiere de una llave única alojada en la ruta: " + encryptor_key + "que se creó en el momento de la encriptación")
    print("Asegurate de tenerla o el proceso no funcionará")
    print("\nQuieres usar la llave predeterminada (" + encryptor_key + ") o introducir la ruta de otra llave?")
    if(input("(p)redeterminada, (i)ntroducir manualmente: ")=="p"):
        key=Encryptor.load_key()
    else:
        loc=clean_input_paths(input("\nIntroduce la ruta de la llave que quieres utilizar: "))
        while(path.exists(loc)==False):
            print("\nNo se ha encontrado la llave")
            loc=clean_input_paths(input("Vuelve a introducir la ruta: "))


    print("Quieres desencriptar un archivo o todo la carpeta?")
    if(input("(u)n archivo, (t)oda la carpeta: ")=="u"):
        file=clean_input_paths(input("Archivo que desencriptar: "))

        while(path.exists(path.abspath(file))==False):
            print("\nNo se ha encontrado el archivo, intentalo de nuevo. ")
            print("Recuerda que si el archivo no pertenece a la carpeta de trabajo actual debes introducir la ruta completa")
            file=clean_input_paths(input("Archivo que encriptar: "))

        Encryptor.decrypt(file, key)    
    else:
        folders=decrypt_folder()
        recursivity(folders, decrypt_folder, None)
        
def decrypt_folder():
    folders=[]
    for f in os.listdir():
        if(is_folder(path.abspath(f))):
            folders.append(path.abspath(f))
        else:
            Encryptor.decrypt(path.abspath(f), Encryptor.load_key())

    return folders

#SAVE
def security_copy():
    print("Quieres hacer una copia de un archivo, o de todo el fichero?")
    choice=input("(u)n archivo, (f)ichero completo: ")

    print("Quieres que se encripten los archivos antes de guardarlos?") 
    if(ask_if_yes()):
        crypt=True
    else:
        crypt=False
    
    if(choice=="u"):
        secure_file(crypt)
    else:
        secure_folder(crypt)
            
def secure_file(crypt):
    file=clean_input_paths(input("\nDe que archivo quieres hacer una copia?: "))
    while(path.exists(file)==False):
        print("\nNo se ha encontrado el archivo, intentalo de nuevo")
        file=clean_input_paths(input("De que archivo quieres hacer una copia?: "))
    
    secure(file, crypt)

def secure_folder(crypt):
    for f in os.listdir():
        try:
            secure(f , crypt)
        except SameNameException:
            print("MIERDA")
            exit()
        
def secure(f, crypt):
    today_bin=security_folder + os.sep + str(path.abspath(f)).split(os.sep)[-2]
    specific_bin= today_bin + os.sep + File.get_date_for_file() 
    if(path.exists(security_folder)==False):
        os.mkdir(security_folder)
        os.mkdir(today_bin)
        os.mkdir(specific_bin)
    elif(path.exists(today_bin)==False):
        os.mkdir(today_bin)
        os.mkdir(specific_bin)
    elif(path.exists(specific_bin)==False):
        os.mkdir(specific_bin)

    '''
    file=open(specific_bin + os.sep + "info.txt")
    l=file.readline.replace("\n", "").split("\t")
    if(l[0]!=str(path.abspath(f)).split(os.sep)[-1]): raise SameNameException(str(path.abspath(f)).split(os.sep)[-1])
    '''

    file=open(specific_bin + os.sep + "info.txt", "w")
    file.write(path.abspath(f) + "\t" + specific_bin + " \n")
    file.close()


    secured=specific_bin + os.sep + path.basename(f)
    bck=specific_bin + os.sep + "security_copy.bck"

    File.back_up(path.abspath(f), secured, bck)
    if(is_folder(f)):
        shutil.copytree(path.abspath(f), secured)
    else:
        shutil.copy(path.abspath(f), secured)

    if(crypt):
        name=add_to_name(path.basename(secured), " [ENCRYPTED]")
        file=change_path(secured, name)
        os.replace(secured, file)
        if(is_folder(f)):
            dire=os.getcwd()
            os.chdir(path.abspath(f))
            encrypt_folder()
            os.chdir(dire)
        else:
            Encryptor.encrypt(file, Encryptor.load_key())

        shutil.copy(encryptor_key, specific_bin + os.sep + "key.key")

main()





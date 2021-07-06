import inspect
import os 
from os import path
from datetime import datetime
import time
from cryptography.fernet import Fernet

def change_name(archive, new_name):
    name = os.path.splitext(os.path.basename(archive)) #name almacena el nombre en la primera pos y la extension en la segunda

    name = list(name)
    name[0] = new_name  #cambiamos el nombre por elnuevo nombre (sin afectar a la extensión)
    name="".join(name)
    return name

def change_path(archive, new_name):
    pt=path.abspath(str(archive))
    nuevo_archivo= os.path.split(pt) #divide el path en dos

    nuevo_archivo=list(nuevo_archivo) #convierte el path a lista, para poder editarlo
    nuevo_archivo[1] = new_name #cambia el nombre
    nuevo_archivo = "\\".join(nuevo_archivo) #lo convierte de vuelta a string, Y AÑADE \ para que se separe de la carpeta anterior 
    return nuevo_archivo

def add_to_name(archive, addition):
    name = os.path.splitext(os.path.basename(archive)) #name almacena el nombre en la primera pos y la extension en la segunda

    name = list(name)
    name[0] = name[0] + addition  #añadimos al nombre la cadena especificada (sin afectar a la extensión)
    name="".join(name)
    return name

def clean_input_paths(loc):
    if(loc[0] == '"'):
        if(loc[len(loc)-1]=='"'):
            return loc[1:len(loc)-1]
        else:
            return loc[1:len(loc)]
    else:
        if(loc[len(loc)-1]=='"'):
            return loc[0:len(loc)-1]
        else:
            return loc[0:len(loc)]

def calculate_gap(i):
    gap=""
    while(i>0):
        gap=gap+" "
        i=i-1
    return gap

def ask_if_yes():
    if(input("(y)es (n)o: ")=="y"):
        return True
    else:
        return False

def contains_file(path, filename):
    for f in os.listdir(path):
        if (f==filename):
            return True
    return False

def recursivity(folders, function, atributes):
    while(len(folders)>0):
        f=folders.pop()
        dir=os.getcwd() #guarda el directorio antes de entrar a la carpeta
        os.chdir(f) #entra en la carpeta y la resume
        
        if(atributes==None):
            l=function()#guarda en l a su vez las subcarpetas a resumir que hubiere en la subcarpeta
        else:
            l=function(atributes) 
            
        os.chdir(dir) #restaura el directorio principal

        while(len(l)>0):
            folders.append(l.pop()) #añade el contenido de l a la lista de sub_ficheros
            
def time_passed(date, format):
    today=datetime.now()
    date=datetime.strptime(date, format)
    #date=datetime.fromtimestamp(date)
    return today - date

def check_existance(file):
    i=1
    while(path.exists(file)):
        n=path.basename(file)
        a=list(os.path.splitext(n))
        substring=" [" + str(i-1) + "]"
        
        if(str(a[0]).find(substring)!=-1):
            n=change_name(n, str(a[0]).replace(substring, " [" + str(i) + "]"))
        else:
            n=change_name(n, str(a[0] + " [" + str(i) + "]"))
        file=change_path(file, n)
        i=i+1
    return file

def is_folder(f):
    return path.splitext(path.basename(f))[1]==""

def check_extension(file, type):
    name=path.basename(file)
    name=list(path.splitext(name))
    if(name[1]==type):
        return True
    else:
        return False

class byte_conversor:
    # bytes pretty-printing
    UNITS_MAPPING = [
        (1<<50, ' PB'),
        (1<<40, ' TB'),
        (1<<30, ' GB'),
        (1<<20, ' MB'),
        (1<<10, ' KB'),
        (1, (' byte', ' bytes')),
    ]

    def pretty_size(bytes, units=UNITS_MAPPING):
        """Get human-readable file sizes.
        simplified version of https://pypi.python.org/pypi/hurry.filesize/
        """
        for factor, suffix in units:
            if bytes >= factor:
                break
        amount = int(bytes / factor)

        if isinstance(suffix, tuple):
            singular, multiple = suffix
            if amount == 1:
                suffix = singular
            else:
                suffix = multiple
        return str(amount) + suffix

class Logger():
    from inspect import currentframe, getframeinfo
    filename=str()

    def log(message,):
        f=open(Logger.filename, "a")
        time=Logger.get_time()
        f.write(time + "  " + message + "\n")
        f.close()

    def get_time():
        return str(datetime.now().date()) +" " + str(datetime.now().hour) + ":" +str(datetime.now().minute)

    def HERE(do_print=True):
        ''' Get the current file and line number in Python script. The line 
        number is taken from the caller, i.e. where this function is called. 

        Parameters
        ----------
        do_print : boolean
            If True, print the file name and line number to stdout. 

        Returns
        -------
        String with file name and line number if do_print is False.

        Examples
        --------
        HERE() # Prints to stdout

        print(HERE(do_print=False))
        '''
        frameinfo = inspect.getframeinfo(inspect.currentframe().f_back)
        filename = os.path.split(frameinfo.filename)[-1]
        linenumber = frameinfo.lineno
        loc_str = 'File: %s, line: %d' % (filename, linenumber)
        if do_print:
            print('HERE AT %s' % (loc_str))
        else:
            return loc_str

class File:
    filename=str()
    
    def back_up(old, new, folder):
        if(folder==None):
           f=open(File.filename, "a")
        else:
            f=open(folder, "a")

        f.write(old + "\t" + new  + "\n")
        f.close()

    def clean():
        if(path.exists(File.filename)):
            os.remove(File.filename)

    def save_file(new_name, errors):
        b=open(str(new_name), "w")
        b.writelines(errors)
        b.close()

    def get_date_and_time_for_file():
        return str(datetime.now().date()) +" "+ str(datetime.now().hour) + "_" +str(datetime.now().minute) 

    def get_date_for_file():
        return str(datetime.now().date())
    
class Encryptor():
    key=str()

    #Generates a key and save it into a file
    def write_key():
        key = Fernet.generate_key()
        with open(Encryptor.key, "wb") as key_file:
            key_file.write(key)

    def special_key(key):
        return open(key, "rb").read()

    def input_key(key):
        with open(Encryptor.key, "wb") as key_file:
            key_file.write(key)

    #Loads the key from the current directory named `key.key`
    def load_key():
        return open(Encryptor.key, "rb").read()

    #Given a filename (str) and key (bytes), it encrypts the file and write it
    def encrypt(filename, key):
        f = Fernet(key)

        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()

        # encrypt data
        encrypted_data = f.encrypt(file_data)

        # write the encrypted file
        with open(filename, "wb") as file:
            file.write(encrypted_data)

    #Given a filename (str) and key (bytes), it decrypts the file and write it
    def decrypt(filename, key):
        f = Fernet(key)

        with open(filename, "rb") as file:
            # read the encrypted data
            encrypted_data = file.read()

        # decrypt data
        decrypted_data = f.decrypt(encrypted_data)

        # write the original file
        with open(filename, "wb") as file:
            file.write(decrypted_data)       

class InvalidArgumentException(Exception):
    pass
    def __init__(self, message):
        super().__init__(message)

class InvalidExtensionException(Exception):
    pass
    def __init__(self, expected_ext, given_ext):
        message="Se esperaba la extensión '" + expected_ext + "' pero se ha recibido la extensión '" + given_ext + "' en su lugar"
        super().__init__(message)

class SameNameException(Exception):
    pass
    def __init__(self, route):
        message="Ya existe una carpeta con este nombre de otra ruta: " + route
        super().__init__(message)
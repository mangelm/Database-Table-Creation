#---------------------Módulos necesarios----------------------------------
from tkinter import *
from tkinter import messagebox
import sqlite3

#---------------------Funciones----------------------------------
#--------------------Primer Apartado-----------------------------


"""
Esta función pregunta al usuario si desea salir de la aplicación. 
Si el usuario da afirmativo, se destruye la raíz de la ventana. 
Esto significa que la ventana de la aplicación se cierra.
"""
def Salir():
    
    valorpregunta = messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?") #Para almacenar el valor true o false
    
    if valorpregunta==True: 
        raiz.destroy()


"""
Esta función se encarga de conectar a una base de datos y crear una tabla si no existe. 
Primero, crea una conexión a la base de datos con la función "sqlite3.connect()". 
Luego, crea un cursor con el que se puede ejecutar comandos de SQL. 
Después, intenta crear una tabla con la función "miCursor.execute()". 
Si la tabla ya existe, se mostrará un mensaje de advertencia con la función "messagebox.showwarning()". 
Si la tabla se crea correctamente, se mostrará un mensaje de información con la función "messagebox.showinfo()".
"""
def Connectar():
    #Creacion de la base de datos
    miConexion = sqlite3.connect("Usuarios")
    
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
                    CREATE TABLE DATOUSUARIOS (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    NOMBRE_USUARIO VARCHAR(50),
                    PASSWORD VARCHAR(50),
                    APELLIDO VARCHAR(10),
                    DIRECCION VARCHAR(50),
                    COMENTARIOS VARCHAR(100))
                ''')

        messagebox.showinfo("BBDD","BBDD creada con éxito") #El primero es el texto en el primer lugar

    except sqlite3.OperationalError:

        messagebox.showwarning("¡Atención!","La BBDD ya existe")


#-------------Segundo Apartado-----------------------------------------------


"""
La función Borrar_campos() es una función que se usa para borrar los campos de un formulario. 
Esta función establece los campos de texto (textoId, textoNombre, textoPassword, textoApellido y textoDireccion) en cadenas vacías 
y el cuadro de comentarios (cuadroComentarios) se borra desde el primer carácter hasta el final (1.0, END). 
Esta función se usa para limpiar los campos de un formulario antes de ingresar nuevos datos.
"""
def Borrar_campos():

    textoId.set("")
    textoNombre.set("")
    textoPassword.set("")
    textoApellido.set("")
    textoDireccion.set("")
    #Para borrar el apartado comentarios
    cuadroComentarios.delete(1.0, END) #Desde el primer caracter hasta el final


#-----------------Tercer Apartado------------------------------------------------


"""
Esta función se encarga de crear una conexión con la base de datos "Usuarios" utilizando el módulo sqlite3. 
Luego, el cursor es usado para ejecutar la sentencia INSERT INTO, la cual inserta los datos recogidos de los 
campos de la interfaz de usuario. 
Por último, se utiliza el método commit para confirmar la inserción de los datos y mostrar un mensaje de éxito.
"""
def Crear():
    miConexion = sqlite3.connect("Usuarios")

    miCursor = miConexion.cursor()

    datos = textoNombre.get(),textoPassword.get(),textoApellido.get(),textoDireccion.get(),cuadroComentarios.get("1.0",END) #Variable donde se almacenan los datos recogidos

    miCursor.execute("INSERT INTO DATOUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos)) #Evita injeccion sql, un interrogante por cada campo
    
    miConexion.commit()

    messagebox.showinfo("BBDD","Registro insertado con éxito")


"""
Esta función lee los datos de una base de datos de usuarios. 
Utiliza la librería sqlite3 para conectarse a la base de datos 
"Usuarios" y crea un cursor para ejecutar una consulta SQL.

La consulta selecciona todos los campos de la tabla "DATOUSUARIOS" 
donde el campo "ID" coincide con el valor almacenado en la variable 
"textoId". 

La consulta devuelve una lista con los resultados y los asigna 
a la variable "elusuario".

Luego, se recorre la lista en un bucle "for" y se asignan los valores
de cada campo a las variables de texto correspondientes. 

Finalmente, se guardan los cambios en la base de datos mediante 
la función "miConexion.commit()".
"""
def Leer():

    miConexion = sqlite3.connect("Usuarios")

    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOUSUARIOS WHERE ID=" + textoId.get())

    elusuario = miCursor.fetchall()

    for usuario in elusuario:

        textoId.set(usuario[0])
        textoNombre.set(usuario[1]) 
        textoPassword.set(usuario[2]) 
        textoApellido.set(usuario[3]) 
        textoDireccion.set(usuario[4]) 
        cuadroComentarios.insert("1.0", usuario[5])

    miConexion.commit()


"""
El código realiza una actualización en una base de datos relacional mediante el uso de la librería sqlite3. 
Esta función permite conectar con una base de datos llamada “Usuarios” y un cursor para interactuar con ella.
Los datos que se van a actualizar se recogen del texto de los cuadros de texto y se almacenan en una variable.
Después se realiza la consulta de actualización con los datos recogidos, donde se usan interrogantes para evitar la inyección SQL.
Por último se realiza el commit y se muestra un mensaje de confirmación de la actualización.
"""
def Actualizar():

    miConexion = sqlite3.connect("Usuarios")

    miCursor = miConexion.cursor()

    datos = textoNombre.get(),textoPassword.get(),textoApellido.get(),textoDireccion.get(),cuadroComentarios.get("1.0",END) #Variable donde se almacenan los datos recogidos

    miCursor.execute("UPDATE DATOUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?,COMENTARIOS=?" +
                      "WHERE ID=" + textoId.get(),(datos)) #Evita injeccion sql, un interrogante por cada campo

    miConexion.commit()

    messagebox.showinfo("BBDD","Registro actualizado con éxito")


"""
Este código define una función llamada Borrar_Usuario(). 
La función se conecta a una base de datos llamada Usuarios usando el módulo sqlite3. 
Luego, crea un cursor para ejecutar una sentencia SQL. 

La sentencia SQL se usa para eliminar un registro específico en la tabla DATOUSUARIOS 
basado en el valor recibido de la variable textoId. 

Por último, la función hace un commit de la operación de eliminación y muestra un 
mensaje de confirmación de que el registro se ha eliminado con éxito.
"""
def Borrar_Usuario():
    
    miConexion = sqlite3.connect("Usuarios")

    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM DATOUSUARIOS WHERE ID=" + textoId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD","Registro eliminado con éxito")


#--------------------------Apartado 4---------------------------------------


def Licencia():
    messagebox.showwarning("Esta licencia pertenece Angel Moreno")


def Acercade():
    messagebox.showinfo("BBDD","Creada por Angel Moreno")


#----------------------Inicio interfaz gráfica--------------------------


raiz=Tk()

raiz.title("tk")
#Menu superior creacion
barraMenu = Menu(raiz)

raiz.config(menu=barraMenu,width=300,height=300)


#--------------------------------------------Contenido Menu Superior---------------------


bbddMenu=Menu(barraMenu,tearoff = 0) #Para quitar la barra de los 3 puntitos
bbddMenu.add_command(label="Conectar",command=Connectar) 
bbddMenu.add_command(label="Salir",command=Salir)   

borrarMenu=Menu(barraMenu,tearoff = 0)
borrarMenu.add_command(label="Borrar campos",command=Borrar_campos)

crudMenu=Menu(barraMenu,tearoff = 0)
crudMenu.add_command(label="Crear",command=Crear)
crudMenu.add_command(label="Leer",command=Leer)
crudMenu.add_command(label="Actualizar",command=Actualizar)
crudMenu.add_command(label="Borrar",command=Borrar_Usuario)

ayudaMenu=Menu(barraMenu,tearoff = 0)
ayudaMenu.add_command(label="Licencia",command=Licencia)
ayudaMenu.add_command(label="Acerca de...",command=Acercade)

barraMenu.add_cascade(label="BBDD",menu=bbddMenu) #Primero especificamos el texto que queremos que tenga el recuadro y luego el elemento al que nos referimos
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

#------------------------------------Comienzo de campos---------------------------------------------------


#Tiene doble frame
miFrameinterior = Frame(raiz)
miFrameinterior.pack()

textoId = StringVar() #Para poder extraer el texto de los campos de texto y manipularlos
textoNombre = StringVar()
textoApellido = StringVar()
textoPassword = StringVar()
textoDireccion = StringVar()


#Cuadros de texto y label del frame interior
cuadroId = Entry(miFrameinterior, textvariable=textoId)
cuadroId.grid(row=0, column=1,padx=10,pady=10)

cuadroNombre = Entry(miFrameinterior, textvariable=textoNombre)
cuadroNombre.grid(row=1, column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="right")

cuadroPassword = Entry(miFrameinterior, textvariable=textoPassword)
cuadroPassword.grid(row=2, column=1,padx=10,pady=10)
cuadroPassword.config(show="*")

cuadroApellido = Entry(miFrameinterior, textvariable=textoApellido)
cuadroApellido.grid(row=3, column=1,padx=10,pady=10)

cuadroDireccion = Entry(miFrameinterior, textvariable=textoDireccion)
cuadroDireccion .grid(row=4, column=1,padx=10,pady=10)

#Scrollbar comentarios
cuadroComentarios = Text(miFrameinterior, width=16,height=5)
cuadroComentarios.grid(row=5,column=1,sticky="e", padx=10, pady=10)
labelComentarios = Label(miFrameinterior, text="Comentarios:")
labelComentarios.grid(row=5,column=0,sticky="e", padx=10, pady=10)
scrollVert = Scrollbar(miFrameinterior, command=cuadroComentarios.yview)
scrollVert.grid(row=5,column=2,sticky="nsew") #Para que se adapte al tamaño que le tocaria, ponemos el sticky nsew que serian los 4 punts cardinales

cuadroComentarios.config(yscrollcommand = scrollVert.set) #Para indicar en todo momento en que punto nos encontramos

#--------------------------Labels acompañantes------------------------


labelId= Label(miFrameinterior, text="Id:")
labelId.grid(row=0,column=0, sticky="e", padx=10, pady=10)

labelNombre= Label(miFrameinterior, text="Nombre:")
labelNombre.grid(row=1,column=0, sticky="e", padx=10, pady=10)

labelPassword = Label(miFrameinterior, text="Password:")
labelPassword.grid(row=2,column=0, sticky="e", padx=10, pady=10)

labelApellido = Label(miFrameinterior, text="Apellido:")
labelApellido.grid(row=3,column=0, sticky="e", padx=10, pady=10)

labelDireccion = Label(miFrameinterior, text="Dirección:")
labelDireccion.grid(row=4,column=0,sticky="e", padx=10, pady=10)

#-------------------------------------Botones-----------------------------

miFrameexterior=Frame(raiz)
miFrameexterior.pack()

botonCreate = Button(miFrameexterior,text="Create",command=Crear)
botonCreate.grid(row=1, column=0, sticky="e",padx=10,pady=10)

botonRead = Button(miFrameexterior,text="Read",command=Leer)
botonRead.grid(row=1,column=1, sticky="e",padx=10,pady=10)

botonUpdate = Button(miFrameexterior,text="Update",command=Actualizar)
botonUpdate.grid(row=1, column=2, sticky="e",padx=10,pady=10)

botonDelete = Button(miFrameexterior,text="Delete",command=Borrar)
botonDelete.grid(row=1, column=3, sticky="e",padx=10,pady=10) 
 
raiz.mainloop()

from tkinter import *
from tkinter import messagebox
import sqlite3

#---------------------Funciones----------------------------------
#--------------------Primer Apartado-----------------------------

def Salir():
    
    valorpregunta = messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?") #Para almacenar el valor true o false
    
    if valorpregunta==True: 
        raiz.destroy()

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


def Borrar_campos():

    textoId.set("")
    textoNombre.set("")
    textoPassword.set("")
    textoApellido.set("")
    textoDireccion.set("")
    #Para borrar el apartado comentarios
    cuadroComentarios.delete(1.0, END) #Desde el primer caracter hasta el final

#-----------------Tercer Apartado------------------------------------------------
def Crear():
    miConexion = sqlite3.connect("Usuarios")

    miCursor = miConexion.cursor()

    datos = textoNombre.get(),textoPassword.get(),textoApellido.get(),textoDireccion.get(),cuadroComentarios.get("1.0",END) #Variable donde se almacenan los datos recogidos

    miCursor.execute("INSERT INTO DATOUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos)) #Evita injeccion sql, un interrogante por cada campo
    
    """ 
    miCursor.execute("INSERT INTO DATOUSUARIOS VALUES(NULL,'" + textoNombre.get() + 
        "','" + textoPassword.get() +
        "','" + textoApellido.get() +
        "','" + textoDireccion.get() +
        "','" + cuadroComentarios.get("1.0",END) + "')")
    """
    

    miConexion.commit()

    messagebox.showinfo("BBDD","Registro insertado con éxito")

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

def Actualizar():

    miConexion = sqlite3.connect("Usuarios")

    miCursor = miConexion.cursor()

    datos = textoNombre.get(),textoPassword.get(),textoApellido.get(),textoDireccion.get(),cuadroComentarios.get("1.0",END) #Variable donde se almacenan los datos recogidos

    """     
        miCursor.execute("UPDATE DATOUSUARIOS SET NOMBRE_USUARIO='" + textoNombre.get() +
        "', PASSWORD='" + textoPassword.get() +
        "', APELLIDO='" + textoApellido.get() +
        "', DIRECCION='" + textoDireccion.get() +
        "', COMENTARIOS='" + cuadroComentarios.get("1.0",END) +
        "' WHERE ID=" + textoId.get()) 
    """

    datos = textoNombre.get(),textoPassword.get(),textoApellido.get(),textoDireccion.get(),cuadroComentarios.get("1.0",END) #Variable donde se almacenan los datos recogidos

    miCursor.execute("UPDATE DATOUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?,COMENTARIOS=?" +
                      "WHERE ID=" + textoId.get(),(datos)) #Evita injeccion sql, un interrogante por cada campo

    miConexion.commit()

    messagebox.showinfo("BBDD","Registro actualizado con éxito")


def Borrar():
    
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
crudMenu.add_command(label="Borrar",command=Borrar)

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
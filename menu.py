from tkinter import *

from tkinter.filedialog import askopenfile

import os

class Mi_ventan(Frame):
    

    def __init__(self, master=None):
        super().__init__(master, width=620,height=370,bg='#04B45F')
        self.master=master
        self.pack()
        self.ventana_principal()

    def ventana_principal(self):

        self.boton_abrir=Button(self, text='Cargar archivo', bg='#BDBDBD', command=self.buscar_archivo)

        self.boton_afn=Button(self, text='AFN',bg='#BDBDBD', command=self.modulo_afn )
        self.boton_afd=Button(self,text='AFD',bg='#BDBDBD',command=self.modulo_afd)
        self.boton_OptimizacionE=Button(self,text='OE',bg='#BDBDBD', command=self.formulario_oe )
        self.boton_salir=Button(self,text='Salir',bg='#BDBDBD' , command=self.quit)

        self.boton_abrir.place(x=30, y=100,width=100, height=30 )
        self.boton_afn.place(x=30,y=150, width=100, height=30)
        self.boton_afd.place(x=30, y=200, width=100, height=30 )
        self.boton_OptimizacionE.place(x=480, y=100, width=100, height=30)
        self.boton_salir.place(x=480,y=150, width=100, height=30)
        #-----------Datos personales----------------

        self.label_curso=Label(self, text='Lab. Lenguajes Formales y de Programacion P')
        self.label_nombre=Label(self,text="Fernando Misael Morales Ortíz")
        self.label_carnet=Label(self, text='202001950')
      
        self.label_curso.place(x=150,y=100, width=300, height=35)
        self.label_nombre.place(x=150,y=150, width=300, height=35)
        self.label_carnet.place(x=150,y=200, width=250, height=35)
    
    def modulo_afd(self):
        ventana2=Toplevel()
        ventana2.title("Datos personales")
        ventana2.geometry("500x250")
        ventana2.config(bg='#04B45F')

        boton_crearAFD=Button(ventana2, text='Crear AFD',bg='#BDBDBD', command=self.formulario_afd )
        boton_evaluar=Button(ventana2, text='Evaluar cadena',bg='#BDBDBD' )
        boton_reporte=Button(ventana2, text='Generar Reporte',bg='#BDBDBD' )
        boton_ayuda=Button(ventana2, text='Ayuda',bg='#BDBDBD' )
        boton_salir=Button(ventana2, text='Salir',bg='#BDBDBD', command=ventana2.destroy )

        boton_crearAFD.place(x=120,y=50, width=100, height=30)
        boton_evaluar.place(x=120,y=90, width=100, height=30)
        boton_reporte.place(x=120,y=130, width=100, height=30)
        boton_ayuda.place(x=120,y=170, width=100, height=30)
        boton_salir.place(x=120,y=210, width=100, height=30)

    def modulo_afn(self):
        ventana3=Toplevel()
        ventana3.title("Datos personales")
        ventana3.geometry("500x250")
        ventana3.config(bg='#04B45F')

        boton_crearAFD=Button(ventana3, text='Crear AFD',bg='#BDBDBD',command=self.formulario_afn )
        boton_evaluar=Button(ventana3, text='Evaluar cadena',bg='#BDBDBD' )
        boton_reporte=Button(ventana3, text='Generar Reporte',bg='#BDBDBD' )
        boton_ayuda=Button(ventana3, text='Ayuda',bg='#BDBDBD' )
        boton_salir=Button(ventana3, text='Salir',bg='#BDBDBD', command=ventana3.destroy)

        boton_crearAFD.place(x=120,y=50, width=100, height=30)
        boton_evaluar.place(x=120,y=90, width=100, height=30)
        boton_reporte.place(x=120,y=130, width=100, height=30)
        boton_ayuda.place(x=120,y=170, width=100, height=30)
        boton_salir.place(x=120,y=210, width=100, height=30)
      
    def formulario_afn(self):
        ventana4=Toplevel()
        ventana4.title("Datos personales")
        ventana4.geometry("500x350")
        ventana4.config(bg='#04B45F')

        label_nombre=Label(ventana4, text="Nombre",bg='#BDBDBD')
        label_estados=Label(ventana4, text="Estados",bg='#BDBDBD')
        label_alfabeto=Label(ventana4, text="Alfabeto",bg='#BDBDBD')
        label_estadoI=Label(ventana4, text="Estado Inicial",bg='#BDBDBD')
        label_estadoAcep=Label(ventana4, text="Estados de aceptacion",bg='#BDBDBD')
        label_transicion=Label(ventana4, text="Transicion",bg='#BDBDBD')

        nombre=Entry(ventana4)
        estado=Entry(ventana4)
        alfabeto=Entry(ventana4)
        estadoI=Entry(ventana4)
        estadoAcep=Entry(ventana4)
        transicion=Entry(ventana4)

        label_nombre.place(x=75,y=5, width=120, height=30)
        label_estados.place(x=75,y=45, width=120, height=30)
        label_alfabeto.place(x=75,y=85, width=120, height=30)
        label_estadoI.place(x=75,y=125, width=120, height=30)
        label_estadoAcep.place(x=75,y=165, width=120, height=30)
        label_transicion.place(x=75,y=205, width=120, height=30)

        nombre.place(x=250,y=5, width=150, height=30)
        estado.place(x=250,y=45, width=150, height=30)
        alfabeto.place(x=250,y=85, width=150, height=30)
        estadoI.place(x=250,y=125, width=150, height=30)
        estadoAcep.place(x=250,y=165, width=150, height=30)
        transicion.place(x=250,y=205, width=150, height=30)

        boton_Guardar=Button(ventana4, text="Guardar")
        boton_Guardar.place(x=200, y=250, width=100, height=30)

    def formulario_afd(self):
        ventana6=Toplevel()
        ventana6.title("Datos personales")
        ventana6.geometry("500x350")
        ventana6.config(bg='#04B45F')

        label_nombre=Label(ventana6, text="Nombre",bg='#BDBDBD')
        label_estados=Label(ventana6, text="Estados",bg='#BDBDBD')
        label_alfabeto=Label(ventana6, text="Alfabeto",bg='#BDBDBD')
        label_estadoI=Label(ventana6, text="Estado Inicial",bg='#BDBDBD')
        label_estadoAcep=Label(ventana6, text="Estados de aceptacion",bg='#BDBDBD')
        label_transicion=Label(ventana6, text="Transicion",bg='#BDBDBD')

        nombre=Entry(ventana6)
        estado=Entry(ventana6)
        alfabeto=Entry(ventana6)
        estadoI=Entry(ventana6)
        estadoAcep=Entry(ventana6)
        transicion=Entry(ventana6)

        label_nombre.place(x=75,y=5, width=120, height=30)
        label_estados.place(x=75,y=45, width=120, height=30)
        label_alfabeto.place(x=75,y=85, width=120, height=30)
        label_estadoI.place(x=75,y=125, width=120, height=30)
        label_estadoAcep.place(x=75,y=165, width=120, height=30)
        label_transicion.place(x=75,y=205, width=120, height=30)

        nombre.place(x=250,y=5, width=150, height=30)
        estado.place(x=250,y=45, width=150, height=30)
        alfabeto.place(x=250,y=85, width=150, height=30)
        estadoI.place(x=250,y=125, width=150, height=30)
        estadoAcep.place(x=250,y=165, width=150, height=30)
        transicion.place(x=250,y=205, width=150, height=30)

        boton_Guardar=Button(ventana6, text="Guardar")
        boton_Guardar.place(x=200, y=250, width=100, height=30)

    def formulario_oe(self):
        ventana5=Toplevel()
        ventana5.title("Datos personales")
        ventana5.geometry("500x350")
        ventana5.config(bg='#04B45F')

        boton_seleccionar=Button(ventana5,text="Seleccionar AFD")
        boton_reporte=Button(ventana5, text="Generar reporte OE")

        boton_seleccionar.place(x=100, y=50, width=120, height=30)
        boton_reporte.place(x=100, y=100, width=120, height=30)

    def buscar_archivo(self):
      self.ventana=askopenfile(title="seleccione el archivo")
      print("se cargo el archivo")
      
      print('se cargo el archivo seleccionado')
        

root=Tk()
app=Mi_ventan(root)
app.mainloop()
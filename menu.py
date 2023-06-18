from tkinter import *

from tkinter.filedialog import askopenfilename
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 

import os
lis=[]
lis_nombre=[]
lis_estados=[]
lis_alfabeto=[]
lis_estadoI=[]
lis_estadosAcep=[]
lista_aux=[]
class Mi_ventan(Frame):
    

    def __init__(self, master=None):
        super().__init__(master, width=620,height=370,bg='#04B45F')
        self.master=master
        self.pack()
        self.ventana_principal()


    def ventana_principal(self):

        self.boton_abrir=Button(self, text='Cargar archivo', bg='#BDBDBD', command=self.ventana_seleccionar_archivo)

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
        boton_reporte=Button(ventana2, text='Generar Reporte',bg='#BDBDBD', command=self.generarPDF )
        boton_ayuda=Button(ventana2, text='Ayuda',bg='#BDBDBD' )
        boton_salir=Button(ventana2, text='Salir',bg='#BDBDBD', command=ventana2.destroy )

        curso2=Label(ventana2, text='Lab. Lenguajes Formales y de Programacion P')
        nombre2=Label(ventana2,text="Fernando Misael Morales Ortíz")
        carne2=Label(ventana2, text='202001950')

        curso2.place(x=200,y=75,width=290,height=35)
        nombre2.place(x=200,y=115,width=290,height=35)
        carne2.place(x=200,y=155,width=290,height=35)

        boton_crearAFD.place(x=75,y=50, width=100, height=30)
        boton_evaluar.place(x=75,y=90, width=100, height=30)
        boton_reporte.place(x=75,y=130, width=100, height=30)
        boton_ayuda.place(x=75,y=170, width=100, height=30)
        boton_salir.place(x=75,y=210, width=100, height=30)

    def modulo_afn(self):
        ventana3=Toplevel()
        ventana3.title("Datos personales")
        ventana3.geometry("500x250")
        ventana3.config(bg='#04B45F')

        boton_crearAFD=Button(ventana3, text='Crear AFD',bg='#BDBDBD',command=self.formulario_afn )
        boton_evaluar=Button(ventana3, text='Evaluar cadena',bg='#BDBDBD' )
        boton_reporte=Button(ventana3, text='Generar Reporte',bg='#BDBDBD',command=self.generarPDF_AFN )
        boton_ayuda=Button(ventana3, text='Ayuda',bg='#BDBDBD' )
        boton_salir=Button(ventana3, text='Salir',bg='#BDBDBD', command=ventana3.destroy)

        boton_crearAFD.place(x=75,y=50, width=100, height=30)
        boton_evaluar.place(x=75,y=90, width=100, height=30)
        boton_reporte.place(x=75,y=130, width=100, height=30)
        boton_ayuda.place(x=75,y=170, width=100, height=30)
        boton_salir.place(x=75,y=210, width=100, height=30)

        curso2=Label(ventana3, text='Lab. Lenguajes Formales y de Programacion P')
        nombre2=Label(ventana3,text="Fernando Misael Morales Ortíz")
        carne2=Label(ventana3, text='202001950')

        curso2.place(x=200,y=75,width=290,height=35)
        nombre2.place(x=200,y=115,width=290,height=35)
        carne2.place(x=200,y=155,width=290,height=35)
      
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

        self.nombre_afn=Entry(ventana4)
        self.estado_afn=Entry(ventana4)
        self.alfabeto_afn=Entry(ventana4)
        self.estadoI_afn=Entry(ventana4)
        self.estadoAcep_afn=Entry(ventana4)
        self.transicion_afn=Text(ventana4)

        label_nombre.place(x=75,y=5, width=120, height=30)
        label_estados.place(x=75,y=45, width=120, height=30)
        label_alfabeto.place(x=75,y=85, width=120, height=30)
        label_estadoI.place(x=75,y=125, width=120, height=30)
        label_estadoAcep.place(x=75,y=165, width=120, height=30)
        label_transicion.place(x=75,y=205, width=120, height=30)

        self.nombre_afn.place(x=250,y=5, width=150, height=30)
        self.estado_afn.place(x=250,y=45, width=150, height=30)
        self.alfabeto_afn.place(x=250,y=85, width=150, height=30)
        self.estadoI_afn.place(x=250,y=125, width=150, height=30)
        self.estadoAcep_afn.place(x=250,y=165, width=150, height=30)
        self.transicion_afn.place(x=250,y=205, width=150, height=40)

        boton_Guardar=Button(ventana4, text="Guardar",command=self.imprimir)
        boton_Guardar.place(x=200, y=250, width=100, height=30)


    def recogerDatos_afn(self):
        
        nombre1=self.nombre_afn.get()
        estados1=self.estado_afn.get()
        alfabeto1=self.alfabeto_afn.get()
        estadoI1=self.estadoI_afn.get()
        estadoA1=self.estadoAcep_afn.get()
        trans1=self.transicion_afn.get()
        lista_aux.append(nombre1)
        lista_aux.append(estados1)
        lista_aux.append(alfabeto1)
        lista_aux.append(estadoI1)
        lista_aux.append(estadoA1)
        lista_aux.append(trans1)

        lis.append(lista_aux)

    def imprimir(self):
        for i in lis:
            print(i)

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

        self.nombre=Entry(ventana6)
        estado=Entry(ventana6)
        alfabeto=Entry(ventana6)
        estadoI=Entry(ventana6)
        estadoAcep=Entry(ventana6)
        transicion=Text(ventana6)

        label_nombre.place(x=75,y=5, width=120, height=30)
        label_estados.place(x=75,y=45, width=120, height=30)
        label_alfabeto.place(x=75,y=85, width=120, height=30)
        label_estadoI.place(x=75,y=125, width=120, height=30)
        label_estadoAcep.place(x=75,y=165, width=120, height=30)
        label_transicion.place(x=75,y=205, width=120, height=40)

        self.nombre.place(x=250,y=5, width=150, height=30)
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

        boton_seleccionar.place(x=75, y=75, width=120, height=30)
        boton_reporte.place(x=75, y=125, width=120, height=30)

        curso2=Label(ventana5, text='Lab. Lenguajes Formales y de Programacion P')
        nombre2=Label(ventana5,text="Fernando Misael Morales Ortíz")
        carne2=Label(ventana5, text='202001950')

        curso2.place(x=200,y=75,width=290,height=35)
        nombre2.place(x=200,y=115,width=290,height=35)
        carne2.place(x=200,y=155,width=290,height=35)
        

    def ventana_seleccionar_archivo(self):
        ventana_abrir=Toplevel()
        ventana_abrir.geometry("500x350")
        ventana_abrir.config(bg='#04B45F')

        boton_afn=Button(ventana_abrir,text="Seleccionar AFD",command=self.buscar_archivo)
        boton_afd=Button(ventana_abrir, text="Seleccionar AFN", command=self.buscar_archivo2)
        boton_regresar=Button(ventana_abrir, text="Regresar",command=ventana_abrir.destroy)

        boton_afn.place(x=100, y=50, width=120, height=30)
        boton_afd.place(x=100, y=100, width=120, height=30)
        boton_regresar.place(x=100,y=170,width=120, height=30)


    def buscar_archivo(self):
        
        try:
            self.file = askopenfilename(title="Cargar un archivo", filetypes=[("Archivos", f'*.afd')])
            self.text = self.file
            self.openfile = open(self.text, encoding="utf-8")
            self.archivo = self.openfile.read().split("\n")
            
            for lineas in self.archivo:
                #archivo2=lineas.split("\n")
                lis.append(lineas)

        except:
            print('Error, no se ha seleccionado ningún archivo')

    def buscar_archivo2(self):
      
        try:
            self.file = askopenfilename(title="Cargar un archivo", filetypes=[("Archivos", f'*.afn')])
            self.text = self.file
            self.openfile = open(self.text, encoding="utf-8")
            self.archivo = self.openfile.read().split("\n")
            
            
            for lineas in self.archivo:
                
                lis_nombre.append(lineas)
            
        except:
            print('Error, no se ha seleccionado ningún archivo')

    def generarDOT(self):
        dot = Digraph('AFD', filename='AFDPrueba', format='png')
        dot.attr(rankdir='LR', size='8,5')
        dot.attr('node', shape='doublecircle')
        dot.node('B')
        dot.attr('node', shape='circle')
        dot.node('A')
        dot.edge('A', 'B', label='1') # A,1;B
        dot.render('AFDPrueba', view=False)

    def generarPDF(self):
        w, h = A4
        pdf = canvas.Canvas("ReporteAFD.pdf", pagesize=A4)
        pdf.setTitle("Reporte de AFD")
        text = pdf.beginText(50, h - 50)
        text.setFont("Times-Roman", 12)

        aux=0
        indice=0
        
        while aux < len(lis):
            elemento=lis[aux]
            if indice==0:
                text.textLine(elemento)
                
            indice +=1
            if indice==1:
                text.textLine("Alfabeto: "+elemento)
            if indice==2:
                text.textLine("Estados: "+elemento)
            if indice==3:
                text.textLine("Estado inicial: "+elemento)
            if indice==4:
                text.textLine("Estado final: "+elemento)
                text.textLine("Transiciones:")
            if indice>4 and elemento !="%":
                text.textLine(elemento)
            
            if elemento== "%":
                indice=0
                text.textLine()
 
            aux+=1
        text.textLine()
        text.textLine("AFD generado con Graphviz")
        pdf.drawText(text)
        
        pdf.save()
        webbrowser.open_new_tab('ReporteAFD.pdf')
        
    def generarPDF_AFN(self):
        w, h = A4
        pdf = canvas.Canvas("ReporteAFN.pdf", pagesize=A4)
        pdf.setTitle("Reporte de AFN")
        text = pdf.beginText(50, h - 50)
        text.setFont("Times-Roman", 12)

        aux=0
        indice=0
        
        while aux < len(lis_nombre):
            elemento=lis_nombre[aux]
            if indice==0:
                text.textLine(elemento)
            indice +=1
            if indice==1:
                text.textLine("Alfabeto: "+elemento)
            if indice==2:
                text.textLine("Estados: "+elemento)
            if indice==3:
                text.textLine("Estado inicial: "+elemento)
            if indice==4:
                text.textLine("Estado final: "+elemento)
                text.textLine("Transiciones:")
            if indice>4 and elemento !="%":
                text.textLine(elemento)
            
            if elemento== "%":
                indice=0
                text.textLine()
     
            aux+=1
        text.textLine()
        text.textLine("AFD generado con Graphviz")
        pdf.drawText(text)
        
        pdf.save()
        webbrowser.open_new_tab('ReporteAFN.pdf')

root=Tk()
app=Mi_ventan(root)
app.mainloop()
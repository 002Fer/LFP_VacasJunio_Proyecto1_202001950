from tkinter import *

import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 

import os
lis=[] #para guardar el archivo de entrada AFD
lis_nombre=[] #para guardar el archivo de entrada AFN


lista_nuevos=[]
lista_nuevos2=[]

lista_estados=[] #lista para separar los estados
nueva_lista = [] #lista para las transiciones

lista_estadosAFN=[] #lista para separar los estados
nueva_listaAFN = [] #lista para las transiciones
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
        boton_ayuda=Button(ventana2, text='Ayuda',bg='#BDBDBD',command=self.ejemplo_afd )
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
        

        aux=0
        indice=0
        listaa_a=[]
        while aux < len(lis):
            elemento=lis[aux]
            if indice==0:
                indice+=1
            elif indice==1:
                listaa_a.append(elemento)
                indice+=1
            elif indice>1 and indice<=4:
                indice +=1

            elif indice>4 and elemento !="%":
                lista_nuevos.append(elemento)
                indice +=1
            elif elemento== "%":
                indice=0
       
            aux+=1

        for elemento2 in lista_nuevos:
            elementos_separados = elemento2.replace(",", ";").split(";")
            
            nueva_lista.extend(elementos_separados)
            nueva_lista.append("#")
           
        
        for elemento3 in listaa_a:
            elementos_separados2 = elemento3.split(",")
            
            lista_estados.extend(elementos_separados2)
            lista_estados.append("#")
            
        
        print(nueva_lista)
        print(lista_estados)
        self.generarGraficas()
       

    def modulo_afn(self):
        ventana3=Toplevel()
        ventana3.title("Datos personales")
        ventana3.geometry("500x250")
        ventana3.config(bg='#04B45F')

        boton_crearAFD=Button(ventana3, text='Crear AFD',bg='#BDBDBD',command=self.formulario_afn )
        boton_evaluar=Button(ventana3, text='Evaluar cadena',bg='#BDBDBD' )
        boton_reporte=Button(ventana3, text='Generar Reporte',bg='#BDBDBD',command=self.generarPDF_AFN )
        boton_ayuda=Button(ventana3, text='Ayuda',bg='#BDBDBD',command=self.ejemplo_afn )
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

        aux=0
        indice=0
        listaa_a=[]
        while aux < len(lis_nombre):
            elemento=lis_nombre[aux]
            if indice==0:
                indice+=1
            elif indice==1:
                listaa_a.append(elemento)
                indice+=1
            elif indice>1 and indice<=4:
                indice +=1

            elif indice>4 and elemento !="%":
                lista_nuevos.append(elemento)
                indice +=1
            elif elemento== "%":
                indice=0
       
            aux+=1

        for elemento2 in lista_nuevos:
            elementos_separados = elemento2.replace(",", ";").split(";")
            
            nueva_listaAFN.extend(elementos_separados)
            nueva_listaAFN.append("#")
           
        
        for elemento3 in listaa_a:
            elementos_separados2 = elemento3.split(",")
            
            lista_estadosAFN.extend(elementos_separados2)
            lista_estadosAFN.append("#")
            
        
        print(nueva_listaAFN)
        print(lista_estadosAFN)
        self.generarGraficasAFN()
      
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

        boton_Guardar=Button(ventana4, text="Guardar")
        boton_Guardar.place(x=200, y=250, width=100, height=30)


    def recogerDatos_afn(self):
        
        nombre1=self.nombre_afn.get()
        estados1=self.estado_afn.get()
        alfabeto1=self.alfabeto_afn.get()
        estadoI1=self.estadoI_afn.get()
        estadoA1=self.estadoAcep_afn.get()
        trans1=self.transicion_afn.get()
        lis_nombre.extend(nombre1)
        lis_nombre.extend(estados1)
        lis_nombre.extend(alfabeto1)
        lis_nombre.extend(estadoI1)
        lis_nombre.extend(estadoA1)
        lis_nombre.extend(trans1)
        print("informacion guardad")

        tkinter.messagebox.showinfo("Guardado","Se guardado el nuevo elemento")

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
            
            tkinter.messagebox.showinfo("Archivo","Se cargo el archivo")
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
            tkinter.messagebox.showinfo("Archivo","Se cargo el archivo")
            
        except:
            print('Error, no se ha seleccionado ningún archivo')

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
                text.textLine("Nombre "+elemento)
                indice +=1
            elif indice==1:
                text.textLine("Alfabeto: "+elemento)
                indice +=1
            elif indice==2:
                text.textLine("Estados: "+elemento)
                indice +=1
            elif indice==3:
                text.textLine("Estado inicial: "+elemento)
                indice +=1
            elif indice==4:
                text.textLine("Estado final: "+elemento)
                text.textLine("Transiciones:")
                indice +=1
            elif indice>4 and elemento !="%":
                text.textLine(elemento)
                indice +=1
            elif elemento== "%":
                indice=0
                text.textLine()
            
        
            aux+=1
            
        text.textLine()
        text.textLine("AFD generado con Graphviz")
        pdf.drawText(text)
        pdf.drawInlineImage("AFDPrueba2.png", 100, 0, width=200, height=400, preserveAspectRatio=True)
        
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
            
            elif indice==1:
                text.textLine("Alfabeto: "+elemento)
                indice +=1
            elif indice==2:
                text.textLine("Estados: "+elemento)
                indice +=1
            elif indice==3:
                text.textLine("Estado inicial: "+elemento)
                indice +=1
            elif indice==4:
                text.textLine("Estado final: "+elemento)
                text.textLine("Transiciones:")
                indice +=1
            elif indice>4 and elemento !="%":
                text.textLine(elemento)
                indice +=1

            elif elemento== "%":
                indice=0
                text.textLine()
     
            aux+=1
        text.textLine()
        text.textLine("AFD generado con Graphviz")
        pdf.drawText(text)

        pdf.drawInlineImage("AFDPrueba3.png", 100, 0, width=200, height=700, preserveAspectRatio=True)
        pdf.save()
        webbrowser.open_new_tab('ReporteAFN.pdf')

                
    def generarGraficas(self):

        dot = Digraph('AFD', filename='AFDPrueba2', format='png')
        dot.attr(rankdir='LR', size='8,5')

        aux=0
        indice=0

        while aux < len(lista_estados):
            elemento=lista_estados[aux]
            if indice<=0 and elemento!="#" :
                dot.attr('node', shape='circle')
                dot.node(elemento)
                indice +=1

            elif elemento== "#":
                indice=0

            aux+=1
        aux2=0
        indice2=0
        while aux2< len(nueva_lista):
            elementoss=nueva_lista[aux2]

            if indice2==0:
                inicio=elementoss
                indice2 +=1
            if indice2==1:
                transicion=elementoss
                indice2 +=1
            if indice2==2:
                final=elementoss
                indice2 +=1
            if elementoss=="#":
                dot.edge(inicio, final, label=transicion)
                indice2=0
            aux2 +=1



        dot.render('AFDPrueba2', view=False)

    def generarGraficasAFN(self):

        dot = Digraph('AFD', filename='AFDPrueba3', format='png')
        dot.attr(rankdir='LR', size='8,5')

        aux=0
        indice=0

        while aux < len(lista_estadosAFN):
            elemento=lista_estadosAFN[aux]
            if indice<=0 and elemento!="#" :
                dot.attr('node', shape='circle')
                dot.node(elemento)
                indice +=1

            elif elemento== "#":
                indice=0

            aux+=1
        aux2=0
        indice2=0

        while aux2< len(nueva_listaAFN):
            elementoss=nueva_listaAFN[aux2]

            if indice2==0:
                inicio=elementoss
                indice2 +=1
            if indice2==1:
                transicion=elementoss
                indice2 +=1
            if indice2==2:
                final=elementoss
                indice2 +=1
            if elementoss=="#":
                dot.edge(inicio, final, label=transicion)
                indice2=0
            aux2 +=1



        dot.render('AFDPrueba3', view=False)
    def ejemplo_afn(self):
        w, h = A4
        pdf = canvas.Canvas("EjemploAFN.pdf", pagesize=A4)
        pdf.setTitle("Reporte de AFN")
        text = pdf.beginText(50, h - 50)
        text.setFont("Times-Roman", 12)
        text.textLine("AFN")
        text.textLine("Un autómata finito no determinista es un modelo computacional en el cual puede tener multiples ")
        text.textLine("opciones para poder hacer una transicion a otro estado y tambien permite transiciones con epsilon")
        text.textLine("permitiendo que el autómata se mueva de un estado a otro sin consumir un símbolo de entrada")
        text.textLine("pero un punto negativo es que es mas dificiles de analizar al tener muchas transiciones.")
        text.textLine("Alfabeto: x")
        text.textLine("Estados: A, B, C")
        text.textLine("Estado inicial: A")
        text.textLine("Estado final: B")
        text.textLine("Transiciones:")
        text.textLine("A,X;B")
        text.textLine("A,1;C")
        text.textLine("C,Ɛ;B")
        text.textLine()
        
        pdf.drawText(text)
        pdf.drawInlineImage("ejemploAFN.PNG", 100, 0, width=200, height=200, preserveAspectRatio=True)
        pdf.save()
        webbrowser.open_new_tab('EjemploAFN.pdf')

    def ejemplo_afd(self):
        w, h = A4
        pdf = canvas.Canvas("EjemploAFD.pdf", pagesize=A4)
        pdf.setTitle("Reporte de AFD")
        text = pdf.beginText(50, h - 50)
        text.setFont("Times-Roman", 12)
        text.textLine("AFN")
        text.textLine("Un autómata finito determinista es un modelo computacional con transiciones deterministas y un comportamiento  ")
        text.textLine("predecible porque para hacer una transicion a otro estado solo admite una unica entrada")
        text.textLine("es bastante facil de comprender e ideal para el diseño de algoritmos rapidos. ")
        text.textLine("Alfabeto: a, b")
        text.textLine("Estados: q0, q1, q2")
        text.textLine("Estado inicial: q0")
        text.textLine("Estado final: q2")
        text.textLine("Transiciones:")
        text.textLine("q0,a;q1")
        text.textLine("q1,b;q2")
        text.textLine("q2,b;q1")
        text.textLine()
        
        pdf.drawText(text)
        pdf.drawInlineImage("ejemploAFD.PNG", 100, 0, width=200, height=200, preserveAspectRatio=True)
        pdf.save()
        webbrowser.open_new_tab('EjemploAFD.pdf')
root=Tk()
app=Mi_ventan(root)
app.mainloop()
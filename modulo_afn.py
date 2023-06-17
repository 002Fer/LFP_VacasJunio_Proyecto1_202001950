from tkinter import *
from modulo_afd import listasimple
from tkinter.filedialog import askopenfilename
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 
def generarDOT():
    dot = Digraph('AFD', filename='AFDPrueba', format='png')
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', shape='doublecircle')
    dot.node('B')
    dot.attr('node', shape='circle')
    dot.node('A')
    dot.edge('A', 'B', label='1') # A,1;B
    dot.render('AFDPrueba')

def mostrarDOT():
    webbrowser.open_new_tab('AFDPrueba.png')

b=[["afd1"],["a,b,c,d"],["A"]]
a=[]
for a in b:
    a.append(a)
    print(a)
def generarPDF():
    w, h = A4
    pdf = canvas.Canvas("Reporte.pdf", pagesize=A4)
    pdf.setTitle("Reporte de AFD")
    text = pdf.beginText(50, h - 50)
    text.setFont("Times-Roman", 12)
    indice = 0

    while indice < len(a):
        elemento = a[indice]
        text.textLine(elemento)
        indice += 1
    
    text.textLine("Alfabeto: ")
    text.textLine("Estados: A, B")
    text.textLine("Estado inicial: A")
    text.textLine("Estado final: B")
    text.textLine("Transiciones:")
    text.textLine("A,1;B")
    text.textLine()
    text.textLine("AFD generado con Graphviz")
    pdf.drawText(text)
    
    pdf.save()
    webbrowser.open_new_tab('Reporte.pdf')


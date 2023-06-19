
from graphviz import Digraph
import webbrowser


lis_nombre = ["A,1;A", "A,0;B", "B,1;C"]

nueva_lista = []

for elemento in lis_nombre:
    elementos_separados = elemento.replace(",", ";").split(";")
    nueva_lista.extend(elementos_separados)

print(nueva_lista)
print(len(nueva_lista))
def generarDOT():
    dot = Digraph('AFD', filename='AFDPrueba', format='png')
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', shape='doublecircle')
    dot.node('Bzzzzz')
    dot.attr('node', shape='circle')
    dot.node('A')
    dot.attr('node', shape='circle')
    dot.node('C')
    dot.attr('node', shape='circle')
    dot.node('D')
    dot.edge("A", "B", label="")
    dot.edge("C", "x", label="")

    aux=0
    indice=0
    while aux< len(nueva_lista):
        elementoss=nueva_lista[aux]

        if indice==0:
            inicio=elementoss
            print(inicio)
        if indice==1:
            transicion=elementoss
            print(transicion)
        if indice==2:
            final=elementoss
            print(final)
        if indice==3:
            dot.edge(inicio, final, label=transicion)
            indice=0
        aux +=1

         # A,1;B
    dot.render('AFDPrueba', view=True)



generarDOT()

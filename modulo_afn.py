
from graphviz import Digraph
import webbrowser
  
a="7"
def generarDOT():
    dot = Digraph('AFD', filename='AFDPrueba', format='png')
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', shape='doublecircle')
    dot.node('B')
    dot.attr('node', shape='circle')
    dot.node('A')
    dot.edge('A', 'B', label=a) # A,1;B
    dot.render('AFDPrueba', view=False)

def mostrarDOT():
    webbrowser.open_new_tab('AFDPrueba.png')

generarDOT()
mostrarDOT()
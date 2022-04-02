import PySimpleGUI  as sg

layout = [[sg.Button('Hello, new Stack', size=(30,4))]]
window = sg.Window('Gui Sample', layout, size=(200,200))
event, values = window.read()

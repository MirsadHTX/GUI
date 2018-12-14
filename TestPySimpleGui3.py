import PySimpleGUI
import random

layoutKonfiguration = [[PySimpleGUI.Text('Mirsad Random')],
                      [PySimpleGUI.Text('', key="NavnPaaText")],
                      [PySimpleGUI.Yes(), PySimpleGUI.Exit()]]

window = PySimpleGUI.Window('Mirsads vinduet').Layout(layoutKonfiguration)


while True:
    button, values = window.ReadNonBlocking()
    randTal = random.randint(-5,5)
    window.FindElement("NavnPaaText").Update(randTal)
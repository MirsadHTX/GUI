import PySimpleGUI

layout = [[PySimpleGUI.Text('Persistent window')],
          [PySimpleGUI.Input()],
          [PySimpleGUI.RButton('Read'), PySimpleGUI.Exit()]]

window = PySimpleGUI.Window('Window that stays open').Layout(layout)


while True:
    button, values = window.Read()
    if button is None or button == 'Exit':
        break
    print(button, values)
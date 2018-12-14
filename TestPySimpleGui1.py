import PySimpleGUI
#layout = [
#          [PySimpleGUI.Text('Please enter your Name, Address, Phone')],
#          [PySimpleGUI.Text('Name', size=(15, 1)), PySimpleGUI.InputText()],
#          [PySimpleGUI.Text('Address', size=(15, 1)), PySimpleGUI.InputText()],
#          [PySimpleGUI.Text('Phone', size=(15, 1)), PySimpleGUI.InputText(size=(15, 1))],
#          [PySimpleGUI.Submit(), PySimpleGUI.Cancel(),PySimpleGUI.Yes(),PySimpleGUI.No()],
#          [PySimpleGUI.Submit(), PySimpleGUI.Cancel(),PySimpleGUI.Yes(),PySimpleGUI.No()]
#         ]


layout = [[PySimpleGUI.Text('Persistent window')],
          [PySimpleGUI.Text('Name', size=(15, 1)), PySimpleGUI.InputText()],
          [PySimpleGUI.Text('Address', size=(15, 1)), PySimpleGUI.InputText()],
          [PySimpleGUI.Text('Phone', size=(15, 1)), PySimpleGUI.InputText(size=(15, 1))],
          [PySimpleGUI.RButton('Mirsad'), PySimpleGUI.RButton('MirsadIgen'), PySimpleGUI.Yes(), PySimpleGUI.No()]]


window = PySimpleGUI.Window('Simple data entry window').Layout(layout)


while True:
    button, values = window.ReadNonBlocking()
    #if button is None or button == 'Exit':
    #    break
    print(button, values)



#PySimpleGUI.Popup('The GUI returned:', knapper, verdier)
#print( verdier[1]), verdier[1], verdier[2])
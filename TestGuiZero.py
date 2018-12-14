import guizero


def KaldMinFunktion():
    guizero.Text(app, text="Mirsad!")


def slider_changedFunktion(slider_value):
    #guizero.Text(app, text=slider_value)
    #guizero.TextBox(app, slider_value )
    textBoxVar.value = slider_value


app = guizero.App(title="Min vindue")
guizero.Text(app, text="Welcome to the Hello world app!")
guizero.PushButton(app, command=KaldMinFunktion)
textBoxVar = guizero.TextBox(app)
guizero.Slider(app, command=slider_changedFunktion)


app.display()
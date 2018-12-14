from guizero import App, Text, TextBox, PushButton

# Method to display the greeting
def display_greeting():
   text.value = "Hello " + name.value

# Set up the app
app = App("Hello machine")

text = Text(app, text="What is your name?")
name = TextBox(app)
button = PushButton(app, display_greeting, text="Greet me")

app.display()

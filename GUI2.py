import tkinter

minVindue = tkinter.Tk()

frame = tkinter.Frame(minVindue, bg="black", height="200", width="20")
frame.pack()


greenButton = tkinter.Button(frame, text="Hej grøn", fg="green")
greenButton.pack( side = tkinter.TOP )

redButton = tkinter.Button(frame, text="Hej rød", fg="red")
redButton.pack( side = tkinter.TOP)

blueButton = tkinter.Button(frame, text="Hej blå", fg="blue")
blueButton.pack( side = tkinter.TOP)


minVindue.mainloop()
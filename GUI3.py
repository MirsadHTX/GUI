import tkinter

minVindue = tkinter.Tk()

frame1 = tkinter.Frame(minVindue, bg="black", height="200", width="20")
frame1.pack()
frame2 = tkinter.Frame(minVindue, bg="green")
frame2.pack( side = tkinter.LEFT)

greenButton = tkinter.Button(frame1, text="Hej grøn", fg="green")
greenButton.pack( side = tkinter.TOP )
redButton = tkinter.Button(frame1, text="Hej rød", fg="red")
redButton.pack( side = tkinter.TOP)


blueButton = tkinter.Button(frame2, text="Hej blå         ", fg="blue")
blueButton.pack( side = tkinter.TOP)
blueButton2 = tkinter.Button(frame2, text="Hej blå", fg="blue")
blueButton2.pack( side = tkinter.TOP)


minVindue.mainloop()
import tkinter

minVindue = tkinter.Tk()

frame1 = tkinter.Frame(minVindue, bg="black")
frame1.pack(side = tkinter.TOP)
frame2 = tkinter.Frame(minVindue, bg="green")
frame2.pack()
frame3 = tkinter.Frame(minVindue)
frame3.pack( side = tkinter.LEFT)


greenButton = tkinter.Button(frame1, text="Hej grøn", fg="green")
greenButton.pack( side = tkinter.TOP )
redButton = tkinter.Button(frame1, text="Hej rød", fg="red")
redButton.pack( side = tkinter.TOP)

blueButton = tkinter.Button(frame2, text="Hej blå         ", fg="blue")
blueButton.pack( side = tkinter.TOP)
blueButton2 = tkinter.Button(frame2, text="Hej blå", fg="blue")
blueButton2.pack( side = tkinter.TOP)

textIn = tkinter.Entry(minVindue)
textIn.pack(side = tkinter.RIGHT)

minVindue.mainloop()
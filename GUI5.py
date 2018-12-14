import tkinter

minVindue = tkinter.Tk()

frame1 = tkinter.Frame(minVindue, bg="black")
frame1.grid(row = 0, column = 0)

frame2 = tkinter.Frame(minVindue, bg="blue")
frame2.grid(row = 0, column = 1)



greenButton = tkinter.Button(frame1, text="Hej grøn", fg="green")
greenButton.grid(row = 1, column = 1 )
redButton = tkinter.Button(frame1, text="Hej rød", fg="red")
redButton.grid(row = 1, column = 2 )
blueButton = tkinter.Button(frame1, text="Hej blå         ", fg="blue")
blueButton.grid(row = 2, column = 2 )
blueButton2 = tkinter.Button(frame1, text="Hej blå", fg="blue")
blueButton2.grid(row = 3, column = 3 )
textIn = tkinter.Entry(frame1)
textIn.grid(row = 1, column = 3 )



greenButton = tkinter.Button(frame2, text="Hej grøn", fg="green")
greenButton.grid(row = 1, column = 1 )
redButton = tkinter.Button(frame2, text="Hej rød", fg="red")
redButton.grid(row = 1, column = 2 )
blueButton = tkinter.Button(frame2, text="Hej blå         ", fg="blue")
blueButton.grid(row = 2, column = 2 )
blueButton2 = tkinter.Button(frame2, text="Hej blå", fg="blue")
blueButton2.grid(row = 3, column = 3 )
textIn = tkinter.Entry(frame2)
textIn.grid(row = 1, column = 3 )

minVindue.mainloop()
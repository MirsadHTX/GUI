import tkinter

minVindue = tkinter.Tk()

frame1 = tkinter.Frame(minVindue, bg="black")
frame1.grid(row = 0, column = 0)

frame2 = tkinter.Frame(minVindue, bg="blue")
frame2.grid(row = 0, column = 1)

frame3 = tkinter.Frame(minVindue, bg="yellow")
frame3.grid(row = 0, column = 2)



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

minCanvas1 = tkinter.Canvas(frame3, width=200, height=100)
minCanvas1.grid(row = 1, column = 1 )
minCanvas2 = tkinter.Canvas(frame3, width=200, height=100)
minCanvas2.grid(row = 1, column = 2 )

minCanvas1.create_line(0, 0, 200, 100)
minCanvas1.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

minCanvas2.create_rectangle(50, 25, 150, 75, fill="blue")

minVindue.mainloop()
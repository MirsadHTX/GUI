import tkinter

master = tkinter.Tk()

def callback():
    print ("click!")

b = tkinter.Button(master, text="OK", command=callback)
b.pack()

master.mainloop()
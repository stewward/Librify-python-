from tkinter import * #Imports everything from tkinter

window = Tk() #Creates a default window object

def km_to_miles():
    print("Converts!")

b1 = Button(window, text = "Press me", command=km_to_miles)
#b1.pack() Press button 
b1.grid(row = 0, column = 0)

#Creates entry (place/space to write words)
e1 = Entry(window)
e1.grid(row=0, column=1)

#Text widget can just display text and not to anything with it, unlike entry
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2) #adds to the grid

window.mainloop()

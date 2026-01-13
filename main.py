from tkinter import*
import matplotlib.pyplot as plt
import numpy as np
root = Tk()
button_1 = Button(root, text="process")
button_1.grid(row=1, column=0)


a1 = Entry(root, width=5, borderwidth=5)
a1.grid(row=0, column=0, padx=3, pady=10)
a1.insert(0, "x1")
a2 = Entry(root, width=5, borderwidth=5)
a2.grid(row=0, column=1, padx=3, pady=10)
a2.insert(0, "y1")
a3 = Entry(root, width=5, borderwidth=5)
a3.grid(row=0, column=2, padx=3, pady=10)
a3.insert(0, "x2")

a4 = Entry(root, width=5, borderwidth=5)
a4.grid(row=0, column=3, padx=3, pady=10)
a4.insert(0, "y2")

typeOfLine= Entry(root, width=50, borderwidth=5)
typeOfLine.grid(row=2, column=0,columnspan=5, padx=3, pady=10)




def buttonClick():
    x1= int(a1.get())
    y1=int (a2.get())
    x2= int(a3.get())
    y2=int (a4.get())
    if x1!=x2:
      m=(y2-y1)/(x2-x1)
      b=y1-m*x1
      x = np.linspace(-5, 5, 100)
      y=m*x+b

      eqn= " y=" + str(m)+ " x +" +str(b)

      plt.plot(x, y, '-r', label="y=mx+b")
    else:
      plt.figure(figsize = (10, 5))
      plt.axvline(x = x1, color = 'b', label = 'axvline - full height')
      eqn=str(x1)

    plt.title("Graph of " + eqn)
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

  

    typeOfLine.delete(0, END)
    typeOfLine.insert(0, "the equation of the line is: " + eqn)

button_1 = Button(root, text="process", command = buttonClick)  


button_1.grid(row=1, column=0)

root.mainloop()







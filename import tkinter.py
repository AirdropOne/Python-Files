import tkinter

root = tkinter.Tk()


for i in range (4):
    root.grid_columnconfigure[i](padx=10, pady=10)



label1 = tkinter.Label(root, text = "label 1", foreground = "white", background = "black")
label2 = tkinter.Label(root, text = "label 1", foreground = "white", background = "black")


label1.grid (row=0, column=0, padx = 10, pady = 10)
label2.grid (row=1, column=1, padx = 10, pady = 10)



tkinter.mainloop()



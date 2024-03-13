# from tkinter import *
# from tkinter import ttk
# from tkinter.ttk import *
# root = Tk()

# Label(root, text = 'Shakat', font =('Verdana', 15)).pack(side = TOP, pady = 10) 
# photo = PhotoImage(file = r"C:\Users\shavk\OneDrive\Рабочий стол\virus\rasm.jpg") 
# photoimage = photo.subsample(3, 3)

# # root.geometry('370x150')
# # style = Style()
# # style.configure('TButton', font = ('calibri', 20, 'bold', 'underline'), borderwidth = '4')

# # style.map('TButton', foreground = [('active', '!disabled', 'green')], background = [('active', 'black')])

# # btn1 = Button(root, text = 'Quit !', style = 'TButton', command = root.destroy)
# # btn1.grid(row = 0, column = 3, padx = 100)

# Button(root, text = 'Click me !', image = photoimage, compound = LEFT).pack(side = TOP)
# # btn2.grid(row = 1, column = 3, pady = 10, padx = 100)
# # frm = ttk.Frame(root, padding=10)
# # frm.grid()
# # ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# # ttk.Button(frm, text="Quit", command=root.destroy, fg="red", bg="blue").grid(column=1, row=0)
# root.mainloop()




from tkinter import *

root = Tk() 
root.geometry("600x500") 
v2 = DoubleVar() 
root.title("Zuvuk")
def show2(): 
	
	sel = "Vertical Scale Value = " + str(v2.get()) 
	l2.config(text = sel, font =("Courier", 14)) 

s2 = Scale( root, variable = v2, from_ = 50, to = 1, orient = VERTICAL)
l4 = Label(root, text = "Vertical Scaler") 

b2 = Button(root, text ="Display Vertical", command = show2, bg = "purple", fg = "white") 

l2 = Label(root) 

s2.pack(anchor = CENTER)
l4.pack() 
b2.pack() 
l2.pack() 

root.mainloop() 

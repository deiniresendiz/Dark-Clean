from tkinter import *
#from tkinter import scrolledtext
#from tkinter.ttk import *
#from tkinter import messagebox

window = Tk()

window.title("Dark Clean")

w = 900 # width for the Tk root
h = 550 # height for the Tk root

# get screen width and height
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.resizable(width=0, height=0)

# create all of the main containers
top_frame = Frame(window, bg='cyan', width=w, height=20, pady=3)
center = Frame(window, bg='gray2', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(window, bg='white', width=450, height=45, pady=3)
btm_frame2 = Frame(window, bg='lavender', width=450, height=60, pady=3)

# # layout all of the main containers
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
btm_frame2.grid(row=4, sticky="ew")

# # create the widgets for the top frame
# model_label = Label(top_frame, text='Model Dimensions')
# width_label = Label(top_frame, text='Width:')
# length_label = Label(top_frame, text='Length:')
# entry_W = Entry(top_frame, background="pink")
# entry_L = Entry(top_frame, background="orange")

# # layout the widgets in the top frame
# model_label.grid(row=0, columnspan=3)
# width_label.grid(row=1, column=0)
# length_label.grid(row=1, column=2)
# entry_W.grid(row=1, column=1)
# entry_L.grid(row=1, column=3)

# # create the center widgets
# center.grid_rowconfigure(0, weight=1)
# center.grid_columnconfigure(1, weight=1)

# ctr_left = Frame(center, bg='blue', width=100, height=190)
# ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
# ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3)

# ctr_left.grid(row=0, column=0, sticky="ns")
# ctr_mid.grid(row=0, column=1, sticky="nsew")
# ctr_right.grid(row=0, column=2, sticky="ns")

window.mainloop()
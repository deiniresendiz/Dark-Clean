from tkinter import *

root=Tk()
root.geometry("640x480")
root.title("Skroutz Parser")

#entryText=StringVar(root)
topFrame=Frame(root, bg='cyan', width = 640, height=80)
middleFrame=Frame(root,bg='gray2', width=640, height=400)
bottomFrame=Frame(root, bg='yellow', width = 640, height=50)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

topFrame.grid(row=0, column=0, sticky='ew')
middleFrame.grid(row=1, column=0, sticky='nsew')
bottomFrame.grid(row=2, column=0, sticky='ew')

# layout middle container
middleFrame.grid_rowconfigure(0, weight=1)
middleFrame.grid_columnconfigure(1, weight=1)

leftFrame=Frame(middleFrame, bg='green', width = 125, height=400)
rightFrame=Frame(middleFrame, bg='white', width = 515, height=400)

leftFrame.grid(row=0,column=0,sticky="nsew")
rightFrame.grid(row=0, column=1, sticky='nsew')

leftFrame.grid_columnconfigure(0, weight=1)
rightFrame.grid_rowconfigure(0, weight=1)
rightFrame.grid_columnconfigure(0, weight=1)

buttonFeatured=Button(leftFrame, text='   Recommended    ', pady=5)
buttonSkroutz=Button(leftFrame, text='Skroutz Products', pady=5)
buttonFeatured.grid(row=0, column=0, sticky="new")
buttonSkroutz.grid(row=1, column=0, sticky='new')

entryText=StringVar()
entryMain=Entry(rightFrame,textvariable=entryText, bg="white")
entryMain.grid(row=0,column=0,sticky="new")

root.mainloop()
from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askopenfilename ,asksaveasfile
import os

# functions
def newFile():
    global file
    root.title("Ultitled - Notepad")
    file=None
    textarea.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*"),("Text Documents","*.txt")])
    if file=="":
        file= None
    else:
        root.title(str(os.path.basename(file))+" - Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfile(defaultextension=".txt",filetypes=[("All Files","*"),("Text Documents","*.txt")])
        # save as a new file
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
        root.title(os.path.basename(file)+" - Notepad")
        print("File Saved")
    else:
        # save the file 
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()

def cut():
    textarea.event_generate(("<>"))
def copy():
    textarea.event_generate(("<>"))
def paste():
    textarea.event_generate(("<>"))
def about():
    showinfo("Notepad","Notepad created by Elite for personal use")

if __name__=="__main__":
    root = Tk()
    # window size
    root.title("Elite_notepad")
    root.geometry("600x400")

    # text area
    textarea=Text(root,font="lucida 13")
    file=None
    textarea.pack(expand=True,fill=BOTH)


    # main menu
    mainmenu=Menu(root)

    # File menu
    Filemenu=Menu(mainmenu,tearoff=0)
    # create new file
    Filemenu.add_command(label="New",command=newFile)
    # to open a existing file
    Filemenu.add_command(label="Open",command=openFile)
    # save file 
    Filemenu.add_command(label="Save",command=saveFile)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit",command=quit)
    mainmenu.add_cascade(label="File",menu=Filemenu)
    # edit menu 
    Editmenu=Menu(mainmenu,tearoff=0)
    Editmenu.add_command(label="Cut",command=cut)
    Editmenu.add_command(label="Copy",command=copy)
    Editmenu.add_command(label="Paste",command=paste)
    mainmenu.add_cascade(label="Edit",menu=Editmenu)
    # help menu 
    helpmenu=Menu(root,tearoff=0)
    helpmenu.add_command(label="About Notebook",command=about)
    mainmenu.add_cascade(label="Help",menu=helpmenu)

    root.config(menu=mainmenu)

    # adding Scrollbar
    Scroll =Scrollbar(textarea)
    Scroll.pack(side=RIGHT,fill=Y,padx=5)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)

    root.mainloop()
from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askopenfilename ,asksaveasfile
import os


# font and fontsize
font="Arial"
font_size=13

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
    textarea.event_generate("<Control-x>")
def copy():
    textarea.event_generate("<Control-c>")
def paste():
    textarea.event_generate("<Control-v>")
def select_all():
    textarea.tag_add(SEL, "1.0", END)

def change_font(temp_font):
    global font
    font=temp_font
def change_font_size(temp_font_size):
    global font_size
    font_size=temp_font_size


def about():
    showinfo("Notepad","Notepad created by Elite for personal use")

if __name__=="__main__":
    root = Tk()
    # window size
    root.title("Elite_notepad")
    root.geometry("900x600")
    root.minsize(900,200)

    # text area
    f1=Frame(root)
    f1.pack(side=LEFT,fill=BOTH,expand=True)
    textarea=Text(f1,font=f"{font} {font_size}")
    textarea.pack(expand=True,fill=BOTH)


    file=None


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
    Editmenu.add_command(label="Select All",command=select_all)
    # sub_font_menu 
    # sub_font_menu=Menu(Editmenu,tearoff=0)
    # # fonts 
    # sub_font_menu.add_command(label="Arial",command=change_font("Arial"))
    # sub_font_menu.add_command(label="Terminal",command=change_font("Terminal"))
    # sub_font_menu.add_command(label="Arial",command=change_font("Arial"))
    # sub_font_menu.add_command(label="Arial",command=change_font("Arial"))
    # sub_font_menu.add_command(label="Arial",command=change_font("Arial"))
    # sub_font_menu.add_command(label="Arial",command=change_font("Arial"))
    # # font list over
    # Editmenu.add_cascade(label="Fonts",menu=sub_font_menu)
    # # sub_font_size_menu 
    # sub_font_size_menu=Menu(Editmenu,tearoff=0)
    # # font size
    # Editmenu.add_cascade(label="Font Size",menu=sub_font_size_menu)
    # sub_font_size_menu.add_command(label="Arial",command=change_font_size(25))
    # sub_font_size_menu.add_command(label="Terminal",command=change_font_size(55))
    # # font size list over



    mainmenu.add_cascade(label="Edit",menu=Editmenu)


    # help menu 
    helpmenu=Menu(mainmenu,tearoff=0)
    helpmenu.add_command(label="About Notebook",command=about)
    mainmenu.add_cascade(label="Help",menu=helpmenu)
    
    root.config(menu=mainmenu)

    # adding Scrollbar
    Scroll =Scrollbar(root)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)

    root.mainloop()
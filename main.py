from tkinter import *
from tkinter import font
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
    textarea.event_generate("<Control-x>")
def copy():
    textarea.event_generate("<Control-c>")
def paste():
    textarea.event_generate("<Control-v>")
def select_all():
    textarea.tag_add(SEL, "1.0", END)
def Theme_dark():
    textarea.config(background="Black",fg="White")
def Theme_light():
    textarea.config(background="White",fg="Black")
def light_red():
    textarea.config(background="White",fg="Red")
def light_green():
    textarea.config(background="White",fg="Green")
def light_magenta():
    textarea.config(background="White",fg="Magenta")

def dark_cyan():
    textarea.config(background="Black",fg="Cyan")
def dark_yellow():
    textarea.config(background="Black",fg="Yellow")
def dark_red():
    textarea.config(background="Black",fg="Red")
def dark_green():
    textarea.config(background="Black",fg="Green")
def dark_magenta():
    textarea.config(background="Black",fg="Magenta")

def font_Courier():
    textarea.config(font=("Courier",13))
def font_Arial():
    textarea.config(font=("Arial",13))
def font_Roman():
    textarea.config(font=("Roman",13))
def font_Times_New_Roman():
    textarea.config(font=("Times New Roman",13))
def font_Impact():
    textarea.config(font=("Impact",13))


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
    textarea=Text(f1,font=("Ariel",13))
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
    Editmenu.add_command(label="Cut",command=cut,accelerator='Ctrl+X')
    Editmenu.add_command(label="Copy",command=copy,accelerator='Ctrl+C')
    Editmenu.add_command(label="Paste",command=paste,accelerator='Ctrl+V')
    Editmenu.add_command(label="Select All",command=select_all)
    mainmenu.add_cascade(label="Edit",menu=Editmenu)
    # Theme
    Theme_menu=Menu(mainmenu,tearoff=0)
    Theme_menu.add_command(label="Light",command=Theme_light)
    Theme_menu.add_command(label="Light Red",command=light_red)
    Theme_menu.add_command(label="Light Green",command=light_green)
    Theme_menu.add_command(label="Light Magenta",command=light_magenta)
    Theme_menu.add_command(label="Dark",command=Theme_dark)
    Theme_menu.add_command(label="Dark Cyan",command=dark_cyan)
    Theme_menu.add_command(label="Dark Magenta",command=dark_magenta)
    Theme_menu.add_command(label="Dark Yellow",command=dark_yellow)
    Theme_menu.add_command(label="Dark Red",command=dark_red)
    Theme_menu.add_command(label="Dark Green",command=dark_green)
    mainmenu.add_cascade(label="Theme",menu=Theme_menu)
    # font style
    Font_menu=Menu(mainmenu,tearoff=0)
    Font_menu.add_command(label="Courier",command=font_Courier)
    Font_menu.add_command(label="Arial",command=font_Arial)
    Font_menu.add_command(label="Roman",command=font_Roman)
    Font_menu.add_command(label="Times_New_Roman",command=font_Times_New_Roman)
    Font_menu.add_command(label="Impact",command=font_Impact)

    mainmenu.add_cascade(label="Font",menu=Font_menu)
    


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



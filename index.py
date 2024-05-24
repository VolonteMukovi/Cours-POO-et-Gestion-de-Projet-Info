from tkinter import *
import tkinter as tk
from tkinter import filedialog
from classes.Mes_class import ExtensionFileOrganizer


window = Tk()
window.geometry("800x500")
window.resizable(height=False,width=False)
window.title("Files Organizer")

framegauche = tk.Frame(window,width=400,height=800,bg="blue")
framegauche.pack_propagate(0)
framegauche.pack(side=LEFT,padx=5)

framedroite = tk.Frame(window,width=400,height=800,bg="white")
framedroite.pack_propagate(0)
framedroite.pack(side=RIGHT,padx=5)
mo_titre=Label(framedroite,text="BIENVENUE SUR FILES ORGANIZER",bg="black",fg="white",width="30")
mo_titre.place(x='110',y='20')

def select_folder():
    folder_path = filedialog.askdirectory()
    return folder_path

def organization():
    folder_path = filedialog.askdirectory()
    organize = ExtensionFileOrganizer()
    organize.organiser(folder_path)
    
texte = tk.Text(framegauche,wrap="word",bg="blue",fg="white")
texte.insert('1.0','    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Harum accusamus corporis maiores eos incidunt error quae totam autem ad fugiat voluptatum, sapiente labore neque aut amet. Perspiciatis tempora vero repellat     Lorem ipsum dolor sit, amet consectetur adipisicing elit. Harum accusamus corporis maiores eos incidunt error quae totam autem ad fugiat voluptatum, sapiente labore neque aut amet. Perspiciatis tempora vero repellat??')
texte.tag_configure('center',justify="center")
texte.tag_add("center",'1.0','end')
texte.pack(expand=True)

button = Button(framedroite,text="Selectionner un Dossier a Organisant",bg="blue",fg="white",command=organization)
button.place(x='110',y='200')
# button_org = Button(framedroite,text="Organise",bg="white",fg="blue",command=org)
# button_org.place(x='160',y='250')


window.mainloop()
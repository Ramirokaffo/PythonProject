from tkinter import *
from tkinter import ttk
from bd_service import MysqlConnectorToBd


BdManager = MysqlConnectorToBd()


def save_data_seance():
    nom_repetiteur_seance = nomRepetiteurChamps.get()
    classe_seance = classeRepetitionChamps.get()
    cours_seance = coursRepetitionChamps.get()


root = Tk()
root.title("Gestion des cours de repetition")
noteBookMere = ttk.Notebook(root)
panedAcceuil = PanedWindow(noteBookMere, orient=HORIZONTAL)
frameAcceuil = Frame(panedAcceuil, background="blue")
frameChampsRemplir = Frame(frameAcceuil)

nomRepetiteurLabel = Label(frameChampsRemplir, text="Nom: ")
nomRepetiteurLabel.grid(row=1, column=1)
nomRepetiteurChamps = ttk.Combobox(frameChampsRemplir, values=BdManager.select_all_professeur())
nomRepetiteurChamps.grid(row=1, column=2)

classeRepetitionLabel = Label(frameChampsRemplir, text="Classe repétée: ")
classeRepetitionLabel.grid(row=2, column=1)
classeRepetitionChamps = ttk.Combobox(frameChampsRemplir, values=BdManager.select_all_classe())
classeRepetitionChamps.grid(row=2, column=2)

coursRepetitionLabel = Label(frameChampsRemplir, text="Cours dispensé: ")
coursRepetitionLabel.grid(row=3, column=1)
coursRepetitionChamps = ttk.Combobox(frameChampsRemplir, values=BdManager.select_all_course())
coursRepetitionChamps.grid(row=3, column=2)

salleRepetitionLabel = Label(frameChampsRemplir, text="Salle: ")
salleRepetitionLabel.grid(row=4, column=1)
salleRepetitionChamps = ttk.Combobox(frameChampsRemplir, values=BdManager.select_all_salle())
salleRepetitionChamps.grid(row=4, column=2)

dureeRepetitionLabel = Label(frameChampsRemplir, text="Durée: ")
dureeRepetitionLabel.grid(row=5, column=1)
dureeRepetitionChamps = Spinbox(frameChampsRemplir, from_=0.5, to=3, increment=0.5, wrap=True)
dureeRepetitionChamps.invoke(element="buttondown")
dureeRepetitionChamps.grid(row=5, column=2)

boutonValidation = Button(frameChampsRemplir, text="Valider", command=BdManager.select_all_professeur)
boutonValidation.grid(row=6, column=1, columnspan=2)

frameChampsRemplir.grid(row=1, column=1)
panedAcceuil.add(frameAcceuil)
frameTreeviewStat = LabelFrame(panedAcceuil, text="Fiche de suivie des cours", labelanchor="n")

treeviewPresence = ttk.Treeview(frameTreeviewStat, columns=('1', "2", "3", "4", "5", "6"), show="headings", height=50)

treeviewPresence.heading(column="1", text="Nom du professeur")
treeviewPresence.heading(column="2", text="Classe repetée")
treeviewPresence.heading(column="3", text="Cours dispensé")
treeviewPresence.heading(column="4", text="Durée du cours")
treeviewPresence.heading(column="5", text="Salle")
treeviewPresence.heading(column="6", text="Date")

treeviewPresence.column(column="1", )
treeviewPresence.column(column="2", )
treeviewPresence.column(column="3", )
treeviewPresence.column(column="4", )
treeviewPresence.column(column="5", )
treeviewPresence.column(column="6", )

treeviewPresence.pack(expand=YES)

panedAcceuil.add(frameTreeviewStat)
noteBookMere.add(panedAcceuil, text="Acceuil")
noteBookMere.pack(expand=YES)

root.mainloop()

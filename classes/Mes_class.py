import os
import shutil
from abc import ABC, abstractmethod
from tkinter.messagebox import showinfo

class FileOrganizer(ABC):
    @abstractmethod
    def organiser(self, dossierFile):
        pass

class ExtensionFileOrganizer(FileOrganizer):
    def organiser(self, dossierFile):
        contenu_dossier = os.listdir(dossierFile)
        for element in contenu_dossier:
            chemin_dossierFile = os.path.join(dossierFile, element)
            list_ext = chemin_dossierFile.split(".")
            list_ext_1 = list_ext[-1]
            os.makedirs(list_ext_1, exist_ok=True)

        for nom_fichier in os.listdir(dossierFile):
            chemin_dossierFile = os.path.join(dossierFile, nom_fichier)
            # print(chemin_dossierFile)
            if os.path.isfile(chemin_dossierFile):
                list_ext = chemin_dossierFile.split(".")
                list_ext_1 = list_ext[-1]
                print(list_ext_1)
                if list_ext_1 in os.listdir(dossierFile):
                    chemin_dossier_destination = os.path.join(dossierFile, list_ext_1)
                    shutil.move(chemin_dossierFile, chemin_dossier_destination)
                    print("Déplacement avec succès")
                else:
                    print("Pas de dossiers correspondants à ce fichier")
            else:
                print("Ce n'est pas un fichier")
            # if(shutil.move(chemin_dossierFile, chemin_dossier_destination)):
            #     showinfo("Information", "Déplacement avec succès")

# """    def organiser(self, dossierFile, extension):
#         for nom_fichier in os.listdir(dossierFile):
#             chemin_dossierFile = os.path.join(dossierFile, nom_fichier)
#             if os.path.isfile(chemin_dossierFile):
#                 list_ext = nom_fichier.split(".")
#                 list_ext_1 = list_ext[-1]
#                 if list_ext_1 == extension:
#                     chemin_dossier_destination = os.path.join(dossierFile, extension)
#                     shutil.move(chemin_dossierFile, chemin_dossier_destination)
#                     print("Déplacement avec succès pour l'extension", extension)
#                 else:
#                     print("Pas de fichiers avec l'extenskion spécifiée dans le dossier")"""

# organize = ExtensionFileOrganizer()
# organize.organiser("D:\OneDriver\OneDrive\Bureau\TP EXAMENS POO GP")


import os,shutil

liste_fichier = []
f = "D:/folders"
chemin = "D:/OneDriver/OneDrive/Bureau/TP EXAMENS POO GP"
contenu_dossier = os.listdir(chemin)
for element in contenu_dossier:
    liste_fichier.append(element)
    # chemin_dossier_destination = i
    if os.path.isfile(element):
        for i in range(0,len(liste_fichier)):
            ext = liste_fichier[i]
            ext_convert = "".join(ext)
            liste_ext = []
            liste = ext_convert.split(".")
            liste_1 = liste[-1]
            liste_ext.append(liste_1)
            for i in range(0,len(liste_ext)):
                fichier = liste_ext[i]
                os.makedirs(fichier,exist_ok=True)
        chemin_dossier_destination = os.path.join(f, element)
        shutil.move(chemin, chemin_dossier_destination)
        print("deplacement avec success")
    else:
        print("les fichiers n'ont pas ete deplace")




# # Parcourez les fichiers dans le dossier source
# for nom_fichier in os.listdir(dossier_source):
#     chemin_fichier_source = os.path.join(dossier_source, nom_fichier)
#     if os.path.isfile(chemin_fichier_source):
#         # Obtenez la première lettre du nom de fichier
#         premiere_lettre = nom_fichier[0].upper()
#         # Vérifiez si le dossier de destination existe
#         if premiere_lettre in lettres:
#             chemin_dossier_destination = os.path.join(dossier_cible, premiere_lettre)
#             # Déplacez le fichier vers le dossier de destination
#             shutil.move(chemin_fichier_source, chemin_dossier_destination)
#             print(f"Le fichier '{nom_fichier}' a été déplacé vers '{chemin_dossier_destination}'.")

# print("Organisation terminée !")
        





# dossier_cible = "D:\z"
# lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for lettre in lettres:
#     chemin_dossier = os.path.join(dossier_cible, lettre)
#     os.makedirs(chemin_dossier, exist_ok=True)
#     print(lettre,lettres)
#     #Choisissez le dossier source contenant vos fichiers
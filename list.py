import os,shutil

liste_nom = ["volonte.pdf","james.doc","exauce.xlxs"]
for i in range(0,len(liste_nom)):
    ext = liste_nom[i]
    ext_convert = "".join(ext)
    liste_ext = []
    liste = ext_convert.split(".")
    liste_1 = liste[-1]
    liste_ext.append(liste_1)
    for i in range(0,len(liste_ext)):
        print(liste_ext[i])




dossier_cible = "D:\z"
lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for lettre in lettres:
    chemin_dossier = os.path.join(dossier_cible, lettre)
    os.makedirs(chemin_dossier, exist_ok=True)
    print(lettre,lettres)# Choisissez le dossier source contenant vos fichiers
import os,shutil
class OrganizeFile():
    def organiser(self,dossierFile):
        contenu_dossier = os.listdir(dossierFile)
        for element in contenu_dossier:
            chemin_dossierFile = os.path.join(dossierFile,element)
            list_ext = chemin_dossierFile.split(".")
            list_ext_1 = list_ext[-1]
            os.makedirs(list_ext_1,exist_ok=True)

        for nom_fichier in os.listdir(dossierFile):
            chemin_dossierFile = os.path.join(dossierFile,nom_fichier)
            print(chemin_dossierFile)
            if os.path.isfile(chemin_dossierFile):
                    list_ext = chemin_dossierFile.split(".")
                    list_ext_1 = list_ext[-1]
                    if list_ext_1 in os.listdir(dossierFile):
                        chemin_dossier_destination = os.path.join(dossierFile, list_ext_1) 
                        shutil.move(chemin_dossierFile, chemin_dossier_destination)
                        print("deplacement avec succes")
                    else:
                        print("pas de dossiers correspondats à ce fichier")
            else:
                 print("c'est n'est pas un fichier")


        


       
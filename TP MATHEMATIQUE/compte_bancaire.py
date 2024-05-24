class account:
    solde = 20
    def __init__(self,balance):
        self.balance = balance

    def getBalance(self,solde):
        self.solde = solde
        return solde
    
    def depose(self,mnt_depose,solde):
        self.solde = solde
        self.mnt_depose = mnt_depose
        solde_actuel = solde+mnt_depose
        return solde_actuel

    def retire(self,mnt_retire,solde):
        self.mnt_retire = mnt_retire
        self.solde = solde
        resultat = solde-mnt_retire
        return resultat

    def ajout_interet(self,taux_interet,solde):
        self.taux_interet = taux_interet
        self.solde = solde
        interet = solde * (1+taux_interet)
        return interet
    
client = account(balance=0)
solde = client.solde
get_ballance=client.getBalance(solde)

operation = input("quelle opearation vous lez vous accepte 'deposer' ou 'retire'  ")
if(operation=="deposer"):
    depose = int(input("entre votre montant a deposer  "))
    solde_compte = client.depose(depose,get_ballance)
    taux_interet = float(input("entre votret taux d'interet  "))
    interet = client.ajout_interet(taux_interet,solde_compte)
    print(f"votre solde actuel est: {solde_compte} et votre taux d'interet est {interet} ")

elif(operation=="retire"):
    retire = int(input("entre votre montant a retire  "))
    solde_apre_retrai = client.retire(retire,solde)
    taux_interet = float(input("entre votret taux d'interet  "))
    interet = client.ajout_interet(taux_interet,solde_apre_retrai)
    print(f"vous avez retire {retire} votre solde actuel est: {solde_apre_retrai} et votre interet est: {interet} ")

else:
    print("ce choix la n'est pas reconnues ")


    






    
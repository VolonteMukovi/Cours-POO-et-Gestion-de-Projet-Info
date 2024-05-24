class somme:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def som(self,n1,n2):
        resultat = n1 + n2
        return resultat
    

n_Ut1 = float(input("entre le nombre 1  "))
n_Ut2 = float(input("entre le nombre 2  "))

som1 = somme(n_Ut1,n_Ut2)

print(f"La Somme de {n_Ut1} et {n_Ut2} = {som1.som(n_Ut1,n_Ut2)}")


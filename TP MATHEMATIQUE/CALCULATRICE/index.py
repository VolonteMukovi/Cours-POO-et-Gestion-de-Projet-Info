nbr1=int(input("Entrez le nombre 1: "))
nbr2=int(input("Entrez le nombre 2: "))
symbole=input("Entrez le type d'operation que vous voulez effectuer: ")

match symbole:
    case"+":
        reponse = nbr1 + nbr2
    case"-":
        reponse = nbr1 - nbr2
    case"*":
        reponse = nbr1 * nbr2
    case"/":
        if (nbr2 != 0):
            reponse = nbr1 / nbr2
        else:
            reponse = "Division par zéro impossible"
print(reponse)
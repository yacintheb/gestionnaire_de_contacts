## On importe les fonctions
from afficher_contacts import afficher_contact
from ajout_contact import ajouter_contact
from supprimer_contact import supprimer_contact
from rechercher_contact import rechercher_contact

## afficher le menu à l'utilisateur
print ("======== gestionnaire de contacts========")
print ("Appuyez sur:\n1 pour afficher les contacts\n2 pour ajouter un contact\n3 pour supprimer un contact\n4 pour rechercher un contact\n5 pour quitter le programme")

choix = input("Votre choix")
while True: # 2. Boucle infinie pour afficher le menu tant qu'on ne quitte pas
    
    choix = int(input(" votre choix ?: ")) # 3. On demande le choix à l'utilisateur

    if choix == 1:
        afficher_contact() # On appelle la fonction
    elif choix == 2:
        ajouter_contact()
    elif choix == 3:
        supprimer_contact()
    elif choix == 4:
        rechercher_contact()
    elif choix == 5:
        print("Vous avez quitté le programme")
        break # Arrête la boucle while
    else:
        print("Votre choix n'est pas valable, réessayez.")
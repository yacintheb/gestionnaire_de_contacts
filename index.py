## On importe les fonctions
from afficher_contacts import afficher_contact
from ajout_contact import ajouter_contact
from supprimer_contact import supprimer_contact
from rechercher_contact import rechercher_un_contact

contacts = [] ## On crée la liste

## afficher le menu à l'utilisateur
print ("======== gestionnaire de contacts========")
print ("Appuyez sur:\n1 pour afficher les contacts\n2 pour ajouter un contact\n3 pour supprimer un contact\n4 pour rechercher un contact\n5 pour quitter le programme")

while True: # 2. Boucle infinie pour afficher le menu tant qu'on ne quitte pas

    try:
        choix = int(input("Votre choix : "))
    except ValueError:
        print("Veuillez saisir un nombre entre 1 et 5.")
        continue

    if choix == 1:
        afficher_contact(contacts) # On appelle la fonction
    elif choix == 2:
        ajouter_contact(contacts)
    elif choix == 3:
        supprimer_contact(contacts)
    elif choix == 4:
        rechercher_un_contact(contacts)
    elif choix == 5:
        print("Vous avez quitté le programme")
        break # Arrête la boucle while
    else:
        print("Votre choix n'est pas valable, réessayez.")

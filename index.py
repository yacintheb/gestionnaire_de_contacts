# Import the functions
from afficher_contacts import afficher_contact
from ajout_contact import ajouter_contact
from supprimer_contact import supprimer_contact
from rechercher_contact import rechercher_un_contact

contacts = []  # Create the list

# Display the menu to the user
print ("======== gestionnaire de contacts========")
print ("Appuyez sur:\n1 pour afficher les contacts\n2 pour ajouter un contact\n3 pour supprimer un contact\n4 pour rechercher un contact\n5 pour quitter le programme")

while True:  # Keep displaying the menu until the user quits

    try:
        choix = int(input("Votre choix : "))
    except ValueError:
        print("Veuillez saisir un nombre entre 1 et 5.")
        continue

    if choix == 1:
        afficher_contact(contacts)  # Call the function
    elif choix == 2:
        ajouter_contact(contacts)
    elif choix == 3:
        supprimer_contact(contacts)
    elif choix == 4:
        rechercher_un_contact(contacts)
    elif choix == 5:
        print("Vous avez quitté le programme")
        break  # Stop the while loop
    else:
        print("Votre choix n'est pas valable, réessayez.")

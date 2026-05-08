def supprimer_contact(contacts):
    contact_trouve = False
    nom1 = input("Entrez le nom du contact à supprimer:")
    with open("contacts.txt", "r") as f:
        lignes = f.readlines()
    with open("contacts.txt", "w") as f:
        for ligne in lignes:
        # On sépare la ligne par la virgule et on prend le premier élément [0]
            nom_dans_fichier = ligne.split(",")[0]
        # On compare exactement le nom (en enlevant les espaces inutiles)          
            if nom_dans_fichier == nom1:
                contact_trouve = True  # On a trouvé le contact, on ne l'écrit pas
            else:
                f.write(ligne)         # On garde les autres contacts

# 3. Message de confirmation
        if contact_trouve:
            print(f"Succès : Le contact '{nom1}' a été supprimé.")
        else:
            print(f"Erreur : Aucun contact au nom de '{nom1}' n'a été trouvé.")
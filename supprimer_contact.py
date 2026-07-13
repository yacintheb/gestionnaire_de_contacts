def supprimer_contact(contacts):
    contact_trouve = False
    nom1 = input("Entrez le nom du contact à supprimer : ").strip()

    if not nom1:
        print("Vous devez saisir un nom.")
        return

    try:
        with open("contacts.txt", "r", encoding="utf-8") as f:
            lignes = f.readlines()
    except FileNotFoundError:
        print("Vous n'avez pas de contacts enregistrés.")
        return

    with open("contacts.txt", "w", encoding="utf-8") as f:
        for ligne in lignes:
        # Split the line at the comma and take the first item [0].
            nom_dans_fichier = ligne.split(",")[0].strip()

            if nom_dans_fichier.lower() == nom1.lower():
                contact_trouve = True  # The contact was found, so do not write it
            else:
                f.write(ligne)         # Keep the other contacts

    if contact_trouve:
        # Also remove the contact from the list used by the program.
        for contact in contacts.copy():
            if contact["nom"].strip().lower() == nom1.lower():
                contacts.remove(contact)

        print(f"Succès : Le contact '{nom1}' a été supprimé.")
    else:
        print(f"Erreur : Aucun contact au nom de '{nom1}' n'a été trouvé.")

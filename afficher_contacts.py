def afficher_contact (contacts):
    try:
        with open("contacts.txt", "r") as f:
            contenu = f.read()
            print (contenu)
    except FileNotFoundError:
        print("vous n'avez pas de contacts enregistrés")
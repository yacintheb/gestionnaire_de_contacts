def afficher_contact (contacts):
    try:
        with open("contacts.txt", "r", encoding="utf-8") as f:
            contenu = f.read()

            if contenu.strip():
                print(contenu)
            else:
                print("Vous n'avez pas de contacts enregistrés.")
    except FileNotFoundError:
        print("Vous n'avez pas de contacts enregistrés.")

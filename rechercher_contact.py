# Create the function
def rechercher_un_contact (contacts):
    contact_trouve = False
    nom2 = input("Entrez le nom du contact que vous cherchez : ").strip()

    if not nom2:
        print("Vous devez saisir un nom.")
        return

    try:
        with open("contacts.txt", "r", encoding="utf-8") as f:
            lignes = f.readlines()
    except FileNotFoundError:
        print("Vous n'avez pas de contacts enregistrés.")
        return

    for ligne in lignes:
        informations = ligne.strip().split(",")

        # A valid line must contain a name, a phone number, and an email address.
        if len(informations) != 3:
            continue

        nom, telephone, email = informations

        if nom.strip().lower() == nom2.lower():
            contact_trouve = True
            print(f"Nom : {nom}, téléphone : {telephone}, email : {email}")

    if not contact_trouve:
        print(f"Erreur : Aucun contact au nom de '{nom2}' n'a été trouvé.")

# Ask the user for the name, phone number, and email address

def ajouter_contact (contacts):
    nom = input("Entrez le nom : ").strip()
    telephone = input("Entrez le numéro : ").strip()
    email = input("Entrez l'adresse mail : ").strip()

    if not nom or not telephone or not email:
        print("Tous les champs sont obligatoires.")
        return

    if "," in nom or "," in telephone or "," in email:
        print("Les virgules ne sont pas autorisées.")
        return

    # Store the information in a dictionary
    contact = {
        "nom": nom,
        "telephone": telephone,
        "email": email
     }
    # Add the new contact to the list
    contacts.append(contact)
    # Save the contact to a file
    with open("contacts.txt", "a", encoding="utf-8") as f:
        ligne = ",".join(contact.values())
        f.write(ligne + "\n")

    print("Contact sauvegardé.")

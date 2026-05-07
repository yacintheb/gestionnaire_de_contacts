## Demander à l'utilisateur le nom, le numéro et l'adresse mail

def ajouter_contact (contacts):
    nom = input ("Entrez le nom")
    telephone = int (input("Entrez le numéro"))
    email = input ("Entrez l'adresse mail")
## On sauvegarde dans un dictionnaire
    contact = {
        "nom": nom,
        "telephone": telephone,
        "email": email
     }
## On enregistre / ajoute le nouveau contact dans une liste
    contacts.append(contact)
## Sauvergarder le tout dans un fichier
    with open ("contacts.txt","a") as f:
            ligne = ",".join(map(str, contact.values())) ## récupère les valeurs, les convertis en caracètres en les joingnant par une virgule
            f.write(ligne + "\n")
    print ("contact sauvegardé")

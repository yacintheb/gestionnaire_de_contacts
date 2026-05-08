## on crée la fonction
def rechercher_un_contact (contacts):
    contact_trouve = False
    nom2 = input("Entrez le nom du contact que vous cherchez:")
    with open("contacts.txt", "r") as f:
        lignes = f.readlines()
    with open("contacts.txt", "w") as f:
        for ligne in lignes:
        # On sépare la ligne par la virgule et on prend le premier élément [0]
            nom_dans_fichier = ligne.split(",")[0]
        # On compare exactement le nom (en enlevant les espaces inutiles)          
            if nom_dans_fichier == nom2:
                contact_trouve = True
                nom = ligne.split(",")[0]
                telephone = ligne.split(",")[1]
                email = ligne.split(",")[2]
                print(f" Les détails du contact. nom:{nom}, téléphone:{telephone}, email:{email}" )  
    if not  contact_trouve: ## si on ne trouve pasle contact, 
                            ## on sort de la bouvle pour afficher une seule fois l'erreur
        print(f"Erreur : Aucun contact au nom de '{nom2}' n'a été trouvé.")
def split_input(user_input):
    # Diviser la chaîne en une liste en utilisant la virgule comme séparateur
    elements_list = [element.strip() for element in user_input.split(",")]
    return elements_list


# Demander à l'utilisateur d'entrer une chaîne
user_input = input("Entrez une chaîne d'éléments séparés par des virgules : ")

# Appeler la fonction avec l'entrée utilisateur et afficher le résultat
result = split_input(user_input)
print(result)

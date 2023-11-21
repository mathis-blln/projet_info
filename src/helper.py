def trier(liste: list[list]):
    liste_triee = sorted(liste, key=lambda x: x[1])
    return liste_triee


def selectionner_n_premiers(n, liste: list[list]):
    l = []
    for i in range(n):
        l.append(liste[i])
    return l


def element_distinct(liste: list):
    elements_distincts = []
    for element in liste:
        if element not in elements_distincts:
            elements_distincts.append(element)

    print(elements_distincts)


def split_input(user_input):
    if user_input = "":
        return []
    else :           
        # Diviser la chaîne en une liste en utilisant la virgule comme séparateur
        elements_list = [element.strip() for element in user_input.split(",")]
        return elements_list

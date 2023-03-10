
def mode_weekend(heure):
    """Verifier si la valeur entrée est une float"""
    if type(heure) != float:
        return "Heure incorrecte"

    """Verifier si l'heure est comprise entre 9h et 22h"""
    if 9 <= heure <= 22:
        return "Confort"
    else:
        return "Eco"


print(mode_weekend(20.7))

import mysql.connector


class MysqlConnectorToBd:
    def __init__(self):
        self.my_bd = mysql.connector.connect(host="localhost", user="root", password="68153", database="repetition",
                                             port=3306)
        self.my_cursor = self.my_bd.cursor()

    def select_all_classe(self):
        self.my_cursor.execute("SELECT nom_classe FROM classe;")
        return [ligne[0] for ligne in self.my_cursor.fetchall()]

    def select_all_salle(self):
        self.my_cursor.execute("SELECT nom_salle FROM salle;")
        return [ligne[0] for ligne in self.my_cursor.fetchall()]

    def select_all_course(self):
        self.my_cursor.execute("SELECT nom_cours FROM cours;")
        return [ligne[0] for ligne in self.my_cursor.fetchall()]

    def select_all_professeur(self):
        self.my_cursor.execute("SELECT nom_professeur FROM professeur;")
        return [ligne[0] for ligne in self.my_cursor.fetchall()]

    def save_seance_data(self, classe, cours, salle, duree):
        self.my_cursor.execute("UPDATE seance SET ()")


dico = {
    1: {"nom": "paul", "age": 30, "tension": 12},
    2: {"nom": "jean", "age": 50, "tension": 22},
    3: {"nom": "junior", "age": 19, "tension": 16},
        }

for key in list(dico.keys()):
    print(dico[key]["nom"], dico[key]["age"], dico[key]["tension"])




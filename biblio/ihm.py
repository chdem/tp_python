from Livre import Livre
from exceptions import DocumentDejaEmpprunteException


def menu(documents: list):
    while True:
        print("====== GESTION BIBLIOTHEQUE ======")
        print("1. Consulter")
        print("2. Emprunt")
        print("3. Restitution")
        print("0. Quitter")

        saisie = input("Entrez le numéro de l'opération  : ")

        match saisie:
            case "1": afficher_documents(documents)
            case "2": emprunter_livre(documents)
            case "3": pass
            case "0": exit()
            case _: print("Entrez un choix valide.")

def afficher_documents(documents: list):
    if len(documents) <= 0: print("Pas de documents")
    for i, doc in enumerate(documents):
        print(f"{i+1}. {doc.afficher_infos()}")

def emprunter_livre(documents: list):
    livres = [doc for doc in documents if isinstance(doc, Livre)]
    if len(livres) <= 0: print("Pas de livres")
    for i, l in enumerate(livres):
        print(f"{i+1}. {l.afficher_infos()}")

    saisie = int(input("Saisissez un numéro de livre : "))
    if 1 <= saisie <= len(livres):
        livre = livres[saisie - 1]
        try:
            livre.emprunter()
        except DocumentDejaEmpprunteException as e:
            print(e)






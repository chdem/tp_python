from Document import Document
from Consultable import Consultable

class Magazine(Document, Consultable):

    def __init__(self, titre, annee_publication, numero: int):
        super().__init__(titre, annee_publication)
        self.__numero = numero

    def afficher_infos(self):
        return f"Magazine : {self.titre}, numéro : {self.__numero}"

    def consulter(self):
        print(f"Magazine consulté : {self.titre}, numéro : {self.__numero} ")
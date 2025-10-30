from Document import Document
from Empruntable import Empruntable
from Consultable import Consultable
from exceptions import *
import enums.Genre as Genre


class Livre(Document, Empruntable, Consultable):

    def __init__(self, titre, annee_publication, auteur: str, nb_pages : int, genre: Genre):
        super().__init__(titre, annee_publication)
        Empruntable.__init__(self)
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__genre = genre

    @property
    def nb_pages(self):
        return self.__nb_pages

    @staticmethod
    def new(titre: str, auteur: str, genre: Genre):
        return Livre(titre, 0, auteur, 100, genre)
    
    @staticmethod
    def compteur_pages(livres : list):
        return sum(l.nb_pages for l in livres)
    
    def afficher_infos(self):
        return f"Livre : {self.titre}"

    def emprunter(self):
        if not self.est_emprunte:
            self.est_emprunte = True
            print("Livre emprunté")
        else: raise DocumentDejaEmpprunteException("Déja emprunté")

    def rendre(self):
        if self.est_emprunte: 
            print("Livre rendu")
            self.est_emprunte = False
        else: raise DocumentNonEmprunteException("Pas emprunté, par rendable")

    def consulter(self):
        print("Livre consulté")
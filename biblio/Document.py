from abc import ABC, abstractmethod


class Document(ABC):
    nb_document: int = 0

    def __init__(self, titre: str, annee_publication: int):
        self.__titre = titre
        self.__annee_publication = annee_publication
        Document.nb_document += 1

    @abstractmethod
    def afficher_infos():
        pass

    @classmethod
    def afficher_nb_document(cls):
        return cls.nb_document
    
    @property
    def titre(self):
        return self.__titre
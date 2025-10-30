from abc import ABC, abstractmethod


class Empruntable(ABC):

    def __init__(self):
        self._est_emprunte = False
        
    @abstractmethod
    def emprunter(self):
        pass

    @abstractmethod 
    def rendre(self):
        pass

    @property
    def est_emprunte(self):
        return self._est_emprunte

    @est_emprunte.setter
    def est_emprunte(self, valeur: bool):
        self._est_emprunte = valeur


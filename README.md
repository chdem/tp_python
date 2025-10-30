# Py TP

## 1. Cloner
Utiliser git clone + l'url présente dans github

## 2. Explications 

- classe principale :
  ```python
  def main():
    l1 = Livre("Lord of the rings", 1948, "Tolkien", 1500, Genre.FANTASTIQUE )
    l2 = Livre("The Witcher", 1997, "Machin truc", 700, Genre.FANTASTIQUE )
    l3 = Livre.new("Truc machin", "auteur", Genre.ROMAN)


    m1 = Magazine("vroom", 1912, 1)


    menu([l1, l2, l3, m1])


    if __name__ == "__main__":
        main()
    
  ```

- objet principal 
    ```python
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
    ```

- menu
    ```python
        print("====== GESTION BIBLIOTHEQUE ======")
        print("1. Consulter")
        print("2. Emprunt")
        print("3. Restitution")
        print("0. Quitter")
    ```
  


```python

```

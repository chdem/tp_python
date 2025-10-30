from Livre import Livre
from enums.Genre import Genre
from Magazine import Magazine
from ihm import *


def main():
    l1 = Livre("Lord of the rings", 1948, "Tolkien", 1500, Genre.FANTASTIQUE )
    l2 = Livre("The Witcher", 1997, "Machin truc", 700, Genre.FANTASTIQUE )
    l3 = Livre.new("Truc machin", "auteur", Genre.ROMAN)


    m1 = Magazine("vroom", 1912, 1)


    menu([l1, l2, l3, m1])


if __name__ == "__main__":
    main()
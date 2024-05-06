# @title Exercício (copy/paste)
class Classe1:
    s = "Bom"

class Classe2:
    s = "trabalho"

class Classe3(Classe1, Classe2):
    def __init__(self):
        self.s = Classe1.s + " " + Classe2.s  # Concatenar

_ = Classe3()
print(_.s)

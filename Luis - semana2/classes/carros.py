class Carro:
  #O método __init__ inicializa os atributos da instância da Classe Carro
  def __init__(self, marca_nome, deposito_valor, nivel):
    self.marca = marca_nome
    self.deposito = deposito_valor
    self.nivel = nivel

  def andar(self, km):
    if self.nivel == 0:
      print(f"{self.marca} não tem combustível para andar!")
      return
    
    consumo = km * 7
    if self.nivel < consumo:
      print(f"{self.marca} não tem combustível suficiente para andar {km} km! Só tem {self.nivel // 7} para andar.")
      self.nivel = 0
      return
    
    self.nivel -= consumo

  def abastecer(self, litros):
    if litros <= 0:
      print("Não pode abastecer com quantidade negativa de litros!")
      return
    
    self.nivel += litros
    if self.nivel > self.deposito:
      self.nivel = self.deposito
      print(f"{self.marca} abastecido até ao máximo ({self.deposito}L).")
    else:
      print(f"{self.marca} abastecido com {litros}L.")


##### --- Teste da classe Carro --- #####

carro1 = Carro("Ferrari", 50, 10)
carro2 = Carro("Bugatti", 60, 10)

#Carro 1
abastecerCarro1 = int(input("Insira um valor para abastecer o carro 1 (combustivel L): "))
andarCarro1 = int(input("Insira um valor em para carro 1 andar (Km): "))
carro1.abastecer(abastecerCarro1)
carro1.andar(andarCarro1)

# Carro 2
abastecerCarro2 = int(input("Insira um valor para abastecer o carro 2: "))
andarCarro2 = int(input("Insira um valor em para carro 2 andar (Km): "))
carro2.abastecer(abastecerCarro2)
carro2.andar(andarCarro2)

class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None

  def mostrar_no(self):
    print(self.valor)


class ListaEncadeada:
  def __init__(self):
    self.primeiro = None

  def inserir_inicio(self, valor):
    novo = No(valor)
    novo.proximo = self.primeiro
    self.primeiro = novo

  def verifica_vazia(self):
    if self.primeiro == None:
      return True
    else: 
      return False
  
  def mostra_lista(self):
    if self.verifica_vazia() == True:
      print("Lista Vazia")
    else:
      atual = self.primeiro
      while atual is not None:
        atual.mostrar_no()
        atual = atual.proximo

  def ordenar(self):
    if self.verifica_vazia() == True:
      print("Lista Vazia")
    else:
      anterior = self.primeiro
      while anterior is not None:
        atual = anterior.proximo
        while atual is not None:
          if anterior.valor > atual.valor:
            temp = anterior.valor
            anterior.valor = atual.valor
            atual.valor = temp
          atual = atual.proximo
        anterior = anterior.proximo

  def quantidade_numero(self, valor):
    if self.verifica_vazia() == True:
      print("Lista Vazia")
    else:
      atual = self.primeiro
      quant=0
      while atual is not None:
        if atual.valor == valor:
          quant+=1
        atual = atual.proximo 
      if quant == 0:
        print("Número {} não foi encontrado na Lista".format(valor))
      else:
        print("O número {} foi encontrado: {} vez(s)".format(valor, quant))

  def inserir_fim(self, valor):
    if self.verifica_vazia() == True:
      print("Por Favor encira no começo pois a lista está vazia")
    else:
      atual = self.primeiro
      novo = No(valor)
      novo.proximo = None
      while atual.proximo is not None:
        atual = atual.proximo
      atual.proximo = novo

  def excluir_um_valor(self, valor):
    if self.verifica_vazia() == True:
      print("Lista Vazia")
    elif self.primeiro.valor == valor:
      self.primeiro = self.primeiro.proximo
    else:
      anterior = self.primeiro
      atual = anterior.proximo
      while atual is not None:
        if atual.valor == valor:
          remover = atual
          anterior.proximo = atual.proximo
          anterior = anterior.proximo
          del remover
        atual = atual.proximo




lista = ListaEncadeada()
lista.inserir_inicio(8)
lista.inserir_fim(3)
lista.inserir_fim(3)
lista.inserir_fim(3)
lista.inserir_fim(3)
lista.mostra_lista()
lista.quantidade_numero(1)
lista.excluir_um_valor(3)
lista.excluir_um_valor(3)
lista.mostra_lista()

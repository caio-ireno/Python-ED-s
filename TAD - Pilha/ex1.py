class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        return self.items.pop()

    def vazia(self):
        return len(self.items) == 0
    
    def getItems(self):
        return self.items

def separar_pares_impares(valores):
    pilha_pares = Pilha()
    pilha_impares = Pilha()

    for valor in valores:
        if valor % 2 == 0:
            pilha_pares.empilhar(valor)
        else:
            pilha_impares.empilhar(valor)

    return pilha_pares, pilha_impares

def main():
    valores = []
    for i in range(10):
        valor = int(input(f"Digite o {i+1}º valor inteiro: "))
        valores.append(valor)

    pilha_pares, pilha_impares = separar_pares_impares(valores)

    print("Valores pares:")
    while not pilha_pares.vazia():
        print(pilha_pares.desempilhar())

    print("\nValores ímpares:")
    while not pilha_impares.vazia():
        print(pilha_impares.desempilhar())

main()

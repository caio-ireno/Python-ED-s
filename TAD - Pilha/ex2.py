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

def inverter_string(string):
    pilha = Pilha()
    for letra in string:
        pilha.empilhar(letra)
        print(pilha.getItems())

    string_invertida = ""
    while not pilha.vazia():
        string_invertida += pilha.desempilhar()
        print(string_invertida)

    return string_invertida

# Exemplo de uso
texto = "TEXTO PARA REVERTER"
texto_invertido = inverter_string(texto)
print(texto_invertido)

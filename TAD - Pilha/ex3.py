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
    
def inverter_palavras(string):
    palavras = string.split()  # Separa a string em palavras
    print (palavras)
    string_invertida = ""

    pilha = Pilha()
    for palavra in palavras:
        for letra in palavra:
            #print(pilha.getItems())
            pilha.empilhar(letra)
        
        palavra_invertida = ""
        while not pilha.vazia():
            print("Antes do pop",pilha.getItems())
            palavra_invertida += pilha.desempilhar()
            print("depois do pop",pilha.getItems())

        string_invertida += palavra_invertida + " "

    return string_invertida.strip()  # Remove o espaço em branco extra no final

# Exemplo de uso
texto = "caio eduardo PARA REVERTER"
texto_invertido = inverter_palavras(texto)
print("String original:", texto)
print("String invertida:", texto_invertido)

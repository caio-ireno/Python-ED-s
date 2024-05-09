class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        return self.items.pop()

    def vazia(self):
        return len(self.items) == 0

def verifica_palindromo(palavra):
    palavra = palavra.lower()  # Convertendo a palavra para minúsculas para ser case insensitive
    pilha = Pilha()

    # Empilha todas as letras da palavra
    for letra in palavra:
        pilha.empilhar(letra)

    # Compara a palavra original com a palavra formada pela desempilhação da pilha
    for letra in palavra:
        if letra != pilha.desempilhar():
            return False
    
    return True

# Exemplo de uso
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")
if verifica_palindromo(palavra):
    print(f'A palavra "{palavra}" é um palíndromo.')
else:
    print(f'A palavra "{palavra}" não é um palíndromo.')

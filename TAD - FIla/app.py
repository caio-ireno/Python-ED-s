from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque()

    def insere(self, elemento):
        self.fila.append(elemento)

    def remove(self):
        """Remove e retorna o elemento na frente da fila."""
        if not self.vazia():
            return self.fila.popleft()
        else:
            raise IndexError("A fila está vazia")

    def frente(self):
        """Retorna o elemento na frente da fila sem removê-lo."""
        if not self.vazia():
            return self.fila[0]
        else:
            raise IndexError("A fila está vazia")

    def __len__(self):
        """Retorna o tamanho da fila."""
        return len(self.fila)

    def vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.fila) == 0


fila = Fila()
fila.insere(10)
print(fila.frente())
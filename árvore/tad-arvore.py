class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)

class Arvore:
    def __init__(self):
        self.raiz = None

    def insere(self, chave):
        if self.raiz is None:
            self.raiz = NodoArvore(chave)
        else:
            self._insere(self.raiz, chave)

    def _insere(self, raiz, chave):
        if chave < raiz.chave:
            if raiz.esquerda is None:
                raiz.esquerda = NodoArvore(chave)
            else:
                self._insere(raiz.esquerda, chave)
        else:
            if raiz.direita is None:
                raiz.direita = NodoArvore(chave)
            else:
                self._insere(raiz.direita, chave)

    def busca(self, chave):
        return self._busca(self.raiz, chave)

    def _busca(self, raiz, chave):
        if raiz is None or raiz.chave == chave:
            return raiz
        if raiz.chave < chave:
            return self._busca(raiz.direita, chave)
        return self._busca(raiz.esquerda, chave)

    def em_ordem(self):
        self._em_ordem(self.raiz)

    def _em_ordem(self, raiz):
        if raiz is None:
            return
        self._em_ordem(raiz.esquerda)
        print(raiz.chave),
        self._em_ordem(raiz.direita)

    def pre_ordem(self):
        self._pre_ordem(self.raiz)

    def _pre_ordem(self, raiz):
        if raiz is None:
            return
        print(raiz.chave),
        self._pre_ordem(raiz.esquerda)
        self._pre_ordem(raiz.direita)

    def pos_ordem(self):
        self._pos_ordem(self.raiz)

    def _pos_ordem(self, raiz):
        if raiz is None:
            return
        self._pos_ordem(raiz.esquerda)
        self._pos_ordem(raiz.direita)
        print(raiz.chave)


# Testando a classe Arvore
arvore = Arvore()

for chave in [40, 20, 60, 50, 70, 10, 30]:
    arvore.insere(chave)

for chave in [-50, 10, 30, 70, 100]:
    resultado = arvore.busca(chave)
    if resultado:
        print("Busca pela chave {}: Sucesso!".format(chave))
    else:
        print("Busca pela chave {}: Falha!".format(chave))

# Testando os métodos de caminhamento
print("Caminhamento em ordem:")
arvore.em_ordem()
print("\nCaminhamento em pré-ordem:")
arvore.pre_ordem()
print("\nCaminhamento em pós-ordem:")
arvore.pos_ordem()

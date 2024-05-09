class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)

def insere(raiz, nodo):
    if raiz is None:
        raiz = nodo
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)

def busca(raiz, chave):
    if raiz is None:
        return None
    if raiz.chave == chave:
        return raiz
    if raiz.chave < chave:
        return busca(raiz.direita, chave)
    return busca(raiz.esquerda, chave)

def em_ordem(raiz):
    if not raiz:
        return
    em_ordem(raiz.esquerda)
    print(raiz.chave),
    em_ordem(raiz.direita)


def pre_ordem(raiz):
    if not raiz:
        return
    print(raiz.chave),
    pre_ordem(raiz.esquerda)
    pre_ordem(raiz.direita)

def pos_ordem(raiz):
    if not raiz:
        return
    pos_ordem(raiz.esquerda)
    pos_ordem(raiz.direita)
    print(raiz.chave),

raiz = NodoArvore(40)

for chave in [20, 60, 50, 70, 10, 30,-50]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)

for chave in [-50, 10, 30, 70, 100]:
    resultado = busca(raiz, chave)
    if resultado:
        print("Busca pela chave {}: Sucesso!".format(chave))
    else:
        print("Busca pela chave {}: Falha!".format(chave))

# Testando as funções
print("Caminhamento em ordem:")
em_ordem(raiz)
print("\nCaminhamento em pré-ordem:")
pre_ordem(raiz)
print("\nCaminhamento em pós-ordem:")
pos_ordem(raiz)

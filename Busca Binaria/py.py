def pesquisa_binaria(lista_de_numeros, valor_pesquisado):
    tamanho = len(lista_de_numeros) # Defino o tamanho
    #Como primeiro passo é sempre 0
    inicio = 0 

    #No primeiro passo é sempre tamanho -1 
    fim = tamanho - 1


    while inicio <= fim:
        meio = (inicio + fim) // 2
        print(inicio, meio, fim)
        elemento_do_meio = lista_de_numeros[meio]

        if elemento_do_meio == valor_pesquisado:
            return f"{elemento_do_meio} encontrado na posição {meio}"
        elif valor_pesquisado < elemento_do_meio:
            fim = meio - 1
        else:
            inicio = meio + 1
       

    return "Não aparece na lista"

lista = [16, 18, 20, 50, 60, 81, 84, 89]
print(pesquisa_binaria(lista, 84))
print(pesquisa_binaria(lista, 10))

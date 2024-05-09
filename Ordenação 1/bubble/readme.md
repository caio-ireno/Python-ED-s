# Porque I e J (Dois FOR)

No algoritmo BubbleSort, as variáveis ​`i` e `j` são usadas como índices para percorrer a lista e comparar os elementos durante o processo de ordenação.

1. A variável `i` é utilizada para controlar as iterações externas do algoritmo, ou seja, ela percorre a lista do início ao fim, determinando quantas vezes o processo de comparação e troca será repetido. No contexto do BubbleSort, a cada iteração de `i`, o maior elemento da lista (ou o menor, dependendo da ordem de classificação desejada) é movido para a sua posição correta na lista ordenada.

2. A variável `j` é utilizada para controlar as iterações internas do algoritmo. Dentro de cada iteração de `i`, a variável `j` percorre a lista da esquerda para a direita, comparando pares de elementos adjacentes. Isso permite que o algoritmo verifique se um elemento é maior (ou menor) que o próximo elemento na lista e, se necessário, os troque de posição para ordená-los corretamente.

Portanto, as variáveis ​​`i` e `j` são essenciais para o funcionamento do algoritmo BubbleSort, pois permitem que ele itere sobre todos os elementos da lista e realize as comparações e trocas necessárias para ordená-los.

# Alteração na lsta Original

No algoritmo `BubbleSort`, o retorno da lista dentro da função e a atribuição dentro do condicional `if` afetam diretamente a lista original que é passada como argumento para a função.

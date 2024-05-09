def is_well_formed(string):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in string:
        if char in ['(', '[', '{']:
            # Se o caractere for um parêntese de abertura, colchete ou chave, empilhe-o
            stack.append(char)
        elif char in [')', ']', '}']:
            # Se o caractere for um parêntese de fechamento, colchete ou chave
            if not stack:
                # Se a pilha estiver vazia e encontrarmos um fechamento, está desbalanceado
                return False
            # Removemos o elemento do topo da pilha
            top_element = stack.pop()
            # Verificamos se o elemento removido do topo e o caractere atual correspondem
            if mapping[char] != top_element:
                # Se não correspondem, a sequência é inválida
                return False
    
    # Verificamos se todos os parênteses foram fechados corretamente
    return len(stack) == 0

# Exemplo de uso
print(is_well_formed("( ( ( [ ] ) ) {})"))  # Saída: True
print(is_well_formed("( [  ) ]"))          # Saída: False
print(is_well_formed("( ( ( ) )  "))       # Saída: False

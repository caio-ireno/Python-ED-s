

'''
O objetivo dessa atividade é fazer uma função contador, que recebe uma string
e devolve uma contagem de palavras, na forma de um dicionário

Por exemplo, ao fazer 
d = contador("o doce mais doce")
esperamos que d contenha o dicionário {"o":1, "mais":1, "doce":2}
        
Esse arquivo se auto testa. Ao rodar a função runTests, você verá o que já
conseguiu fazer e o que falta.

Se você tiver curiosidade, no teste temos as seguintes duas linhas
d = contador("o doce mais doce")        
self.assertEqual(d,{"o":1, "mais":1, "doce":2})
que dizem que a variavel d tem que ser igual a {"o":1, "mais":1, "doce":2}


'''

import unittest

def contador(texto):
    palavras = texto.split()
    dici = {}
    for palavra in palavras:
        if palavra not in dici:
            dici[palavra]=1
        else:
            dici[palavra]+=1
    return dici


class TestStringMethods(unittest.TestCase):
     def test_01_contador_retorna_dic(self):
         d=contador('o doce mais doce')
         self.assertEqual(type(d),type({'dicionario':'exemplo'}),"Passou no Teste")

     def test_02_contador(self):
        d = contador("o doce mais doce")
        self.assertEqual(d,{"o":1, "mais":1, "doce":2})
        d2=contador('esse exercício é um exercício fácil ou difícil')
        self.assertEqual(d2,{'é': 1, 'difícil': 1,
                            'esse': 1, 'ou': 1, 'um': 1, 'fácil': 1, 'exercício': 2})
        d3=contador('o doce perguntou ao doce qual é o doce mais doce '+
                    'e o doce respondeu ao doce que o doce mais doce é '+
                    'o doce de batata doce')
        self.assertEqual(d3['doce'],10)
        self.assertTrue('gato' not in d3)
        self.assertTrue('respondeu' in d3)
     
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == "__main__":
    runTests()

'''
ESSE CODIGO SERVE PARA CRIAR UMA BASE PARA MATRIZ, DE FORMA QUE SEJA POSSIVEL CRIAR QUANTAS COLUNAS FOREM NECESSARIAS AUTOMATICAMENTE
NÃO SE LIMITANDO APENAS A ESSA FUNÇÃO
VOCÊ PODE FAZER AS MUDANÇAS QUE JULGAR NECESSARIAS E DEIXAR O CÓDIGO MAIS FUNCIONAL PARA SUA NECESSIDADE

NO MEU CASO, O ARQUIVO QUE EU ABRO COMO EXEMPLO, CONTEM:
LINHA 0: NOME DA MATRIZ
LINHA 1: QUANTIDADE DE LINHAS / COLUNAS (INT)
LINHA 2 EM DIANTE: NOMES DAS LINHAS / COLUNAS
'''

from openpyxl import Workbook
import string

book = Workbook()
sheet = book.active
nome_xlsx = 'teste.xlsx'

listax=[]
abrir_aquivo = open('DADOS.txt', 'r' ,encoding='utf8')
lista_seguindo_usuario = abrir_aquivo.read()
listax = lista_seguindo_usuario.split('\n')
abrir_aquivo.close()
usuario_principal = listax[0]
del(listax[0])
numero_seguindo = int(listax[0])
del(listax[0])
#na segunda linha do txt tem o numero de colunas e linhas que eu preciso fazer :)

lista = list(string.ascii_uppercase)
lista2 = list(string.ascii_uppercase)
lista2.insert(0,'A')
aux = 0
cont = 0
flag = 0
x=1
numero_seguindo = numero_seguindo + 1
while cont != numero_seguindo:
    print(cont)
    aux2 = lista2[0]
    if aux == (len(lista)):
        aux = 0
        flag = 1
        del(lista2[0])
        aux2 = lista2[0]
    if aux < len(lista)  and flag == 0:
        sheet[str(lista[aux]) + str(x)] = listax[0]
        aux = aux + 1
    if aux < len(lista) and flag == 1:
        sheet[aux2 + str(lista[aux]) + str(x)] = listax[0]
        aux = aux + 1
    cont = cont + 1
    sheet['A'+str(cont+1)] = listax[0]
    del(listax[0])    
sheet['A1'] = 'MATRIZ'
book.save(nome_xlsx)
print('FIM')

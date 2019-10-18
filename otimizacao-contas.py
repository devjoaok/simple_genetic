import time
from datetime import datetime
import random
import math

saida = {}
custos = {}
dia = datetime.strptime('2019-10-15', '%Y-%m-%d').date()


def calcula_custo(conta):
    if (dia == conta[4]):
        return conta[3]
    elif (dia < conta[4]):
        diferenca = conta[4] - dia
        # Calculando os Juros simples por dia
        return conta[3] + (diferenca.days * (conta[3] * conta[7]))
    else:
        diferenca = dia - conta[4]
        if (diferenca.days >= conta[5]):
            # Com desconto
            return conta[3] - (conta[3] * conta[6])
        return conta[3]

for linha in open('saida.csv'):
    _codigo, _cnpj, _nome, _custo, _data, _dias, _desconto, _juros = linha.split(';')
    _codigo = int(_codigo)
    saida.setdefault(_codigo, [])
    custos.setdefault(_codigo, 0)
    saida[_codigo].append([_codigo, _cnpj, _nome, float(_custo.replace(',', '.')), datetime.strptime(_data, '%Y-%m-%d').date(), int(_dias), (int(_desconto.replace('%', '').replace(',', '.')) / 100), (float(_juros.replace('%\n', '').replace(',', '.')) / 100)])
    custos[_codigo] = calcula_custo(saida[_codigo][0])

# recebe um array com index das contas em order
def imprimir_contas(contas):
    for i in contas:
        print("{} - R${}".format(saida[i][0][1], custos[i]))
    
print(saida[1][0][0])
imprimir_contas([29,4,8,6,9,4,4,3,16,7,2])
# imprimir_contas([1])

import pyautogui as py
import pandas as pd
from time import sleep

# Passo 1 - Abrir o sistema da empresa
py.PAUSE = 5

py.click(x=778, y=747)
py.click(x=1157, y=12)
py.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
py.press('enter')

# Passo 2 - Fazer login
sleep(10)
py.click(x=443, y=392)
py.write('manuelatrindade100@gmail.com')
py.press('tab')
py.write('senha')
py.press('tab')
py.press('enter')

# Passo 3 - Importar a base de dados dos produtos
tabela=pd.read_csv('produtos.csv')
sleep(10)

# Passo 4 - Cadastrar um produto
for linha in tabela.index:
    py.click(x=423, y=275)

    codigo=tabela.loc[linha,'codigo']
    py.write(str(codigo))
    py.press('tab')

    marca=tabela.loc[linha,'marca']
    py.write(str(marca))
    py.press('tab')

    tipo=tabela.loc[linha,'tipo']
    py.write(str(tipo))
    py.press('tab')

    categoria=tabela.loc[linha,'categoria']
    py.write(str(categoria))
    py.press('tab')

    preço=tabela.loc[linha,'preco_unitario']
    py.write(str(preço))
    py.press('tab')

    custo=tabela.loc[linha,'custo']
    py.write(str(custo))
    py.press('tab')

    obs=tabela.loc[linha,'obs']
    if not pd.isna(obs):
        py.write(str(tabela.loc[linha,'obs']))
    py.press('tab')

    py.press('enter')
    py.scroll(5000)

# Passo 5 - Repetir o passo 4 até acabar todos os produtos

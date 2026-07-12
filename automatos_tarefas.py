# bibliotexas = pacotes de código
# pip install pyautogui
# Passo a passo de programa
# passo 1: Entrar no sistema de empresa
# passo 2: Fazer login
# passo 3: Abrir a base de dados
# passo 4: Cadastrar produto
# passo 5: Repetir o passo 4 até acabar a lista de produtos

import pyautogui
import time

# pyautogui.click -> clica
# pyautogui.write -> Escreve texto
# pyautogui.press -> Aperta uma tecla
# pyautogui.hotkey -> escreve um atalho
pyautogui.PAUSE = 1.0
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo para o programa
# Passo 1 - Entrar no sistema de empresa
# Abriria o navegador

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1.0)
pyautogui.write(link)
pyautogui.press("enter")
# Fazer pausa maior para carregar o site
time.sleep(3)
# Passo 2 - fazer login
# Clicar no campo de email
pyautogui.click(x=687, y=408)
time.sleep(0.5)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
time.sleep(1.0)
pyautogui.write("senha")
time.sleep(0.5)
pyautogui.press("tab")
# time.sleep(0.5)
pyautogui.press("enter")
# Fazer uma pausa para carregar o site
time.sleep(4)
# Passo 3: Abrir a base de dados
# pip install panda openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    # Código
    pyautogui.click(x=671, y=289) # clicar no campo da pag. de produto
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    time.sleep(0.5)
    pyautogui.press("tab")
    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    time.sleep(0.5)
    pyautogui.press("tab")
    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    time.sleep(0.5)
    pyautogui.press("tab")
    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    time.sleep(0.5)
    pyautogui.press("tab")
    # Preço
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    time.sleep(0.5)
    pyautogui.press("tab")
    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    time.sleep(0.5)
    pyautogui.press("tab")
    # Observação
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    time.sleep(0.5)
    pyautogui.press("tab")
    # Enviar (enter)
    pyautogui.press("enter")
    # Voltar ao inicio da tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos

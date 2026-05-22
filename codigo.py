# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos

import pyautogui
import time
import pandas

# Configuração do PyAutoGUI
pyautogui.PAUSE = 1

# Link do sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"


# PASSO 1 - Abrir navegador


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Espera abrir
time.sleep(3)

# Seleciona barra de endereço
pyautogui.hotkey("ctrl", "l")

# Digita o link
pyautogui.write(link)
pyautogui.press("enter")

# Espera site carregar
time.sleep(5)


# PASSO 2 - Fazer login


# Campo email
pyautogui.click(x=960, y=478)
time.sleep(1)

# Email
pyautogui.write("brunoossouza@hotmail.com")

# Próximo campo
pyautogui.press("tab")

# Senha
pyautogui.write("isabelly")

# Botão login
pyautogui.press("tab")
pyautogui.press("enter")

# Espera carregar sistema
time.sleep(5)


# PASSO 3 - Ler base de dados


tabela = pandas.read_csv("produtos.csv")

print(tabela)


# PASSO 4 - Cadastrar produtos


for linha in tabela.index:

    # Clica no campo código
    pyautogui.click(x=709, y=322)
    time.sleep(1)

    # Código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # Observações
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    # Enviar produto
    pyautogui.press("enter")

    # Espera cadastro concluir
    time.sleep(2)

    # Volta para cima da página
    pyautogui.scroll(5000)

    # Pequena pausa
    time.sleep(1)
    


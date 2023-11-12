from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import ImageGrab
from datetime import datetime
import os
import time
from anticaptchaofficial.imagecaptcha import *
import json
import sys

def gera_json(status, cod_rast, titulo, msg):
    # Dados para o JSON
    dados_json = {
        "status": status,
        "code": cod_rast,
        "data": {
            "title": titulo,
            "message": msg
        }
    }

    # Formatando os dados como uma string JSON
    json_formatado = json.dumps(dados_json, ensure_ascii=False, indent=2)

    # Imprimir os dados formatados
    print(json_formatado)

def quebra_captcha(imagem):
    solver = imagecaptcha()

    solver.set_verbose(1)
    solver.set_key("efdfd4a302095c0fdac85ca9812194e3")

    # Faz a quebra da captcha e retorna o valor do texto para colocar na página
    captcha_text = solver.solve_and_return_solution(imagem)

    return captcha_text

def consulta_informaçoes(cod_rastreio):

    driver = webdriver.Chrome()

    driver.get('https://rastreamento.correios.com.br/app/index.php#')

    driver.maximize_window()

    # Inseri o código de rastreio para buscar os dados
    search_box = driver.find_element(By.XPATH, '//*[@id="objeto"]' )  #driver.find_element_by_name("key")
    search_box.send_keys(cod_rastreio)

    # Envie a pesquisa
    # search_box.send_keys(Keys.RETURN)

    time.sleep(1)

    xpath_imagem = '//*[@id="captcha_image"]'
    elemento_imagem = driver.find_element(By.XPATH, xpath_imagem)

    left = elemento_imagem.location['x']
    right = elemento_imagem.location['y']
    bottom = elemento_imagem.size['width']
    top = elemento_imagem.size['height']

    # Criar o nome do diretório
    nome_diretorio = "captchas_extraidas"  # Substitua pelo nome do seu diretório

    # Criar o diretório se ele não existir
    if not os.path.exists(nome_diretorio):
        os.makedirs(nome_diretorio)

    # Faz a concatenação da data, hora, minuto e segundos para compor o nome do arquivo
    agora = datetime.now()

    data_formatada = agora.strftime("%Y_%m_%d_%H_%M_%S")

    caminho_arquivo = os.path.join(nome_diretorio, f"cod_correios_{data_formatada}.png")

    time.sleep(2)

    # Capturar a imagem do trecho da tela usando o módulo ImageGrab
    imagem_captcha = ImageGrab.grab(bbox=(left, top + 342, right + 472, bottom + 258 ))

    # Salvar a imagem para posterior análise (opcional)
    imagem_captcha.save(caminho_arquivo)

    texto_captcha = quebra_captcha(caminho_arquivo)

    search_box = driver.find_element(By.XPATH, '//*[@id="captcha"]' )  #driver.find_element_by_name("key")
    search_box.send_keys(texto_captcha)

    # Envie a pesquisa
    search_box.send_keys(Keys.RETURN)

    time.sleep(1)

    Status = 'sucess' # //*[@id="ver-mais"]/ul/li[1]/div[2]/p[1]   
    Code = cod_rastreio
    title =  driver.find_element(By.XPATH, '//*[@id="ver-mais"]/ul/li[1]/div[2]/p[1]').text # //*[@id="ver-mais"]/ul/li[1]/div[2]/p[2]
    message = driver.find_element(By.XPATH, '//*[@id="ver-mais"]/ul/li[1]/div[2]/p[2]').text + driver.find_element(By.XPATH, '//*[@id="ver-mais"]/ul/li[1]/div[2]/p[3]').text # //*[@id="ver-mais"]/ul/li[1]/div[2]/p[3]

    gera_json(Status, Code, title, message)
    
# Chamar a função para capturar o trecho da tela no segundo monitor
if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Por favor, informe o CÓDIGO DE RASTREIO VÁLIDO.")
        sys.exit(1)

    consulta_informaçoes(sys.argv[1])

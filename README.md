Automação dos Correios

Essa automação tem por objetivo retornar o status atual de uma encomenda mediante a consulta no site dos Correios por um código de rastreio válido fazendo a quebra da Captcha para prosseguir com a consulta.

A automação foi feita em Python e foram utilizadas algumas bibliotecas.

Caso não tenha essas bibliotecas, é favor instalá-las.

Foram usadas as seguintes bibliotecas:

  Selenium
  Pillow (PIL)
  JSON

Para a quebra da Captcha foi utilizado a API da AntiCaptcha.

Para instalar essa biblioteca utilize o seguinte comando: pip install anticaptchaofficial

Essa API utiliza uma chave que está inserida no próprio módulo.

A automação está dividida em 3 funções, a saber:

  gera_json
  quebra_captcha
  consulta_informaçoes

A chamada da automação será feita via prompt de comando (cmd).

Depois de entrar na pasta onde você salvou a automação, utilize a seguinte sintaxe para executar a automação: python consulta_encomenda.py LB571181225HK, onde essa última informação se trata do código da encomenta.

Depois que pressionar o ENTER, a função será ativada abrindo o site dos Correios, inserirá o código de rastreio, quebrará a captcha e inserirá o valor da Captcha em seu devido campo.

Depois disso, coletará os dados referente ao status atual e imprimirá na tela para que o usuário possa consultar o status atual.

Como solicitado, essa automação não salva os dados do arquivo JSON.

Por outro lado, a automação salva as imagens utilizadas da captcha toda vez que for executada.

A automação cria um diretório para que seja possívl salvar essas imagens (PNG)


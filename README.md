# Um comentário pode arruinar seu dia

Ah, a arte sutil de derrubar um serviço inteiro com uma única linha de comentário. Este projeto foi criado com fins educacionais com o objetivo primordial de te ensinar exatamente isso: como derrubar um serviço inteiro com uma linha de código.

Claro, para os menos aventureiros, também ensinamos como evitar esse caos completo utilizando o Github Actions - mas convenhamos, onde está a diversão nisso?

## O que é o GitHub Actions?

GitHub Actions é uma ferramenta de automação que permite que você defina ações customizadas para o seu repositório no GitHub. Ele permite que você configure workflows de CI/CD (Integração Contínua/Entrega Contínua) diretamente a partir do seu repositório. Em nosso contexto, usamos o GitHub Actions para identificar e impedir que comentários não compatíveis sejam inseridos no código.

## Configurando o GitHub Actions

Para configurar o GitHub Actions, você precisa criar uma pasta chamada `.github` na raiz do seu repositório. Dentro dela, outra pasta chamada `workflows`. É aqui que todos os seus arquivos de configuração de workflow ficarão.

Para este projeto, o arquivo que estamos usando é `django_ci.yml` (ou qualquer outro nome que você escolher com a extensão `.yml`).

### Etapas do arquivo `django_ci.yml`:

1. **Definição do Evento**: Define quando o workflow será acionado. Ex.: em cada `push` ou `pull_request`.
    
2. **Definição de Jobs**: Os jobs são as tarefas que serão executadas. No nosso caso, temos um job chamado `build` que vai rodar em um ambiente Ubuntu.
    
3. **Checkout**: Usa-se `actions/checkout@v2` para fazer checkout do código no runner do GitHub Actions.
    
4. **Instalação do Python 2.7**: Instalamos manualmente o Python 2.7, já que ele não é mais suportado por padrão.
    
5. **Verificar a versão do Python**: Simplesmente imprimimos a versão para fins de debug.
    
6. **Instalar o pip**: O pip é nosso gerenciador de pacotes do Python, que usamos para instalar dependências.
    
7. **Instalar dependências**: Usamos o `pip` para instalar todas as dependências definidas em `requirements.txt`.
    
8. **Checagem de caracteres não UTF-8**: Essa é a etapa onde identificamos se existem caracteres que não são compatíveis com UTF-8, como acentos, no código. Se encontrarmos algum, a build falhará.

Espero que este guia ajude a entender melhor o propósito e funcionamento do nosso projeto. Boa sorte explorando e experimentando!

## Rodando com Docker

Para rodar este projeto com Docker, siga os seguintes passos:

### Pré-requisitos

* [Docker](https://www.docker.com/products/docker-desktop)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Instruções

1. Clone o repositório:
    
    ```bash
    git clone https://github.com/lvgalvao/SafeGuardActions.git
    cd SafeGuardActions
    ```
    
2. Construa a imagem Docker e inicie o container:
    
    ```bash
    docker-compose build
    docker-compose up
    ```
    
3. Acesse o aplicativo no navegador:
    
    ```bash
    http://localhost:8000/hello
    ```
    

## Rodando localmente

Se preferir rodar o projeto localmente sem o Docker, consulte as instruções anteriores sobre a instalação e configuração do `pyenv` e ambiente virtual.

1. Instalando uma versão específica do Python com pyenv:
    
    ```bash
    pyenv install 2.7.18
    ```
    
2. Configurando a versão do Python para o seu sistema:
    
    ```bash
    pyenv local 2.7.18
    ```
    
3. Criando um ambiente virtual:
    
    ```bash
    pyenv virtualenv 2.7.18 my_venv_2.7.18
    ```
    
4. Ativando o ambiente virtual:
    
    ```bash
    pyenv activate my_venv_2.7.18
    ```
    
5. Instale as dependências:
    
    ```bash
    pip install -r requirements.txt
    ```

6. Inicie o servidor de desenvolvimento Django:
    
    ```bash
    python manage.py runserver
    ```
    
7. Acesse o aplicativo no navegador:
    
    ```bash
    http://localhost:8000/hello
    ```
    

## Desafio para você!

Ao rodar a versão `main` tudo irá funcionar, mas experimente rodar também a versão em `dev` e terá uma surpresa. Você consegue descobrir por quê? O que faria para evitar esse problema no futuro? Este é o cerne deste projeto educativo: aprender com os erros e entender como as melhores práticas podem prevenir catástrofes. Boa sorte!

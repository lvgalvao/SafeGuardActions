# Um comentário pode arruinar seu dia

Ah, a arte sutil de derrubar um serviço inteiro com uma única linha de comentário. Este projeto foi criado com fins educacionais com o objetivo primordial de te ensinar exatamente isso. Claro, para os menos aventureiros, também ensinamos como evitar esse caos completo utilizando o Github Actions - mas convenhamos, onde está a diversão nisso?

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

5. Instale as dependências

    ```bash
    pip install -r requirements.txt
    ```
6. Acesse o aplicativo no navegador:
    
    ```bash
    http://localhost:8000/hello
    ```
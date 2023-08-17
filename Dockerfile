FROM python:2.7-slim

# Define variáveis de ambiente
ENV PYTHONUNBUFFERED 1

# Crie e defina o diretório de trabalho
RUN mkdir /app
WORKDIR /app

# Instale as dependências do projeto
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copie o projeto para o container
COPY . /app/

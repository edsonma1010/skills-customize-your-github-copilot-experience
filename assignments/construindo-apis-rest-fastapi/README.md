# 📘 Assignment: Construindo APIs REST com o framework FastAPI

## 🎯 Objective

Aprender a construir APIs RESTful usando o framework FastAPI em Python, incluindo criação de endpoints, tratamento de requisições e retorno de respostas.

## 📝 Tasks

### 🛠️ Criar um Endpoint Básico da API

#### Description
Crie uma aplicação FastAPI simples com um único endpoint GET que retorna uma mensagem de boas-vindas.

#### Requirements
O programa concluído deve:

- Usar FastAPI para criar uma aplicação
- Ter um endpoint GET em `/` que retorna uma resposta JSON com uma mensagem de boas-vindas
- Executar o servidor e verificar se o endpoint funciona

### 🛠️ Adicionar Endpoints CRUD para Itens

#### Description
Estenda a API para incluir operações CRUD para gerenciar uma lista de itens (ex.: produtos ou tarefas).

#### Requirements
O programa concluído deve:

- Incluir endpoint POST para criar novos itens
- Incluir endpoint GET para recuperar todos os itens ou um item específico por ID
- Incluir endpoint PUT para atualizar um item por ID
- Incluir endpoint DELETE para remover um item por ID
- Usar modelos Pydantic para validação de requisição/resposta
- Armazenar itens na memória (lista ou dicionário)
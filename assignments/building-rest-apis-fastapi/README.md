# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a construir uma API REST em Python usando o framework FastAPI, definindo rotas, validando dados com modelos Pydantic e retornando respostas HTTP apropriadas.

## 📝 Tasks

### 🛠️ Criar a Rota Inicial da API

#### Descrição
Use o arquivo `starter-code.py` para criar uma API de catálogo de livros. Complete a rota inicial que confirma que a API está funcionando e execute o servidor localmente com Uvicorn.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI na variável `app`
- Implementar `GET /` retornando `{"message": "Book API is running"}`
- Permitir iniciar a aplicação com `uvicorn starter-code:app --reload`


### 🛠️ Adicionar Listagem e Busca de Livros

#### Descrição
Crie uma rota `GET /books` que retorne os livros armazenados em memória. Depois, adicione um parâmetro de consulta opcional `author` para filtrar os resultados por autor.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books` e retornar uma lista de livros
- Retornar cada livro com os campos `id`, `title` e `author`
- Filtrar por autor quando `author` for informado, sem diferenciar letras maiúsculas e minúsculas
- Retornar uma lista vazia quando nenhum livro corresponder à busca

Exemplo de requisição:

```text
GET /books?author=ursula
```


### 🛠️ Criar Livros com Validação

#### Descrição
Defina um modelo Pydantic `BookCreate` e implemente `POST /books` para adicionar um novo livro. A API deve gerar o identificador do livro e comunicar corretamente quando os dados enviados forem inválidos.

#### Requisitos
O programa concluído deve:

- Definir `BookCreate` com os campos obrigatórios `title` e `author`
- Rejeitar requisições sem esses campos usando a validação automática do FastAPI
- Criar um novo `id` sem sobrescrever livros existentes
- Retornar o livro criado com status HTTP `201`
- Manter o livro criado disponível em chamadas posteriores a `GET /books`

Exemplo de corpo da requisição:

```json
{
  "title": "A Wizard of Earthsea",
  "author": "Ursula K. Le Guin"
}
```
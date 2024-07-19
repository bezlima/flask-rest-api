# FLASK API REST


Este projeto é uma API REST desenvolvida com Flask e Python, projetada para gerenciar usuários com funcionalidades básicas de autenticação e manipulação. A API oferece as seguintes características:

- Cadastro de Usuário: Permite criar novos usuários fornecendo informações como nome de usuário, email e senha.

- Login com JWT: Utiliza JSON Web Tokens (JWT) para autenticação. Usuários podem se autenticar e receber um token JWT para acessar rotas protegidas.

Manipulação de Usuários:

- Ver Todos: Recupera uma lista de todos os usuários registrados.

- Ver Um: Recupera os detalhes de um usuário específico com base em seu ID.

- Deletar Um: Permite excluir um usuário específico pelo seu ID.

A API é projetada para ser simples, com foco na gestão de usuários e autenticação.


## Autor
#### Lucas Lima  - *Desenvolvedor web*

[![github](https://img.shields.io/badge/github-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bezlima)

[![linkedin](https://img.shields.io/badge/linkedin-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bezlima/)

[![portfolio](https://img.shields.io/badge/portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://bezlima-portfolio.vercel.app/)

## Rodando localmente

Em seu terminal:

Clone o projeto

```bash
  git clone https://link-para-o-projeto
```

Entre no diretório do projeto

```bash
  cd my-project
```

## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente na raiz do seu projeto.

#### `.secrets.toml`

```toml
[default]
SECRET_KEY = "string"
ALGORITHM = "string"
```
#### `settings.toml`
```toml
[default]
DATABASE_URI = "string"
MODIFICATIONS = false 
```

## Instalação

Em seu terminal:

Crie um ambiente de virtual

```bash
python -m venv .venv
```

Verifique o ambiente

```bash
which python
```

Ative o ambeiente

```bash
source .venv/bin/activate
```

Instale o gerenciador de dependencias

```bash
pip install poetry
```

Instale as dependencias

```bash
poetry install
```

Inicie o banco de dados SQLite
_*caso exista instance/app.db ignore esse passo_

```bash
flask init-db
```

Rode o projeto

```bash
flask run
```

Finalizando o ambiente

```bash
deactivate
```

## Documentação da API

#### Retorna um ambiente para testar as rotas

```http
  GET /
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| Nenhum | - | Essa rota não requer parâmetros na requisição. |

---

#### Retorna o status da API e informações do servidor

```http
  GET /apistatus
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| Nenhum | - | Essa rota não requer parâmetros na requisição. |

---

#### Login de usuário

```http
  GET /login
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `username`      | `string` | **Obrigatório**.  |
| `password`      | `string` | **Obrigatório**.  |


---

#### Registrar usuário

```http
  POST /register
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `username`      | `string` | **Obrigatório**.  |
| `email`      | `string` | **Obrigatório**.  |
| `password`      | `string` | **Obrigatório**.  |

---

#### Visualizar usuários do sistema

```http
  GET /users
```

| Headers   | Value                                   |
| :---------- |  :------------------------------------------ |
| `Authorization` | Bearer  { token }  |


---

#### Visualizar um usuário do sistema

```http
  GET /get_user/<int:user_id>
```

| Headers   | Value                                   |
| :---------- |  :------------------------------------------ |
| `Authorization` | Bearer  { token }  |


| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `user_id`      | `int` | **Obrigatório** Enviado via url.  |

---

#### Excluir um usuário do sistema

```http
  DELETE /user/<int:user_id>
```

| Headers   | Value                                   |
| :---------- |  :------------------------------------------ |
| `Authorization` | Bearer  { token }  |


| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `user_id`      | `int` | **Obrigatório** Enviado via url.  |


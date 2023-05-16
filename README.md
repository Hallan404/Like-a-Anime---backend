# Like-a-Anime---backend

# Backend do Sistema de Recomendação de Animes

Este repositório contém o código-fonte do backend do Sistema de Recomendação de Animes, 
um projeto desenvolvido como parte de um trabalho acadêmico Projeto Integrador IV - Desenvolvimento de Portais.
O backend é responsável por gerenciar a lógica de negócio, o banco de dados e fornecer a API para comunicação 
com o front-end.

## Tecnologias Utilizadas

O backend foi desenvolvido utilizando as seguintes tecnologias:

- **Python**: Linguagem de programação utilizada para desenvolver o backend.
- **Flask**: Framework web utilizado para criar a API do sistema.
- **SQLAlchemy**: Biblioteca de mapeamento objeto-relacional (ORM) utilizada para interagir com o banco de dados SQLite.
- **SQLite**: Banco de dados utilizado para armazenar as informações sobre os animes e os usuários.
- **Gunicorn**: Servidor HTTP utilizado para executar o backend em produção.

## Configuração do Ambiente

Siga as etapas abaixo para configurar o ambiente de desenvolvimento:

1. Certifique-se de ter o Python instalado em sua máquina. Recomenda-se utilizar a versão 3.7 ou superior.

2. Clone este repositório em sua máquina local:

   ```
   git clone https://github.com/seu-usuario/backend-recomendacao-animes.git
   ```

3. Acesse o diretório do projeto:

   ```
   cd backend-recomendacao-animes
   ```

4. Crie um ambiente virtual para isolar as dependências do projeto:

   ```
   python -m venv venv
   ```

5. Ative o ambiente virtual:

   - No Linux/Mac:

     ```
     source venv/bin/activate
     ```

   - No Windows:

     ```
     venv\Scripts\activate
     ```

6. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```

## Configuração do Banco de Dados

O backend utiliza um banco de dados SQLite para armazenar as informações sobre os animes e os usuários. Certifique-se de ter o arquivo `portal_animes.db` localizado na pasta `.instance`. Se o arquivo não existir, crie-o manualmente.

## Executando o Backend

Após configurar o ambiente e o banco de dados, você pode executar o backend do sistema. Certifique-se de estar no diretório raiz do projeto e com o ambiente virtual ativado. Execute o seguinte comando:

```
gunicorn -c gunicorn_config.py app:app
```

O backend será executado na porta 8000. Você poderá acessar a API por meio da URL `http://localhost:8000`.

## Hospedagem externa 
A API está hospedada no servidor PythnAnywere sob o link 
http://hallandeoliveira.pythonanywhere.com/

## Contribuição

Este projeto foi desenvolvido como parte de um trabalho acadêmico e não está aberto para contribuições externas no momento.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

# Sistema de Gerenciamento de Pet Shop 🐾

Este projeto é um sistema de gerenciamento completo para pet shops, desenvolvido com uma arquitetura robusta e oferecendo múltiplas funcionalidades para a gestão de clientes, animais, serviços e vendas. O sistema conta com duas interfaces (terminal e gráfica) e funcionalidades avançadas de relatórios.

## 🚀 Funcionalidades Principais

O sistema foi projetado para ser uma solução completa, oferecendo:

* **Interface Dupla**:
    * **Interface Gráfica (GUI)**: Uma interface visual e interativa desenvolvida com Pygame, facilitando o uso do sistema com elementos como botões, formulários e menus visuais.
    * **Interface de Terminal (CLI)**: A tradicional interface baseada em texto para quem prefere agilidade e simplicidade no terminal.

* **Gerenciamento Completo (CRUD)**:
    * **Donos e Pets**: Cadastro, consulta, atualização e exclusão de donos e seus animais de estimação.
    * **Produtos**: Controle de inventário de produtos, com quantidade em estoque e custo unitário.
    * **Serviços**: Cadastro de serviços (banho, tosa, etc.), especificando preço e os produtos necessários para cada um.
    * **Despesas**: Registro de despesas operacionais como aluguel, salários e contas.

* **Fluxo de Trabalho Operacional**:
    * **Agendamentos**: Sistema para marcar serviços para os pets, com verificação de conflito de horário e de estoque de produtos. Os agendamentos podem ser cancelados.
    * **Vendas**: Módulo para registrar a venda de um serviço agendado, calculando o valor total com base nos custos, preço do serviço e margem de lucro customizável.

* **Persistência de Dados**:
    * Todo o estado do sistema (cadastros, vendas, agendamentos) é salvo automaticamente em um arquivo `petshop_data.pkl` ao sair.
    * Os dados são carregados ao iniciar a aplicação, garantindo que nenhuma informação seja perdida entre as sessões.

* **Relatórios Avançados**:
    * O sistema gera múltiplos relatórios para análise de negócio, acessíveis tanto pela interface de terminal quanto pela gráfica.
    * **Relatório Geral de Vendas**: Métricas como faturamento total, quantidade de vendas, ticket médio, e valores da maior e menor venda.
    * **Rankings de Desempenho**:
        * **Donos por Gasto**: Lista os clientes que mais investem no pet shop.
        * **Pets por Vendas**: Identifica os animais que mais utilizaram serviços.
        * **Produtos Mais Usados**: Mostra os produtos com maior rotatividade.
        * **Serviços Mais Vendidos**: Aponta os serviços mais populares.

* **População de Dados para Teste**:
    * Para facilitar a demonstração e o teste, o sistema pode popular o banco de dados com uma grande quantidade de dados de exemplo, permitindo uma visualização completa das funcionalidades de relatório.

## 🛠️ Como Executar

Siga os passos abaixo para rodar o projeto em seu ambiente local.

### Pré-requisitos

* Python 3.8 ou superior
* Instale a biblioteca Pygame:
    ```bash
    pip install -r requirements.txt
    ```

### Execução

1.  Clone o repositório para a sua máquina local.

2.  Navegue até o diretório principal do projeto:
    ```bash
    cd petshop
    ```

3.  Execute o arquivo principal da aplicação:
    ```bash
    python app.py
    ```

4.  Ao iniciar, o sistema perguntará qual interface você deseja utilizar: **Terminal** ou **Gráfica (Pygame)**.

### Usando Docker

O projeto também pode ser executado em um container Docker para facilitar o setup do ambiente.

1.  Certifique-se de ter o Docker e o Docker Compose instalados.
2.  No diretório `petshop`, execute o comando:
    ```bash
    docker-compose up --build
    ```

## 🏗️ Estrutura do Projeto

O projeto segue uma arquitetura inspirada no padrão MVC (Model-View-Controller) para manter o código organizado e escalável:

* `app.py`: Ponto de entrada da aplicação. Responsável por carregar/salvar dados e iniciar a interface escolhida.
* `requirements.txt`: Lista as dependências do projeto.
* `docker-compose.yml`: Arquivo de configuração para rodar a aplicação com Docker.
* `models/`: Contém as classes que representam as entidades do sistema (ex: `Pet`, `Dono`, `Venda`).
* `views/`: Responsável pela apresentação dos dados. Contém os módulos para a interface de terminal e o módulo `pygame_view.py` para a interface gráfica.
* `controllers/`: Contém a lógica de negócio que conecta os `models` e as `views`.
* `registry/`: Centraliza a criação dos controladores para serem usados em todo o sistema.
* `utils/`: Módulos com funções auxiliares, como o de persistência de dados (`persistence.py`).
* `petshop_data.pkl`: Arquivo binário onde os dados da aplicação são armazenados (gerado após a primeira execução).

## 🧑‍🏫 Professores Responsáveis

* Douglas Hiura Longo
* André Brascher
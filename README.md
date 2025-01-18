# Automação de Tarefas com Python

Este projeto é uma automação que utiliza as bibliotecas CustomTkinter para criar uma interface gráfica de usuário (GUI) e PyAutoGUI para controlar o mouse e o teclado, automatizando tarefas do dia a dia.

## Visão Geral

A automação implementada é composta de duas partes principais:

### Interface de Login

- Uma tela inicial para autenticação do usuário.
- Valida as credenciais do usuário antes de permitir o acesso às funcionalidades da automação.

### Interface Principal

- Após o login bem-sucedido, uma nova janela exibe botões interativos.
- Cada botão executa uma tarefa específica, como abrir o LinkedIn, GitHub, YouTube, entre outros.

## Funcionalidades

- **Automação do Mouse e Teclado:** Controla o cursor e simula digitações para navegar em sites automaticamente.
- **Interface Gráfica (GUI):** Desenvolvida com CustomTkinter, garantindo um design moderno e responsivo.

### Tarefas Automatizadas:

- Abrir o LinkedIn
- Abrir o GitHub
- Abrir o YouTube
- Abrir o Postman
- Navegar para o site JWT
- Abrir a documentação oficial do Git

## Estrutura do Projeto

### Interface de Login

O programa inicializa com uma tela de login onde o usuário deve fornecer:

- E-mail
- Senha

Somente credenciais válidas (otavio e 123) permitirão o acesso à interface principal.

### Tela Principal

Após o login, o usuário visualiza 6 botões, cada um representando uma ação automatizada:

| **Botão**    | **Ação**                                            |
|--------------|-----------------------------------------------------|
| LinkedIn     | Abre o site do LinkedIn em um navegador.            |
| GitHub       | Abre o site do GitHub em um navegador.              |
| YouTube      | Abre o YouTube para acesso rápido.                  |
| Postman      | Acessa a ferramenta Postman no navegador.           |
| JWT          | Navega até o site oficial do JWT para testar tokens.|
| Git Docs     | Abre a documentação oficial do Git.                 |



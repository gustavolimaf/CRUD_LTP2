
# 🛠 CRUD de Estoque em Python - Gestão Simples pra Quem Precisa Botar a Mão na Massa

Olá! Esse projetinho foi criado durante a disciplina de Lógica e Técnicas de Programação 2 no UniCEUB. É um sistema básico de estoque que fiz enquanto aprendia na prática como integrar Python com bancos de dados.

👉 Traduzindo: Você pode cadastrar produtos, ver a lista completa, atualizar informações e excluir itens - tudo pelo terminal, de um jeito que até quem não é tech-friendly consegue usar.


## Como Faz Para Rodar isso?

1 - Primeiro, clone o repositório em seu PC:

```bash
  git clone https://github.com/gustavolimaf/CRUD_LTP2.git
```
    
2 - Entre na pasta do projeto:

```bash
    cd CRUD_LTP2    
```

3 - Coloque para rodar!

```bash
    pyhon main.pyhon
```

Pronto! O sistema já cria o banco de dados automaticamente na primeira execução.



## Funcionalidades

- **Cadastro Inteligente:** Não deixa você repetir nome de produto;

- **Controle Total:** Ajusta quantidades e preços na hora, só precisando do ID do item;

- **Lista Organizada:** Mostra tudo bonitinho numa tabela fácil de ler;

- **Exclusão com Confirmação:** Para ninguém apagar coisa sem querer;

- **Anti-Burrice:** Valida se você tá digitando número onde é preço, quantidade certa, etc.


## Exemplo da Vida Real

Imagine que você é responsável pelo controle de estoque de uma papelaria:

### Cadastrando

```bash
    Nome: Caderno Universitário
    Quantidade: 30
    Preço: 18.90
```
Output: "Produto cadastrado!"

### Tentando repetir:

```bash
    Nome: Caderno Universitário
```
Output: "Opa, esse já existe! Vê outro nome aí..."

### Atualizando estoque:

```bash
    ID: 3
    Nova Quantidade: 25
    Novo Preço: 19.75
```
Output: "Atualizado! O sistema já reflete o novo preço."
## Por Baixo Dos Panos

**Python 3.8+:** Testado até na versão 3.12

**SQLite:** O banco de dados fica num arquivo .db local)

**Tabulate:** Para deixar as tabelas bonitinhas no terminal

## Desafios

- **Nomes Duplicados:** Quase uma tarde até descobrir o UNIQUE CONSTRAINT do SQLite

- **Rollback Salvador:** Aprendi do jeito hard que transações (commit/rollback) evitam dados corrompidos

- **CLI Amigável:** Formatando tabelas para não ficar aquela lista feia de tuplas

- **Compatibilidade:** Testar em 3 versões diferentes do Python para garantir que rodava nos PCs da faculdade
## Conclusão

Esse código foi feito exclusivamente para fins acadêmicos, mas fique à vontade para:

- Usar como base para seus projetos

-  Melhorar o tratamento de erros (tenho certeza que tem edge cases que não peguei)

- Adicionar novas features (tipo busca por nome ou relatórios)

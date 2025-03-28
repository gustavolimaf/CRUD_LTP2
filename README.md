# CRUD de Gerenciamento de Estoque com SQLite

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-green)](https://www.sqlite.org/index.html)

Projeto desenvolvido para a disciplina **Lógica e Técnicas de Programação 2** do Centro Universitário de Brasília (UniCEUB).

---

## 📝 Descrição  
Sistema de gerenciamento de estoque que permite operações **CRUD** (Criar, Ler, Atualizar, Deletar) utilizando Python e SQLite. O foco está em boas práticas de programação, modularidade e tratamento robusto de erros.

---

## 🚀 Funcionalidades  
- **Banco de dados automático:** Criação e configuração inicial das tabelas  
- **Cadastro de produtos:** Nome único, quantidade e preço + validação de dados  
- **Listagem completa:** Visualização organizada de todos os produtos  
- **Atualização flexível:** Modificação de quantidade e preço por ID  
- **Exclusão segura:** Remoção de produtos com confirmação  
- **Interface CLI intuitiva:** Menu interativo em linha de comando  
- **Sistema robusto:** Tratamento de erros e validação de entradas  

---

## ⚙️ Instalação  
1. Clone o repositório:  
   ```bash  
   git clone https://github.com/gustavolimaf/CRUD_LTP2.git  
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd CRUD_LTP2  
   ```
3. Execute o programa:
   ```bash
   python main.py  
   ```

---

## 🖥 Como Utilizar  
Ao executar o programa, você verá um menu interativo:

```bash
1 - Cadastrar novo produto  
2 - Listar todos os produtos  
3 - Atualizar produto  
4 - Excluir produto  
5 - Sair  
```
Siga as instruções no terminal para cada operação.

---

## 📋 Exemplos de Uso  

### Cadastro de Produto:
```bash
Nome: Caneta  
Quantidade: 50  
Preço: 1.20  
→ Produto cadastrado com sucesso!  
```

### Tentativa de Cadastro Duplicado:
```bash
Nome: Caneta  
→ Erro: Este produto já está cadastrado!  
```

### Atualização de Produto:
```bash
ID do produto: 1  
Nova quantidade: 45  
Novo preço: 1.30  
→ Produto atualizado com sucesso!  
```

### Exclusão de Produto:
```bash
ID para excluir: 1  
→ Produto excluído com sucesso!  
```

---

## 🛠 Tecnologias Utilizadas  
- **Python 3.8+**  
- **SQLite3 (biblioteca padrão)**  

---

## 👥 Equipe  
- **Desenvolvedor:** Gustavo Lima  

---

## 📜 Licença  
Projeto desenvolvido para fins educacionais sob orientação do UniCEUB.  
Livre para uso acadêmico e aprendizado pessoal.

---

## 🧩 Estrutura do Código & Desafios  

### Principais Características:
- Modularização das funções CRUD  
- Conexão centralizada com o banco de dados  
- Validação rigorosa de inputs  
- Tratamento de exceções com `try/except`  

### Desafios Superados:
| Desafio | Solução |
|---------|----------|
| Nomes duplicados | UNIQUE CONSTRAINT + tratamento de exceções |
| Integridade dos dados | Uso de transações (commit/rollback) |
| Interface amigável | Formatação de tabelas e mensagens claras |
| Compatibilidade | Testes em múltiplas versões do Python |

Desenvolvido como requisito da disciplina **LTP2** do **UniCEUB**.

---

🔝 [Voltar ao topo](#crud-de-gerenciamento-de-estoque-com-sqlite)


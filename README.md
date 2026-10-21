# DCC075 - Segurança em Sistemas de Computação
## Atividade 01: Controle de Acesso Baseado em Papéis (RBAC)

Este repositório contém uma implementação simples e didática de um sistema com **RBAC (Role-Based Access Control)** em Python puro.

### 👥 Papéis e Permissões Definidos
O sistema modela um ambiente acadêmico com 3 papéis:
1. **`admin`**: Acesso completo (visualizar relatórios, lançar notas, gerenciar usuários e excluir registros).
2. **`professor`**: Acesso intermediário (visualizar relatórios e lançar notas).
3. **`aluno`**: Acesso básico de consulta (apenas visualizar boletim/relatórios).

### 🔑 Usuários Cadastrados (Estático)
- **Login:** `admin` | **Senha:** `123` | **Papel:** `admin`
- **Login:** `edelberto` | **Senha:** `456` | **Papel:** `professor`
- **Login:** `vitor` | **Senha:** `789` | **Papel:** `aluno`

### 🚀 Como Executar
Basta ter o Python 3 instalado e executar no terminal:
```bash
python rbac.py
```

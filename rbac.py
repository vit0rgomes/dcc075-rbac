"""
DCC075 - Segurança em Sistemas de Computação
Atividade 01 - Controle de Acesso Baseado em Papéis (RBAC - Role-Based Access Control)

Descrição:
Sistema simples de autenticação por login/senha estático no terminal e controle
de acesso (RBAC) contendo 3 papéis distintos:
1. 'admin'     -> Acesso total (criar, visualizar, editar e excluir usuários/relatórios)
2. 'professor' -> Acesso intermediário (visualizar relatórios e lançar notas)
3. 'aluno'     -> Acesso básico (apenas visualizar boletim/relatórios)

Como executar:
    python rbac.py
"""

# =====================================================================
# 1. DEFINIÇÃO DE PAPÉIS E PERMISSÕES (RBAC)
# =====================================================================
# Mapeia cada papel (função) para o conjunto de ações (permissões) permitidas
PAPEIS_PERMISSOES = {
    "admin": [
        "ver_boletim",
        "lancar_notas",
        "gerenciar_usuarios",
        "excluir_registros",
    ],
    "professor": [
        "ver_boletim",
        "lancar_notas",
    ],
    "aluno": [
        "ver_boletim",
    ],
}

# =====================================================================
# 2. BANCO DE DADOS ESTÁTICO DE USUÁRIOS
# =====================================================================
USUARIOS = {
    "admin":     {"senha": "123", "papel": "admin",     "nome": "Administrador do Sistema"},
    "edelberto": {"senha": "456", "papel": "professor", "nome": "Prof. Edelberto"},
    "vitor":     {"senha": "789", "papel": "aluno",     "nome": "Vitor Fernandes"},
}

# =====================================================================
# 3. FUNÇÕES DE AUTENTICAÇÃO E AUTORIZAÇÃO
# =====================================================================
def autenticar(login: str, senha: str):
    """Verifica se o login existe e se a senha corresponde ao cadastro estático."""
    usuario = USUARIOS.get(login)
    if usuario and usuario["senha"] == senha:
        return usuario
    return None


def tem_permissao(papel: str, acao: str) -> bool:
    """Verifica na matriz RBAC se o papel do usuário possui a permissão solicitada."""
    permissoes_do_papel = PAPEIS_PERMISSOES.get(papel, [])
    return acao in permissoes_do_papel


def executar_acao(usuario: dict, acao: str, descricao_acao: str):
    """Tenta executar uma ação no sistema validando antes a permissão via RBAC."""
    papel = usuario["papel"]

    if tem_permissao(papel, acao):
        print(f"  [ACESSO PERMITIDO] Usuário '{usuario['nome']}' (papel: '{papel}') executou '{descricao_acao}' com sucesso!")
    else:
        print(f"  [ACESSO NEGADO] O papel '{papel}' NÃO possui a permissão '{acao}'.")


# =====================================================================
# 4. INTERFACE NO TERMINAL
# =====================================================================
def menu_principal():
    print("=" * 60)
    print("       SISTEMA ACADÊMICO - DEMONSTRAÇÃO RBAC")
    print("=" * 60)
    print("Usuários disponíveis para teste:")
    print("  - Login: admin     | Senha: 123 | Papel: admin")
    print("  - Login: edelberto | Senha: 456 | Papel: professor")
    print("  - Login: vitor     | Senha: 789 | Papel: aluno")
    print("-" * 60)

    login = input("Digite seu login: ").strip()
    senha = input("Digite sua senha: ").strip()

    usuario = autenticar(login, senha)
    if not usuario:
        print("\n[ERRO] Login ou senha inválidos! Encerrando.")
        return

    papel = usuario["papel"]
    permissoes = PAPEIS_PERMISSOES.get(papel, [])
    print(f"\n[SUCESSO] Bem-vindo(a), {usuario['nome']}!")
    print(f"Seu papel atribuído: {papel.upper()}")
    print(f"Suas permissões ativas: {', '.join(permissoes)}")

    # Loop de opções do sistema para testar o controle de acesso
    opcoes = {
        "1": ("ver_boletim", "Visualizar Boletim e Relatórios"),
        "2": ("lancar_notas", "Lançar/Editar Notas de Alunos"),
        "3": ("gerenciar_usuarios", "Cadastrar/Gerenciar Usuários"),
        "4": ("excluir_registros", "Excluir Registros do Sistema"),
    }

    while True:
        print("\n" + "-" * 40)
        print("Escolha uma ação para testar seu nível de acesso:")
        print("  1 - Visualizar Boletim (Requer: ver_boletim)")
        print("  2 - Lançar Notas       (Requer: lancar_notas)")
        print("  3 - Gerenciar Usuários (Requer: gerenciar_usuarios)")
        print("  4 - Excluir Registros  (Requer: excluir_registros)")
        print("  0 - Sair")
        escolha = input("Opção: ").strip()

        if escolha == "0":
            print("Saindo do sistema. Até logo!")
            break
        elif escolha in opcoes:
            acao, descricao = opcoes[escolha]
            executar_acao(usuario, acao, descricao)
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()

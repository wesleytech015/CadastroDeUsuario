usuarios = []

def adicionar_usuario(nome, idade):
    if nome.strip() != "" and idade > 0:
        usuarios.append({"nome": nome, "idade": idade})
        print(f"Usuário {nome} cadastrado com sucesso!")
    elif nome.strip() == "":
        print("Erro: nome inválido. Usuário não cadastrado.")
    else:
        print(f"Erro: idade inválida ({idade}). Usuário {nome} não cadastrado.")

def listar_usuarios():
    print("\nLISTA DE USUÁRIOS:")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for u in usuarios:
            print(f"Usuário: {u['nome']}, Idade: {u['idade']}")

def buscar_usuario(nome):
    for u in usuarios:
        if u["nome"] == nome:
            return u
    return f"Usuário {nome} não encontrado"


# Testes
print("USUÁRIOS CADASTRADOS:")
adicionar_usuario("Wesley", 29)
adicionar_usuario("Eliezer", 37)
adicionar_usuario("João", -5)  # idade inválida
adicionar_usuario("", 22)      # nome inválido

listar_usuarios()

print("\nBUSCAS:")
print("Buscar Wesley:", buscar_usuario("Wesley"))
print("Buscar Eliezer:", buscar_usuario("Eliezer"))
print("Buscar João:", buscar_usuario("João"))

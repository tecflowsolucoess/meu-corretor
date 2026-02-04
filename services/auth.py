import bcrypt

USUARIOS = {
    "admin@admin.com": {
        "senha": bcrypt.hashpw("admin123".encode(), bcrypt.gensalt()),
        "tipo": "admin"
    },
    "corretor@teste.com": {
        "senha": bcrypt.hashpw("123456".encode(), bcrypt.gensalt()),
        "tipo": "corretor"
    }
}

def autenticar(email, senha):
    user = USUARIOS.get(email)
    if not user:
        return False, None

    if bcrypt.checkpw(senha.encode(), user["senha"]):
        return True, user["tipo"]

    return False, None

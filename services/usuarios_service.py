from services.supabase_client import supabase

# =========================
# CADASTRAR USUÁRIO
# =========================
def criar_usuario(email, senha, nome):
    existente = supabase.table("usuarios").select("*").eq("email", email).execute()

    if existente.data:
        return {"erro": "E-mail já cadastrado"}

    response = supabase.table("usuarios").insert({
        "email": email,
        "senha": senha,
        "nome": nome
    }).execute()

    return response.data[0]


# =========================
# LOGIN
# =========================
def autenticar_usuario(email, senha):
    response = supabase.table("usuarios") \
        .select("*") \
        .eq("email", email) \
        .eq("senha", senha) \
        .single() \
        .execute()

    return response.data

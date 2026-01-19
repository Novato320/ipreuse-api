from supabase import create_client, Client

url: str = "https://hkdmjetyhvepudotkcjr.supabase.co"
key: str = "sb_publishable_GoINKSbl3Y_5J7N5lXhBWA_8RQfkJ6T"
supabase: Client = create_client(url, key)

def consultar_banco():
    response = (
        supabase.table("users")
        .select("*")
        .execute()
    )

    return response


# Não testei, mas acredito que não vai funcionar
def escrever_banco():
    response = (
    supabase.table("users")
    .insert({"id": 1, "name": "José"})
    .execute()
    )

    return response

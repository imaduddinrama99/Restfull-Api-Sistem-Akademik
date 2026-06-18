from config import supabase

def get_all():
    response = supabase.table("mahasiswa").select("*").execute()
    return response.data

def get_by_id(mhs_id):
    response = supabase.table("mahasiswa").select("*").eq("id", mhs_id).execute()
    return response.data[0] if response.data else None

def insert(data):
    response = supabase.table("mahasiswa").insert(data).execute()
    return response.data

def update(mhs_id, data):
    response = supabase.table("mahasiswa").update(data).eq("id", mhs_id).execute()
    return response.data

def delete(mhs_id):
    response = supabase.table("mahasiswa").delete().eq("id", mhs_id).execute()
    return response.data
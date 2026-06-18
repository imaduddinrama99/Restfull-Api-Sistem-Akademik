import os
from dotenv import load_dotenv
from supabase import create_client

# Load variabel dari file .env
load_dotenv()

URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(URL, KEY)

def get_all_mahasiswa():
    response = supabase.table("mahasiswa").select("*").execute()
    return response.data

def get_mahasiswa_by_id(mhs_id):
    response = supabase.table("mahasiswa").select("*").eq("id", mhs_id).execute()
    return response.data[0] if response.data else None

def insert_mahasiswa(data):
    response = supabase.table("mahasiswa").insert(data).execute()
    return response.data

def update_mahasiswa(mhs_id, data):
    response = supabase.table("mahasiswa").update(data).eq("id", mhs_id).execute()
    return response.data

def delete_mahasiswa(mhs_id):
    response = supabase.table("mahasiswa").delete().eq("id", mhs_id).execute()
    return response.data

# login user
def login_user(email, password):
    response = supabase.auth.sign_in_with_password({
        "email": email, 
        "password": password
    })
    return response
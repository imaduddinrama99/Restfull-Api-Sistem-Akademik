from config import supabase

def login(email, password):
    response = supabase.auth.sign_in_with_password({
        "email": email, 
        "password": password
    })
    return response
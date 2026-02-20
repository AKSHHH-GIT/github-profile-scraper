from supabase import create_client

# Replace with your actual credentials
SUPABASE_URL = "https://iydkqdjkxiqnvarhjgke.supabase.co/"
SUPABASE_KEY = "sb_publishable_w_n0BVy4DhIZ5GdPCqWYOA_nNT58ztP"

# Create connection
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Supabase connected successfully!")

data = {
    "username": "test_user",
    "name": "Test Name",
    "bio": "Testing insert",
    "followers": 1,
    "following": 2,
    "repositories": 3
}

response = supabase.table("github_profiles").insert(data).execute()

print(response)
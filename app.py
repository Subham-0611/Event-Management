from flask import Flask, render_template, request, redirect
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

# Load Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Insert data into Supabase table (e.g., 'registrations')
    response = supabase.table("registrations").insert({
        "name": name,
        "email": email
    }).execute()

    print(response)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

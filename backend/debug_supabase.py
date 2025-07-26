#!/usr/bin/env python3
"""
Script para debugar a conexão com Supabase
"""

import requests
import json

def test_supabase_connection():
    url = "https://fkhjspuygbheanjxqnin.supabase.co"
    
    # Testar com anon key
    anon_key = "sb_publishable_n8J2U_j-YBC4m6BiZaVFjQ_Aix2xr4d"
    
    headers = {
        "apikey": anon_key,
        "Authorization": f"Bearer {anon_key}"
    }
    
    print("🔍 Testando conexão com Supabase...")
    print(f"URL: {url}")
    print(f"Anon Key: {anon_key[:20]}...")
    
    try:
        # Testar endpoint de health
        response = requests.get(f"{url}/rest/v1/", headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:200]}...")
        
        if response.status_code == 200:
            print("✅ Conexão com anon key funcionou!")
            return True
        else:
            print("❌ Erro na conexão")
            return False
            
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return False

if __name__ == "__main__":
    test_supabase_connection() 
import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações do Supabase
SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://wevzbdepfqsryagiemcz.supabase.co')
SUPABASE_ANON_KEY = os.getenv('SUPABASE_ANON_KEY', 'sb_publishable_-1Jg5reJGbOE4-wojnO8Xw_wEa1tBXv')

# Criar cliente Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

def get_supabase_client():
    """Retorna o cliente Supabase configurado"""
    return supabase

def test_connection():
    """Testa a conexão com o Supabase"""
    try:
        # Tenta fazer uma consulta simples
        response = supabase.table('users').select('count').limit(1).execute()
        return True, "Conexão com Supabase estabelecida com sucesso"
    except Exception as e:
        return False, f"Erro na conexão com Supabase: {str(e)}" 
"""
Configurações da aplicação
"""

import os
from typing import Optional

class Config:
    """Configuração base"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = False
    TESTING = False
    
    # Supabase
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_ANON_KEY = os.environ.get('SUPABASE_ANON_KEY')
    
    # CORS
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*').split(',')
    
    @classmethod
    def is_supabase_configured(cls) -> bool:
        """Verifica se o Supabase está configurado"""
        return bool(cls.SUPABASE_URL and cls.SUPABASE_ANON_KEY)

class DevelopmentConfig(Config):
    """Configuração para desenvolvimento"""
    DEBUG = True
    CORS_ORIGINS = ['http://localhost:3000', 'http://localhost:5173']

class ProductionConfig(Config):
    """Configuração para produção"""
    DEBUG = False

class TestingConfig(Config):
    """Configuração para testes"""
    TESTING = True
    DEBUG = True

def get_config() -> Config:
    """Retorna a configuração baseada no ambiente"""
    env = os.environ.get('FLASK_ENV', 'development')
    
    if env == 'production':
        return ProductionConfig()
    elif env == 'testing':
        return TestingConfig()
    else:
        return DevelopmentConfig() 
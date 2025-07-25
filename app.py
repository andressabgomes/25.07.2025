#!/usr/bin/env python3
import os
import sys

# Adicionar o diretório backend ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Importar e executar a aplicação
try:
    from src.main import app
    print("✅ App importado com sucesso")
except ImportError as e:
    print(f"❌ Erro ao importar app: {e}")
    sys.exit(1)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Iniciando servidor na porta {port}")
    app.run(host='0.0.0.0', port=port, debug=False)


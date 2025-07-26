# 🔑 Como Obter as Chaves do Supabase

## 📍 Localização das Chaves

### 1. Acesse o Painel do Supabase
- Vá para: https://supabase.com/dashboard
- Faça login na sua conta
- Selecione o projeto: `wevzbdepfqsryagiemcz` (CajáIT)

### 2. Vá para Settings > API
- No menu lateral esquerdo, clique em **Settings** (ícone de engrenagem)
- Clique em **API**

### 3. Encontre as Chaves
Na página de API, você verá:

#### 🔓 Project API keys
- **anon public**: `sb_...` (chave anônima para frontend)
- **service_role secret**: `sb_...` (chave secreta para backend)

#### 📍 Project URL
- **Project URL**: `https://wevzbdepfqsryagiemcz.supabase.co`

## 🔧 Atualizar Configuração

### Frontend (`frontend/src/lib/supabase.js`)
```javascript
const supabaseUrl = 'https://wevzbdepfqsryagiemcz.supabase.co'
const supabaseAnonKey = 'SUA_CHAVE_ANON_AQUI'
```

### Backend (`backend/src/lib/supabase.py`)
```python
SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://wevzbdepfqsryagiemcz.supabase.co')
SUPABASE_ANON_KEY = os.getenv('SUPABASE_ANON_KEY', 'SUA_CHAVE_ANON_AQUI')
```

## ✅ Testar a Configuração

Após atualizar as chaves, execute:

```bash
cd backend
source venv/bin/activate
python3 test_supabase.py
```

## 🎯 Próximos Passos

1. **Copie a chave anônima** do painel do Supabase
2. **Atualize os arquivos** de configuração
3. **Teste a conexão** com o script
4. **Execute o teste completo** de integração

---

**Nota**: A chave anônima é segura para usar no frontend, mas a service_role deve ser mantida secreta e usada apenas no backend. 
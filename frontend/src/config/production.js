// Configuração para produção
export const config = {
  // Em produção, o Vercel fará proxy para o Railway automaticamente
  API_BASE_URL: '/api',
  
  // Configurações do Supabase
  SUPABASE_URL: 'https://wevzbdepfqsryagiemcz.supabase.co',
  SUPABASE_ANON_KEY: 'sb_publishable_-1Jg5reJGbOE4-wojnO8Xw_wEa1tBXv',
  
  // Configurações da aplicação
  APP_NAME: 'Customer Support Cajá',
  VERSION: '1.0.0'
};

// Detectar ambiente
export const isProduction = import.meta.env.PROD;
export const isDevelopment = import.meta.env.DEV;

// URL base da API baseada no ambiente
export const getApiBaseUrl = () => {
  if (isProduction) {
    return '/api'; // Vercel fará proxy para Railway
  }
  return 'https://5000-iadtp2mmvuwiqjt6mjfgw-2caab039.manusvm.computer/api'; // Desenvolvimento local
}; 
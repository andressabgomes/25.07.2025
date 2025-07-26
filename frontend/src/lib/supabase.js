import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://wevzbdepfqsryagiemcz.supabase.co'
const supabaseAnonKey = 'sb_publishable_-1Jg5reJGbOE4-wojnO8Xw_wEa1tBXv'

export const supabase = createClient(supabaseUrl, supabaseAnonKey)

// Configuração para desenvolvimento
if (import.meta.env.DEV) {
  console.log('Supabase configurado para desenvolvimento')
} 
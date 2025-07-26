-- Inserir usuários (com senhas)
INSERT INTO users (email, name, role, password) VALUES
('admin@teste.com', 'Administrador', 'admin', 'admin123'),
('carlos@teste.com', 'Carlos Silva', 'agent', '123456'),
('manager@teste.com', 'Manager', 'manager', '123456');

-- Inserir clientes
INSERT INTO customers (name, email, phone, company) VALUES
('João Silva', 'joao@empresa.com', '(11) 99999-9999', 'Empresa ABC'),
('Maria Santos', 'maria@startup.com', '(21) 88888-8888', 'Startup XYZ');

-- Inserir tickets
INSERT INTO tickets (title, description, status, priority) VALUES
('Problema com login', 'Não consigo fazer login no sistema', 'open', 'high'),
('Dúvida sobre funcionalidade', 'Como usar a nova funcionalidade X?', 'open', 'medium'); 
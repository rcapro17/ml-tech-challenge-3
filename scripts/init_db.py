# scripts/init_db.py

import sys
import os
from sqlalchemy import text

# Ajusta o path para importar módulos do src
# (Necessário para que a importação de src.db funcione)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.db import get_engine

# Caminho para o script SQL de inicialização
SQL_FILE_PATH = os.path.join(
    os.path.dirname(__file__), 
    '..', 
    'infra', 
    'db', 
    'init'
)

def init_db():
    print("Inicializando o banco de dados...")
    
    # 1. Conecta usando o Engine configurado (que agora tem as credenciais corretas)
    engine = get_engine()
    
    # 2. Lê o conteúdo do arquivo SQL
    try:
        with open(SQL_FILE_PATH, 'r') as f:
            sql_script = f.read()
    except FileNotFoundError:
        print(f"ERRO: Arquivo SQL não encontrado em: {SQL_FILE_PATH}")
        sys.exit(1)

    # 3. Executa o script SQL
    # Nota: O autocommit é importante para scripts DDL (CREATE TABLE)
    with engine.connect().execution_options(autocommit=True) as conn:
        print("Executando script SQL para criar tabelas...")
        conn.execute(text(sql_script)) 
        print("Tabelas 'series' e 'observations' criadas/verificadas com sucesso.")

if __name__ == "__main__":
    init_db()
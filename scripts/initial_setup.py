# scripts/initial_setup.py

import subprocess
import sys
import os
import time

# O primeiro passo é garantir que as tabelas existam (se você não o fez no pgAdmin)
# Vamos usar o script init_db.py que sugeri antes
print("--- 1. EXECUTANDO CRIAÇÃO DE TABELAS ---")
try:
    # Usando o init_db.py (ou o script que executa seu SQL)
    import init_db 
    init_db.init_db()
except Exception as e:
    print(f"Erro na inicialização do DB: {e}")
    sys.exit(1)

# O restante do pipeline deve estar nos seus scripts existentes:

# 2. COLETA/ETL: Coletar os dados da API e salvá-los no DB (series e observations)
# (Assumindo que você tem um script para isso, talvez um collect_daily.py ou similar)
print("--- 2. EXECUTANDO COLETA E INGESTÃO DE DADOS ---")
try:
    # Use subprocess para rodar seu script de ingestão (ex: scripts/collect_data.py)
    # Se você não tem um, este é o passo que falta!
    subprocess.run([sys.executable, 'scripts/collect_data.py'], check=True) 
    print("Ingestão de dados concluída.")
except FileNotFoundError:
    print("AVISO: Script de coleta não encontrado. Pulando ingestão. VERIFIQUE SEUS DADOS!")
except Exception as e:
    print(f"Erro na coleta/ingestão: {e}")

# 3. TREINAMENTO: Treinar o modelo e salvar o resultado (registry, data/models)
print("--- 3. EXECUTANDO TREINAMENTO E SALVAMENTO DO MODELO ---")
try:
    # Assumindo que scripts/train_save.py faz o treinamento completo
    subprocess.run([sys.executable, 'scripts/train_save.py'], check=True)
    print("Treinamento de modelo concluído.")
except Exception as e:
    print(f"Erro no treinamento: {e}")


print("--- SETUP INICIAL COMPLETO. PRONTO PARA INICIAR O SERVIDOR. ---")
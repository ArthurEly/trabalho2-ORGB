# -*- coding: utf-8 -*-

import os
import subprocess

# Caminho para o diretório onde estão os executáveis e para o gem5
orgb_progs_dir = 'orgb_progs'
gem5_executable = '/path/to/gem5'
simulate_script = 'orgb_configs/simulate.py'

# Verifica se a pasta orgb_progs existe
if not os.path.isdir(orgb_progs_dir):
    print("A pasta orgb_progs não foi encontrada!")
    exit(1)

# Lista todos os arquivos no diretório orgb_progs
executables = [f for f in os.listdir(orgb_progs_dir) if os.path.isfile(os.path.join(orgb_progs_dir, f))]

# Executa cada executável usando o gem5
for exe in executables:
    exe_path = os.path.join(orgb_progs_dir, exe)
    
    # Verifica se o arquivo é executável
    if os.access(exe_path, os.X_OK):
        print("Executando {} com gem5...".format(exe))
        
        try:
            subprocess.run([gem5_executable, simulate_script, 'run-benchmark', '-c', exe_path], check=True)
            print("{} executado com sucesso.\n".format(exe))
        except subprocess.CalledProcessError as e:
            print("Erro ao executar {}: {}\n".format(exe, e))
    else:
        print("{} não é executável.\n".format(exe))

print("Todos os executáveis foram executados com gem5.")

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
        print(f"Executando {exe} com gem5...")
        
        try:
            subprocess.run([gem5_executable, simulate_script, 'run-benchmark', '-c', exe_path], check=True)
            print(f"{exe} executado com sucesso.\n")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar {exe}: {e}\n")
    else:
        print(f"{exe} não é executável.\n")

print("Todos os executáveis foram executados com gem5.")

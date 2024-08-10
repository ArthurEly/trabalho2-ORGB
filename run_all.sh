#!/bin/bash

# Altera o diretório para o local correto
cd /home/orgb/gem5 || { echo "Não foi possível entrar no diretório /home/orgb/gem5"; exit 1; }

# Verifica se a pasta orgb_progs existe
if [ ! -d "orgb_progs" ]; then
    echo "A pasta orgb_progs não foi encontrada!"
    exit 1
fi

# Executa todos os arquivos que são executáveis na pasta orgb_progs
for file in orgb_progs/*; do
    if [ -x "$file" ] && [ ! -d "$file" ]; then
        echo "Executando $(basename "$file") com gem5..."
        ./gem5 orgb_configs/simulate.py run-benchmark -c "$file"
        echo "$(basename "$file") executado."
        echo ""
    fi
done

echo "Todos os executáveis foram executados com gem5."

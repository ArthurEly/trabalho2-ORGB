#!/bin/bash

# Altera o diretório para o local correto
cd /home/orgb/gem5 || { echo "Não foi possível entrar no diretório /home/orgb/gem5"; exit 1; }

# Verifica se a pasta orgb_progs existe
if [ ! -d "orgb_progs" ]; then
    echo "A pasta orgb_progs não foi encontrada!"
    exit 1
fi

# Entra na pasta orgb_progs
cd orgb_progs

# Executa todos os arquivos que são executáveis
for file in *; do
    if [ -x "$file" ] && [ ! -d "$file" ]; then
        echo "Executando $file com gem5..."
        /home/orgb/gem5/gem5 orgb_configs/simulate.py run-benchmark -c "orgb_progs/$file"
        echo "$file executado."
        echo ""
    fi
done

echo "Todos os executáveis foram executados com gem5."

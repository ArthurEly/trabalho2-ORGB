#!/bin/bash

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
        echo "Executando $file..."
        ./"$file"
        echo "$file executado."
        echo ""
    fi
done

echo "Todos os executáveis foram executados."

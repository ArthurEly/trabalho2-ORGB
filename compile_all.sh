#!/bin/bash

# Verifica se a pasta orgb_progs existe
if [ ! -d "orgb_progs" ]; then
    echo "A pasta orgb_progs não foi encontrada!"
    exit 1
fi

# Entra na pasta orgb_progs
cd orgb_progs

# Compila todos os arquivos .c na pasta
for file in *.c; do
    if [ -f "$file" ]; then
        # Extrai o nome do arquivo sem a extensão .c
        output_file="${file%.c}"
        echo "Compilando $file para $output_file..."
        gcc -o "$output_file" "$file"

        # Verifica se a compilação foi bem-sucedida
        if [ $? -ne 0 ]; then
            echo "Erro ao compilar $file"
        else
            echo "$file compilado com sucesso!"
        fi
    fi
done

echo "Todos os arquivos foram compilados."

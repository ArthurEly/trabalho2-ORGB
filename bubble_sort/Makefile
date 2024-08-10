# Nome do executável
TARGET = bubble_sort

# Nome do arquivo fonte
SRC = bubble_sort.c

# Compilador
CC = gcc

# Flags de compilação
CFLAGS = -Wall -O2

# Regra padrão
all: $(TARGET)

# Regra para compilar o executável
$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

# Regra para limpar os arquivos de compilação
clean:
	rm -f $(TARGET)

import matplotlib.pyplot as plt

# Dados para o gráfico
configurations = ['Conf 1a', 'Conf 1b', 'Conf 1c', 'Conf 1d', 'Conf 1e']
crc = [6, 7, 7.5, 8, 9]
fft1 = [4, 5, 5.5, 6, 7]
mm = [2, 3, 3.5, 4, 5]

# Criação do gráfico
plt.plot(configurations, crc, marker='o', color='green', label='crc')
plt.plot(configurations, fft1, marker='o', color='red', label='fft1')
plt.plot(configurations, mm, marker='o', color='blue', label='mm')

# Adiciona título e rótulos
plt.title('Impacto das Modificações nos Parâmetros')
plt.xlabel('Cada modificação no parâmetro escolhido')
plt.ylabel('IPC')

# Limites dos eixos
plt.ylim(0, 10)

# Adiciona a legenda
plt.legend()

# Adiciona uma grade ao gráfico
plt.grid(True)

# Salvar o gráfico como uma imagem
plt.savefig('grafico_ipc.png')

# Mostra o gráfico na tela
plt.show()

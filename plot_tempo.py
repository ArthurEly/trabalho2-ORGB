import matplotlib.pyplot as plt

def plot_graph(configurations, data, title, ylabel, output_filename, y_min=None, y_max=None, color='blue'):
    plt.clf()
    
    plt.figure(figsize=(8, 5))

    # Criação do gráfico
    plt.plot(configurations, data, marker='o', color=color, label=title)
    
    # Adiciona título e rótulos
    plt.title(f'Impacto das Modificações nos Parâmetros - {title}')
    plt.xlabel('Cada modificação no parâmetro escolhido')
    plt.ylabel(ylabel)
    
    # Limites dos eixos
    if y_min is not None and y_max is not None:
        plt.ylim(y_min, y_max)
    
    # Adiciona a legenda
    plt.legend()

    # Adiciona uma grade ao gráfico
    plt.grid(True)
    
    # Salvar o gráfico como uma imagem
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    
    # Mostra o gráfico na tela
    plt.show()

# Dados para o gráfico
configurations = ['Conf 0', 'Conf 1', 'Conf 2', 'Conf 3', 'Conf 4', 'Conf 5', 'Conf 6', 'Conf 7', 'Conf 8', 'Conf 9']
bubble_sort = [0.014521, 0.014518, 0.014520, 0.014515, 0.014521, 0.014521, 0.014521, 0.015956, 0.015928, 0.015929]
primos = [0.043724,0.043729,0.043720,0.043729,0.043724,0.043724,0.043724,0.043624, 0.043602,0.043605]
desvios = [0.007126, 0.007091, 0.007100, 0.007103, 0.007126, 0.007126, 0.007126, 0.007311, 0.007224, 0.007239]

# Gráfico para bubble_sort
plot_graph(configurations, bubble_sort, 'Bubble Sort', 'Tempo de execução', '2grafico_tempo_bubble_sort.png', y_min=0.014, y_max=0.016, color='green')

# Gráfico para primos
plot_graph(configurations, primos, 'Primos', 'Tempo de execução', '2grafico_tempo_primos.png', y_min=0.043, y_max=0.044, color='red')

# Gráfico para desvios
plot_graph(configurations, desvios, 'Desvios', 'Tempo de execução', '2grafico_tempo_desvios.png', y_min=0.007, y_max=0.0074, color='blue')

import matplotlib.pyplot as plt

def plot_graph(configurations, data, title, ylabel, output_filename, y_min=None, y_max=None, color='blue'):
    plt.clf()
    
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
    plt.savefig(output_filename)
    
    # Mostra o gráfico na tela
    plt.show()

# Dados para o gráfico
configurations = ['Conf 0', 'Conf 1', 'Conf 2', 'Conf 3', 'Conf 4', 'Conf 5', 'Conf 6', 'Conf 7', 'Conf 8', 'Conf 9']
bubble_sort  = [0.610768, 0.610879, 0.610793, 0.611017, 0.610768, 0.610768, 0.610768, 0.555838, 0.556824, 0.556776]
primos =[0.216170, 0.216147, 0.216189, 0.216142, 0.216170, 0.216170, 0.216170, 0.216663, 0.216775, 0.216757]
desvios = [0.503632,0.506144,0.505477,0.505295,0.503632,0.503632,0.503632,0.490929,0.496852,0.495772]

# Gráfico para bubble_sort
plot_graph(configurations, bubble_sort, 'Bubble Sort', 'Instruções por ciclo', 'grafico_ipc_bubble_sort.png', y_min=0.55, y_max=0.62, color='green')

# Gráfico para primos
plot_graph(configurations, primos, 'Primos', 'Instruções por ciclo', 'grafico_ipc_primos.png', y_min=0.21, y_max=0.22, color='red')

# Gráfico para desvios
plot_graph(configurations, desvios, 'Desvios', 'Instruções por ciclo', 'grafico_ipc_desvios.png', y_min=0.49, y_max=0.51, color='blue')

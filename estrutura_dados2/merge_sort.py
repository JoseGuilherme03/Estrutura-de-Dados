import time

# Contador global para comparações
comparacoes = 0

def mergesort(lista, inicio=0, fim=None):
    global comparacoes

    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        comparacoes += merge(lista, inicio, meio, fim)


def merge(lista, inicio, meio, fim):
    global comparacoes

    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    comparacoes_merge = 0

    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left += 1
        else:
            comparacoes += 1  # Contabiliza a comparação globalmente
            comparacoes_merge += 1  # Contabiliza a comparação localmente
            if left[top_left] <= right[top_right]:
                lista[k] = left[top_left]
                top_left += 1
            else:
                lista[k] = right[top_right]
                top_right += 1

    return comparacoes_merge  # Retorna o número de comparações locais feitas nesta fusão


# Função para executar o Merge Sort e exibir resultados
def execute_mergesort(dataset):
    global comparacoes
    comparacoes = 0

    start_time = time.perf_counter()
    mergesort(dataset)
    end_time = time.perf_counter()

    print(dataset)
    print(f"Tempo: {end_time - start_time:.10f} segundos")
    print(f"Comparações: {comparacoes}")
    print("Trocas: N/A")
    print("")

# Exemplo de uso com os datasets fornecidos
dataset1 = [87, 91, 2, 15, 60, 78, 99, 58, 23, 37]
dataset2 = [231, 103, 52, 233, 493, 85, 110, 68, 320, 235, 323, 457, 295, 445, 227, 396, 449, 276, 232, 450, 382, 284, 272, 341, 46, 376, 485, 245, 427, 150, 19, 200, 82, 310, 172, 74, 203, 352, 392, 53, 69, 173, 470, 11, 178, 47, 127, 431, 13, 249]
dataset3 = [117, 143, 505, 212, 717, 708, 169, 298, 897, 140, 731, 635, 20, 769, 351, 721, 119, 330, 935, 819, 148, 514, 801, 311, 74, 880, 592, 567, 430, 156, 726, 112, 892, 75, 281, 884, 504, 634, 252, 399, 141, 214, 774, 498, 397, 953, 648, 163, 519, 6, 253, 917, 966, 740, 17, 978, 685, 64, 750, 603, 739, 913, 370, 348, 965, 586, 912, 679, 270, 4, 537, 500, 825, 400, 867, 539, 1000, 28, 734, 157, 826, 201, 5, 932, 125, 969, 788, 818, 996, 308, 918, 245, 618, 814, 128, 854, 506, 251, 136, 562]

execute_mergesort(dataset1)
execute_mergesort(dataset2)
execute_mergesort(dataset3)

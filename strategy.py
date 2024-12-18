from abc import ABC, abstractmethod
import random

# Classe abstrata que contém o método de ordenação que vamos utilizar
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        pass

    def __repr__(self):
        # Retornando string que "explica" a estratégia
        return f"{self._name} sort"

# Implementando diferentes estratégias
# Bubble sort
class BubbleSortStrategy(SortStrategy):
    # Dando nome para a estratégia
    _name = "Bubble"

    def sort(self, data: list[int]) -> list[int]:
        # Criando cópia local dos dados
        data = data.copy()
        # Tamanho da sequência de entrada
        data_len = len(data)

        for outer_loop in range(data_len):
            for inner_loop in range(0, data_len - outer_loop - 1):
                if data[inner_loop] > data[inner_loop + 1]:
                    data[inner_loop + 1], data[inner_loop + 1 + 1] = data[inner_loop + 1 + 1], data[inner_loop + 1]

        return data
    
    def __repr__(self):
        return super().__repr__()
    
class QuickSortStrategy(SortStrategy):
    # Dando nome para a estratégia
    _name = "Quick"
    
    def _partition(self, array, low, high):
        # Elemento mais a direita como pivô
        pivot = array[high]

        # Índice do maior elemento
        i = low - 1

        # Passando por todos os elementos comparando cada um com o pivo
        for j in range(low, high):
            if array[j] <= pivot:
                # Se um elemento menor que o pivõ é encontrado o trocamos
                # com o maior elemento com índice i
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])

        # Trocando pivô com o maior elemento especificado por i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # Retorna posição onde a partição foi feita
        return i + 1
    
    def _quick_sort(self, array, low, high):
        if low < high:
            # Encontra pivô colocando elementos menores a direita e maiores à
            # esquerda
            pivot = self._partition(array, low, high)

            # Chamadas recursivas à esquerda...
            self._quick_sort(array, low, pivot - 1)
            
            # ... e à direita do pivô
            self._quick_sort(array, pivot + 1, high)

    def sort(self, data: list[int]) -> list[int]:
        # Criando cópia local dos dados
        data = data.copy()
        # Tamanho da sequência de entrada
        data_len = len(data)

        # Ordenando dados
        self._quick_sort(data, 0, data_len -1)

        # Retornando dados ordenados
        return data
    
class Context:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def execute(self, data: list[int]) -> list[int]:
        print(f"Ordenando utilizando o metodo de {self._strategy}")
        self._strategy.sort(data)

if __name__ == "__main__":
    unsorted_data = [1, 7, 4, 1, 10, 9, -2]

    print("Unsorted Array")
    print(unsorted_data)

    context = Context(BubbleSortStrategy())
    data = unsorted_data.copy()
    context.execute(data)
    print("Sorted array: ")
    print(data)
    
    context.set_strategy(QuickSortStrategy())
    data = unsorted_data.copy()
    context.execute(data)
    print("Sorted array: ")
    print(data)
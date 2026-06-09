from typing import Any, List

class Deque:

    # Construtor
    def __init__(self) -> None:
        self.__data: List[Any] = []

    # Insere um elemento em uma posição específica
    def insert_index(self, index: int, elemento: Any) -> None:
        self.__data.insert(index, elemento)

    # Insere um elemento no final
    def insert_last(self, elemento: Any) -> None:
        self.__data.append(elemento)

    # Insere um elemento no início
    def insert_first(self, elemento: Any) -> None:
        self.__data.insert(0, elemento)

    # Remove e retorna o último elemento
    def remove_last(self) -> Any:
        if self.is_empty():
            raise IndexError("Não pode remover de um deque vazio")
        return self.__data.pop()

    # Remove e retorna o primeiro elemento
    def remove_first(self) -> Any:
        if self.is_empty():
            raise IndexError("Não pode remover de um deque vazio")
        return self.__data.pop(0)

    # Retorna a representação em string do deque
    def __repr__(self) -> str:
        return str(self.__data)

    # Retorna o último elemento sem removê-lo
    def last(self) -> Any:
        if self.is_empty():
            raise IndexError("Deque vazio")
        return self.__data[-1]

    # Retorna o primeiro elemento sem removê-lo
    def first(self) -> Any:
        if self.is_empty():
            raise IndexError("Deque vazio")
        return self.__data[0]

    # Retorna a quantidade de elementos
    def size(self) -> int:
        return len(self.__data)

    # Retorna uma cópia invertida do deque
    def invert(self):
        invertida = Deque()

        for elemento in reversed(self.__data):
            invertida.insert_last(elemento)

        return invertida

    # Remove todos os elementos
    def clear(self) -> None:
        self.__data.clear()

    # Verifica se o deque está vazio
    def is_empty(self) -> bool:
        return len(self.__data) == 0
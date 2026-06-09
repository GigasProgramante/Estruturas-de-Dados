from estrutura.deque import Deque
from estrutura.queue import Queue
from estrutura.stack import Stack

if __name__ == '__main__':
    pilha = Stack()
    fila = Queue()

    pilha.push("Empilhado 1")
    pilha.push("Empilhado 2")
    pilha.push("Empilhado 3")
    pilha.push("Empilhado 4")
    pilha.push("Empilhado 5")

    fila.enqueue("Enfilerado 1")
    fila.enqueue("Enfilerado 2")
    fila.enqueue("Enfilerado 3")
    fila.enqueue("Enfilerado 4")
    fila.enqueue("Enfilerado 5")

    print(pilha)
    print(fila)

    pilha.pop()
    fila.dequeue()

    print("\n--Depois de retirar:--")

    print(pilha)
    print(fila)

    print("\n--Está a vazia:--")

    print(pilha.is_empty())
    print(fila.is_empty())

    print("\n--Fila está cheia:--")

    print(fila.is_full())

    print("\n--Último elemento:--")

    print(pilha.peek())
    print(fila.peek())

    print("\n--Inverter pilha:--")

    pilha_invertida = pilha.invert()
    print(pilha_invertida)

    print("\n TESTES DEQUE")

    deque = Deque()

    deque.insert_last("111")
    deque.insert_last("222")
    deque.insert_last("333")
    deque.insert_last("444")
    deque.insert_last("555")

    print(deque)
    deque.insert_first("000")

    print(deque)

    deque.remove_last()
    deque.remove_first()

    print(deque)

    print(deque.first())
    print(deque.last())
    print(deque.size())

    invertida = deque.invert()

    print(invertida)
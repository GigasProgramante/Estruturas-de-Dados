class Queue:
    def __init__(self, max_size=None):
        """
        Inicializa uma fila vazia.
        :param max_size: Capacidade máxima da fila (None para ilimitada).
        """
        self._items = []
        self._max_size = max_size

    def enqueue(self, item):
        """Adiciona um item ao final da fila. Lança OverflowError se cheia."""
        if self.is_full():
            raise OverflowError("Não foi possível adicionar o item: a fila atingiu o limite máximo.")
        self._items.append(item)

    def dequeue(self):
        """Remove e retorna o primeiro item da fila (FIFO). Lança IndexError se vazia."""
        if self.is_empty():
            raise IndexError("Não foi possível remover: a fila está vazia.")
        return self._items.pop(0)

    def peek(self):
        """Retorna o primeiro item da fila sem removê-lo. Lança IndexError se vazia."""
        if self.is_empty():
            raise IndexError("Não foi possível espiar: a fila está vazia.")
        return self._items[0]

    def is_empty(self):
        """Retorna True se a fila estiver vazia, False caso contrário."""
        return len(self._items) == 0

    def is_full(self):
        """Retorna True se a fila atingiu o limite max_size, False caso contrário."""
        if self._max_size is None:
            return False
        return len(self._items) >= self._max_size

    def size(self):
        """Retorna o número de elementos atuais na fila."""
        return len(self._items)

    def clear(self):
        """Esvazia completamente a fila."""
        self._items.clear()

    def __repr__(self) -> str:
        return str(self._items)


# Bloco de execução principal (Main)
if __name__ == "__main__":
    print("=== DEMONSTRAÇÃO DE USO E TRATAMENTO DE ERROS ===\n")

    # -------------------------------------------------------------------------
    # CASOS DE SUCESSO (Fluxo Normal)
    # -------------------------------------------------------------------------
    print("--- Cenário 1: Criando e usando uma fila normal (Ilimitada) ---")
    fila = Queue()

    # Enfileirando itens
    fila.enqueue("Primeiro Cliente")
    fila.enqueue("Segundo Cliente")
    fila.enqueue("Terceiro Cliente")
    print(f"Itens adicionados. Tamanho atual da fila: {fila.size()}")

    # Espiando o topo (peek)
    print(f"Próximo a ser atendido (peek): '{fila.peek()}'")

    # Desenfileirando (dequeue)
    print(f"Atendendo: '{fila.dequeue()}'")
    print(f"Atendendo: '{fila.dequeue()}'")
    print(f"Tamanho da fila após atendimentos: {fila.size()}")
    print(f"A fila está vazia? {fila.is_empty()}")

    # Limpando a fila
    print("\n--- Cenário 2: Limpando a fila ---")
    fila.clear()
    print(f"Fila limpa. Tamanho: {fila.size()}")
    print("-" * 50)

    # -------------------------------------------------------------------------
    # CASOS DE ERRO TRATADOS
    # -------------------------------------------------------------------------
    print("\n--- Cenário 3: Forçando e tratando erro de Fila Vazia (IndexError) ---")

    # Tentando remover de uma fila vazia
    try:
        fila.dequeue()
    except IndexError as erro:
        print(f"Capturado com sucesso -> {erro}")

    # Tentando espiar uma fila vazia
    try:
        fila.peek()
    except IndexError as erro:
        print(f"Capturado com sucesso -> {erro}")

    print("-" * 50)
    print("\n--- Cenário 4: Forçando e tratando erro de Fila Cheia (OverflowError) ---")

    # Criando fila com limite estrito de 2 elementos
    fila_restrita = Queue(max_size=2)
    fila_restrita.enqueue("Documento A")
    fila_restrita.enqueue("Documento B")
    print(f"Fila preenchida. Ela está cheia? {fila_restrita.is_full()}")

    # Tentando forçar o estouro de capacidade (Overflow)
    try:
        print("Tentando adicionar um terceiro documento...")
        fila_restrita.enqueue("Documento C")
    except OverflowError as erro:
        print(f"Capturado com sucesso -> {erro}")

    print("\n================ TESTES CONCLUÍDOS ================")
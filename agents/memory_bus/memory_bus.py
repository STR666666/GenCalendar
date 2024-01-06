class MemoryBus:
    def __init__(self, memory=None):
        self._memory = memory

    def read_all(self):
        return self._memory
    
    def update_memory(self, memory):
        self._memory = memory